def sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = sort(l[:mid])
    right = sort(l[mid:])

    return merge(left, right)

def merge(left, right):
    count = 0
    out = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            count += 1
            if left[0] <= right[0]:
                out.append(left[0])
                left = left[1:]
            else:
                out.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            out = out + left
            left = []
        else:
            out = out + right
            right = []
    return out
