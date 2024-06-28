try:
    c = input("Donnez une chaine de caractère : ")
    n1 = int(input("Donnez le premier indice : "))
    n2 = int(input("Donnez le deuxième indice : "))
    k = ""
    if (n1 >= 0 and n1 < len(c) and n2 >= 0 and n2 < len(c) and n2 - n1 >= 2):
        for j in range(n1, n2+1):
            k += c[j]
    else:
        raise Exception("les indice sont invalides")
except ValueError:
    print("La valeur est invalide")
except Exception as e:
    print(e)

print("La suite de programme........")

# K = "gsggsg"
# n1 = 0
# n2 = 3
# s = ""
# for i in range(n1, 7):
#     s += K[i]
# print(s)
