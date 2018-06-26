"""
A is List
A = [3, 1, 2, 4, 3]

p1 = |3 - (1+2+4+3)| = 7
p2 = |(3+1) - (2+4+3)| = 5
p2 = |(3+1+2) - (4+3)| = 1
p2 = |(3+1+2+4) - (3)| = 7

returns the minimal difference
result = 1

"""
left = A[0]
    right = sum(A[1:])
    res = abs(left - right)
    for count, item in enumerate(A[1:len(A)-1]):
        left += item
        right -= item
        if res > abs(left - right):
            res = abs(left - right)

    return res
