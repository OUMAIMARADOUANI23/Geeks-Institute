from datetime import datetime

date_str = input("Entrez votre date de naissance (format DD/MM/YYYY) : ")

naissance = datetime.strptime(date_str, "%d/%m/%Y")
aujourdhui = datetime.today()
age = aujourdhui.year - naissance.year
if (aujourdhui.month, aujourdhui.day) < (naissance.month, naissance.day):
    age -= 1
nb_bougies = age % 10
ligne_bougies = "   " + "i" * nb_bougies + " " * (11 - nb_bougies)
gateau = f"""{ligne_bougies}
  |:H:a:p:p:y:|
__|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~"""
annee = naissance.year
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(gateau)
    print(gateau)
else:
    print(gateau)

