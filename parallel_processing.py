from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy as np
import time
import matplotlib.pyplot as plt
import glob
from PIL import Image
import random
import string
from urllib.request import urlopen  # for API call task

 
MULTITHREADING_TITLE="Multithreading"
MULTIPROCESSING_TITLE="Multiprocessing"


def visualize_runtimes(results, title):
    start,stop = np.array(results).T
    plt.barh(range(len(start)),stop-start,left=start)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.title(title)
    return stop[-1]-start[0]


def multithreading(func, args, workers):
    begin_time = time.time()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [begin_time for i in range(len(args))])
    return list(res)
        
def multiprocessing(func, args, workers):
    begin_time = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [begin_time for i in range(len(args))])
    return list(res)


##############################################
# API Calls task
##############################################
url_N = 10
URL = 'http://scholar.princeton.edu/sites/default/files/oversize_pdf_test_0.pdf'
urls = [URL for i in range(url_N)]


# 'base' parameter will seting, when Multithreading & Multiprocessing function call
def download(url, base):
    start = time.time()-base # base parameter will be the begin time
    try:
        resp = urlopen(url)
    except Exception as e:
        print ('ERROR: %s' % e)
    stop = time.time()-base
    return start,stop








##############################################
# IO Heavy
##############################################
TEXT = ''.join(random.choice(string.ascii_lowercase) for i in range(10**7*5))
text_N=12

def io_heavy(text,base):
    start = time.time() - base
    f = open('output.txt', 'wt', encoding='utf-8')
    f.write(text)
    f.close()
    stop = time.time() - base
    return start,stop




##############################################
# Numpy Functions
##############################################

# Numpy Addition

#Does not use parallel processing by default
#But will see speedups if multiprocessing used
#Because numpy sidesteps python's GIL
DIMS = 10000
numpy_add_N = 20
DIMS_ARR = [DIMS for i in range(numpy_add_N)]
a = np.random.rand(DIMS,DIMS)
b = np.random.rand(DIMS,DIMS)

def addition(i, base):
    # a = np.random.rand(DIMS,DIMS)
    # b = np.random.rand(DIMS,DIMS)
    start = time.time() - base
    res = a + b
    stop = time.time() - base
    return start,stop




# Dot Product
#Automatic parallel processing built works out of the box
#Depending on BLAS impl, MKL (default with anaconda3) does
#Should NOT see speedups with multithreading/processing

DIMS = 3000
numpy_dot_N = 10
DIMS_ARR = [DIMS for i in range(numpy_dot_N)]
a = np.random.rand(DIMS,DIMS)
b = np.random.rand(DIMS,DIMS)

def dot_product(i, base):
    start = time.time() - base
    res = np.dot(a,b)
    stop = time.time() - base
    return start,stop




# CPU Intensive

cpu_N = 10**7
ITERS = 10

def cpu_heavy(n,base):
    start = time.time() - base
    count = 0
    for i in range(n):
        count += i
    stop = time.time() - base
    return start,stop




# Resize Images
# https://github.com/python-pillow/Pillow/blob/c9f54c98a5dc18685a9bf8c8822f770492a796d6/_imagingtk.c

DATA_PATH='/home/bfortuner/workplace/data/imagenet_sample/'
fnames = list(glob.iglob(DATA_PATH+'*/*.JPEG'))
img_N = 5000

#This one takes IO so multithreading might be better?
def resize_img(fpath, base):
    img = Image.open(fpath)
    rimg = img.resize((224,224))
    img.close()
    return rimg







if __name__ == '__main__':
    N = 10
    URL = 'http://scholar.princeton.edu/sites/default/files/oversize_pdf_test_0.pdf'
    urls = [URL for i in range(N)]
    visualize_runtimes(multiprocessing(download, urls, 1), "Single Process")