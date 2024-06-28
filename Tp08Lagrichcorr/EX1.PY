mydict = {"device": "laptop" , "constructeur": "acer" , "ram": "8G" , "processeur" : "Intel core i5", "stockage": "500 G"}

# print(d)
mydict["stockage"]="750 G"
# print(d)

# cle = []
# for i in mydict.keys():
#     cle.append(i)
# print(cle)

print("\n cles:\n")
for i in mydict.keys():
    print(i)
print("\n Valeurs:\n")
for i in mydict.values():
    print(i)
print("\n Pair Cles - Valeurs:\n ")
for k,v in mydict.items():
    print(f"{k} : {v}")

# mydict["Système d'exploitation"] = "Windows 10"
# print(mydict)
