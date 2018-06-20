"""
A is List
K is Int
A = [3, 8, 9, 7, 6]
K = 3
res = [9, 7, 6, 3, 8]
"""
def solution(A, K):
    arr = []
    length = len(A)
    if length == 0:
        return A
    K = K % length
    for x in range(0, K):
        arr.append(A[length-K+x])
    arr.extend(A[0:length-K])
    return arr
