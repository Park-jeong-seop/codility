"""
A is List, X is number

If A contains all the values from 0 to X
Returns the position value of the last found value

find success :
if A is [1, 3, 1, 5, 4, 2, 3, 5, 4], X is 5
return 5

find fail :
if A is [2, 2, 2], X is 2
return -1
"""
def solution(A, X):
    num = 0
    arr = [0]*X

    for k in range(len(A)):
        if arr[A[k]-1] == 0:
            arr[A[k]-1] = 1
            num += 1
            if num == X:
                return k

    return -1
    
