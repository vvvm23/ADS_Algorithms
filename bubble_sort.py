def sort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

    return L