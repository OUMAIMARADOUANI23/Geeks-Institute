birthdays = {
    "Alice": "1995/03/22",
    "Mohamed": "1990/07/15",
    "Leila": "1988/11/05",
    "Youssef": "1999/01/10",
    "Fatima": "2002/09/30"
}
print("Bienvenue dans l'annuaire des anniversaires !")
print("Vous pouvez consulter les dates d'anniversaire des personnes de la liste !")
print("Voici les noms disponibles :"," ".join(birthdays.keys()))
name = input("Entrez le nom de la personne dont vous voulez connaître l'anniversaire : ")
if name in birthdays:
    print("L'anniversaire de : ",name,"est", birthdays[name])
else:
    print("Désolé, nous n'avons pas les informations d'anniversaire pour person", name)