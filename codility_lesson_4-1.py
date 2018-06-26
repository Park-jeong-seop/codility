"""
A is List

A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]

A is permutation return 1
A is not permutation return 0

ex)
A = [4, 1, 3, 2]
A' = [1, 2, 3, 4]
return 1

A = [4, 1, 3]
A' = [1, 3, 4]
return 0
"""
def solution(A):
  max_a = max(A)
    length = len(A)
    set_a = list(set(A))

    if max_a == length and len(A) == len(set_a) and sum(range(max_a+1)) == sum(set_a):
        return 1

    return 0
