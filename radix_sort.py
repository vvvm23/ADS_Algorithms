import math
import queue
def sort(L):
    out_list = []
    n = len(L)
    L_max = max(L)
    digit = math.ceil(math.log10(L_max))
    buckets = [queue.Queue(n) for i in range(10)]

    for d in range(digit):
        for i in range(n):
            buckets[int((L[i] % (10**(d+1))) // 10**(d))].put(L[i])
        for i in range(10):
            for q in range(buckets[i].qsize()):
                out_list.append(buckets[i].get())
        L = out_list
        out_list = []
    return L

