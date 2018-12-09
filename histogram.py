import numpy as np
from operator import add
import threading
import multiprocessing
import time
import matplotlib.pyplot as plt

def histogram(data, data_range, return_tab):
    return_tab.extend([0]*data_range)
    for number in data:
        return_tab[number] = return_tab[number] + 1
    return return_tab

def wrap_hist(data, data_range, queue):
    queue.put(histogram(data, data_range, []))

if __name__ == '__main__':

    data = np.random.randint(10, size = 50000000)

    # klasyczne liczenie histogramu
    result_1 = []
    start = time.time()
    histogram(data, 10, result_1)
    end = time.time()
    print(end - start)
    print(result_1)

    # wątki
    print("\nwątki: ")
    result_t1 = []
    result_t2 = []
    t1 = threading.Thread(target=histogram, args=(data[:25000000], 10, result_t1))
    t2 = threading.Thread(target=histogram, args=(data[25000000:], 10, result_t2))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    result_thread = list(map(add, result_t1, result_t2))
    end = time.time()
    print(end - start)
    print(result_thread)

    # procesy
    print("\nprocesy: ")
    result_p1 = []
    result_p2 = []
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=wrap_hist, args=(data[:25000000], 10, q))
    p2 = multiprocessing.Process(target=wrap_hist, args=(data[25000000:], 10, q))
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    result_process = list(map(add, q.get(), q.get()))
    end = time.time()
    print(end - start)
    print(result_process)

    plt.bar(np.arange(10), result_process)
    plt.show()