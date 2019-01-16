def sort(L):
    quick_sort(L, 0, len(L) - 1)
    return L

def quick_sort(L, left, right):
    if left < right:
        L, pivot = partition(L, left, right)
        L = quick_sort(L, left, pivot - 1)
        L = quick_sort(L, pivot + 1, right)
    return L

def partition(L, left, right):
    x = L[right]
    i = left - 1
    for j in range(left, right):
        if L[j] < x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[right] = L[right], L[i + 1]
    return L, i + 1