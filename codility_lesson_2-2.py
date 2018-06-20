"""
A is List
A = [3, 9, 3, 7, 9]
res = 7
"""
def solution(A):
    doc = {}
    res = 0

    for list_item in A:
        try:
            doc[list_item] += 1
            if doc[list_item] == 3:
                doc[list_item] = 1
        except:
            doc[list_item] = 1

    print(doc)

    for doc_item in doc:
        if doc[doc_item] == 1:
            res = doc_item

    return res
