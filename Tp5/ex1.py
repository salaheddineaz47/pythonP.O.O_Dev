try:
    x = float(input("Donnez un nombre réel : "))
    print(x)
except ValueError:

    print("La valeur est invalide")
except Exception as e:
    print(e)

print("La suite de programme........")
