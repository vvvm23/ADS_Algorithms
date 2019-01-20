def select(L, i, left = -1, right = -1):
    if left == -1 or right == -1:
        left = 0
        right = len(L) - 1

    if left == right:
        return L[left]
    else:
        L, p = partition(L, left, right)

        if i == p:
            return L[i]
        elif i < p:
            return select(L, i, left, p - 1)
        else:
            return select(L, i, p + 1, right)

def partition(L, left, right):
    x = L[right]
    i = left - 1
    for j in range(left, right):
        if L[j] < x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[right] = L[right], L[i + 1]
    return L, i + 1