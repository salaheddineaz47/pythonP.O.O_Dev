def Triple(L):
    list1 = []
    for i in range(len(L) - 1):
        caree = L[i]**2
        for j in range(len(L)):
            if L[j] == caree:
                list1.append(L[i])
    return list1


K = [1, 2, 3, 4, 5, 67, 25, 6, 267, 36, 8, 64]


print(Triple(K))
