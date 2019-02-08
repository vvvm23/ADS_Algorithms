import math
import queue
def sort(L):
    out_list = []
    n = len(L)
    L_max = max(L)
    digit = math.ceil(math.log10(L_max)) + 1
    buckets = [queue.Queue(n) for i in range(10)]

    for d in range(0, digit):
        for i in range(n):
            buckets[(L[i] // 10**d)%10].put(L[i])
        for i in range(10):
            for q in range(buckets[i].qsize()):
                out_list.append(buckets[i].get())
        L = out_list
        out_list = []
    return L