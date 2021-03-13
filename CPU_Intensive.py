from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import matplotlib.pyplot as plt
import numpy as np


MULTITHREADING_TITLE="CPU Intensive Multithreading"
MULTIPROCESSING_TITLE="CPU Intensive Multiprocessing"


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
# CPU Intensive
##############################################
cpu_N = 10**7
ITERS = 10

def cpu_heavy(n,base):
    start = time.time() - base
    count = 0
    for i in range(n):
        count += i
    stop = time.time() - base
    return start,stop









