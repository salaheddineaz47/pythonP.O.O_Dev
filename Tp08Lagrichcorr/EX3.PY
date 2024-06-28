print("entrer l'entier n")
n = int(input())

newDict = {}
for i in range(1, n+1):
    newDict[i] = i * i

print(newDict)