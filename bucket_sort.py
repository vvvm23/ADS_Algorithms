def sort(L):
    n = len(L)
    K = max(L)
    buckets = [0]*(K+1)
    out_list = []
    for i in range(n):
        buckets[L[i]] += 1
    for i in range(K+1):
        for j in range(buckets[i]):
            out_list.append(i)

    return out_list