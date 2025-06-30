a=str(input("Donnez-moi une longue phrase sans 'A' : "))

if ("a") in a.lower():
    print("❌ La première phrase contient la lettre 'A'!!")
    quit()
print("✅ Phrase acceptée :", a)

b=str(input("Donnez moi le deuxieme longue phrase sans A "))

if ("a") in b.lower():
    print("❌ La deuxième phrase contient la lettre 'A'. Game over !")
    quit()    
print("✅ Deuxième phrase acceptée :", b)   

if len(a) > len(b):
    print("🏆 La première phrase est la plus longue !")
elif len(a) < len(b):
    print("🏆 La deuxième phrase est la plus longue !")
else:
    print("🤝 Les deux phrases ont la même longueur !")
    