# The K Weakest Rows in a Matrix
import operator

mat = [[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]]

k = 3


def kWeakestRows(mat, k):
    weakest = {}

    for i in range(len(mat)):
        soldiers = mat[i].count(1)
        weakest[i] = soldiers

    weakest = sorted(weakest.items(), key=operator.itemgetter(1))

    lst = []

    for soldier in weakest:
        lst.append(soldier[0])

    return lst[:k]


print(kWeakestRows(mat, k))