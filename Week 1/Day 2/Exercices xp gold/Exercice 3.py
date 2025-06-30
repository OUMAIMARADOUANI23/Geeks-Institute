names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name_utilisateur=input("donner moi votre nom:")
if name_utilisateur in names:
    index = names.index(name_utilisateur)
    print(name_utilisateur,"est dans la liste à l'index ", index)
else:
    print("Désolé",name_utilisateur,"n'est pas dans la liste.")