def lengthOfWords(L):
    dic = {}
    k = L.split()
    for x in k:
        dic[x] = len(x)

    return dic


K = "Bonjour Anas Kamali"
print(lengthOfWords(K))
