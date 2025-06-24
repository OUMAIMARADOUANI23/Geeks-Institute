import random
def number(number_choix):
    random_number=random.randint(1,100)
    if number_choix==random_number:
        print("Success!")
    else:
        print("Fail! Your number:", number_choix ,",Random number: " ,random_number)

number(51)