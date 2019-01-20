import insertion_sort

'''def select(L, i, left = -1, right = -1):
    if left == -1 or right == -1:
        left = 0
        right = len(L) - 1

    if len(L) <= 5:
        return insertion_sort.sort(L)[i]
    
    x = _select(L)
    L, k = partition(L, left, right, x)
    print(k)
    print(L)

    if i == k:
        return x
    elif i < k:
        return select(L, i, left, k - 1)
    else:
        return select(L, i, k + 1, right)

def _select(L):
    n = len(L)
    nb_full = n // 5
    part_size = n % 5

    sub_lists = [L[s*5:5 + s*5] for s in range(nb_full)]
    sub_lists.append(L[nb_full*5: nb_full*5 + part_size])
    sorted_sub_lists = list(map(insertion_sort.sort, sub_lists))

    medians = [X[len(X) // 2] for X in sorted_sub_lists]

    if len(medians) == 1:
        return medians[0]
    else:
        return _select(medians)

def partition(L, left, right, x):
    i = left - 1
    for j in range(left, right):
        if L[j] < x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[right] = L[right], L[i + 1]
    return L, i + 1

print(select([5,2,6,8,764,4123,42,1], 2))'''

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

def select_pivot(L):
    n = len(L)
    nb_full = n // 5
    part_size = n % 5

    sub_lists = [L[s*5:5 + s*5] for s in range(nb_full)]
    sub_lists.append(L[nb_full*5: nb_full*5 + part_size])
    sorted_sub_lists = list(map(insertion_sort.sort, sub_lists))

    medians = [X[len(X) // 2] for X in sorted_sub_lists]

    if len(medians) == 1:
        return medians[0]
    else:
        return select_pivot(medians)

def partition(L, left, right):
    x = select_pivot(L[left: right + 1])
    i = left - 1
    for j in range(left, right):
        if L[j] < x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[right] = L[right], L[i + 1]
    return L, i + 1

print(select([432,534,123,125,24,1,6], 4))