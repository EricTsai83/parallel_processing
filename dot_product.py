from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import matplotlib.pyplot as plt
import numpy as np


MULTITHREADING_TITLE="Numpy Dot Product Multithreading"
MULTIPROCESSING_TITLE="Numpy Dot Product Multiprocessing"


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
# Numpy Functions
##############################################

# Dot Product
#Automatic parallel processing built works out of the box
#Depending on BLAS impl, MKL (default with anaconda3) does
#Should NOT see speedups with multithreading/processing

DIMS = 1500
numpy_dot_N = 10
DIMS_ARR = [DIMS for i in range(numpy_dot_N)]
a = np.random.rand(DIMS,DIMS)
b = np.random.rand(DIMS,DIMS)

def dot_product(i, base):
    start = time.time() - base
    res = np.dot(a,b)
    stop = time.time() - base
    return start,stop


