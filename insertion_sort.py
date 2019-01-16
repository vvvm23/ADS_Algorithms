def sort(L):
    n = len(L)
    for j in range(1, n):
        x = L[j]
        i = j - 1
        while i >= 0 and L[i] > x:
            L[i+1] = L[i]
            i = i - 1
        L[i+1] = x   
    return L