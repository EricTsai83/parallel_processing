from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import urlopen 

MULTITHREADING_TITLE="API Calls Multithreading"
MULTIPROCESSING_TITLE="API Calls Multiprocessing"

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
# add 'base' parameter will seting, when Multithreading & Multiprocessing function call
def download(url, base):
    start = time.time()-base # base parameter will be the begin time
    try:
        resp = urlopen(url)
    except Exception as e:
        print ('ERROR: %s' % e)
    stop = time.time()-base
    return start,stop
