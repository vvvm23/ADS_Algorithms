def search(L, x, left=-1, right=-1):
    if left == -1 or right == -1:
        left = 0
        right = len(L) - 1

    if right == left and L[left] != x:
        print(x, "does is not in the inputted list!")
        return -1

    p = (left + right) // 2

    if L[p] == x:
        return p

    if x > L[p]:
        return search(L, x, p + 1, right)
    else:
        return search(L, x, left, p - 1)
