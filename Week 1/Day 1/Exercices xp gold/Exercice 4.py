names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name=input("Enter your name ")
if name in names:
    index=names.index(name)
    print("Hello" , name, index)
else :
    print("is not in the list.")