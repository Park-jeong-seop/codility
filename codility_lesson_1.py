"""
Find the number of 0 between 1

N is Int
N = 9 | binary = 1001
res = 2
"""
def solution(N):
    # write your code in Python 3.6
    count = 0
    real_count = 0
    flag = False
    while N > 0:
        if flag is True:
            if N % 2 == 0:
                count += 1
            else:
                if real_count <= count:
                    real_count = count
                count = 0
        else:
            if N % 2 == 1:
                flag = True
        N = N // 2

    return real_count
