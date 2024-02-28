""#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ''' 
#   VALENTINE's APPROACH = HARDDDDD!!!!!
# '''
# x_letters = random.sample(letters, nr_letters)
# x_symbols = random.sample(symbols, nr_symbols) 
# x_numbers = random.sample(numbers, nr_numbers)

# my_list = [x_letters, x_symbols, x_numbers]
# # Flatten the nested list using a nested loop
# flattened_list = []
# for items in my_list:
#     for item in items:
#         flattened_list.append(item)

# random.shuffle(flattened_list)
# password = ''.join(flattened_list)

# print(f"Your password is:{password}")


''' 
  SIMPLIFIED APPROACH = EASIER & CLEANER!!!!!
'''
#set your password to an empty string
password = []

#create your loop
for char in range(1, nr_letters + 1):
  #randomly choose a letter from the list
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  #randomly choose a symbol from the list
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  #randomly choose a number from the list
  password += random.choice(numbers)

random.shuffle(password)

your_password = ""
for char in password:
  your_password += char
print(f"Your password is:{your_password}")
