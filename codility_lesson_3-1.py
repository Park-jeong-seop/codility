"""
X is start from
Y is destination
D is distance to move
X, Y, D are Int
X = 10, Y = 85, D = 30
res = 3
"""
def solution(X, Y, D):
    tmp = (Y-X) % D
    res = int((Y-X) / D)

    if tmp != 0:
        return res + 1
    return res
