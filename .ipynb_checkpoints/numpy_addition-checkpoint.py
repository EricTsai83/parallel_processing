from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import matplotlib.pyplot as plt
import numpy as np


MULTITHREADING_TITLE="Numpy Addition Multithreading"
MULTIPROCESSING_TITLE="Numpy Addition Multiprocessing"


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

# Numpy Addition

#Does not use parallel processing by default
#But will see speedups if multiprocessing used
#Because numpy sidesteps python's GIL
DIMS = 8000
numpy_add_N = 16
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