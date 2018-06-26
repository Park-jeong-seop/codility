"""
find missing element
A is List
A = [2, 3, 1, 5]
res = 4
"""
def solution(A):
    length = len(A)+2
    arr = [0]*length
    count = 0
    for item_A in A:
        arr[item_A] = 1

    for item_arr in arr[1:]:
        count += 1
        if item_arr == 0:
            return count
