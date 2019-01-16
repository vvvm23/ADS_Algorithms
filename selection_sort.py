def sort(L):
    n = len(L)
    for i in range(n - 1):
        x = L[i]
        p = i
        for j in range(i + 1, n):
            if L[j] < x:
                x = L[j]
                p = j
        L[i], L[p] = L[p], L[i]
    return L