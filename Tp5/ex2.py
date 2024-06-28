try:
    n = int(input("Donnez la longeur de la liste : "))
    s = []
    for i in range(n):
        print("Donnez la valeur numéro : ", i+1)
        r = int(input())
        s.append(r)
    print(s)
    x = int(input("Donnez un indice de la liste : "))
    print(s[x])
except ValueError:
    print("La valeur est invalide")
except IndexError:
    print(f"L'index est en dehors  de la liste {s} ")
except Exception as e:
    print(e)

print("La suite de programme........")
