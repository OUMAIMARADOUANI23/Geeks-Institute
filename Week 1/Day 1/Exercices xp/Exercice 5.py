
my_fav_numbers={1,3,5,9}
print("My favorite numbers:" ,my_fav_numbers)

my_fav_numbers.add(2)
my_fav_numbers.add(7)
print("After adding two numbers:" ,my_fav_numbers)

my_fav_numbers.remove(7)
print("After removing the last added number:" , my_fav_numbers)

friend_fav_numbers={1,3,5,6,7}
print("Friend's favorite numbers:", friend_fav_numbers)

our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)