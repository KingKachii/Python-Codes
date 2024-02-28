import math
#from replit import clear
# Calculator

# Add 
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2 

# Divide
def divide(n1, n2):
   return n1 / n2

# dictionary
dict = {}
dict["+"] = add
dict["-"] = subtract
dict["*"] = multiply
dict["/"] = divide

# dict = {
#     "+" : add,
#     "-" : subtract,
#     "*" : multiply,
#     "/" : divide
# }

n1 = int(input("What is the first number?:"))


should_continue = True
while should_continue:
  # print(input("Which of these functions do you want to perform?"))
    for symbol in dict:
       print(symbol)
    function = input("Which of these functions do you want to perform?")
    n2 = int(input("What is the next number?:"))
    if function == "+":
        def add(n1, n2):
           return n1 + n2
    if function == "-":
        def subtract(n1, n2):
            return n1 - n2 
    if function == "*":
        def multiply(n1, n2):
            return n1 * n2
    else:
        def divide(n1, n2):
            return n1 / n2

    output = dict[function]
    result = output(n1, n2)
    print(result)

    question = input("Do you want to perform another calculation? Enter 'y' or 'n'")
    if question == "n":
      should_continue = False
      #clear()
      print(f"Answer = {result}")

    else:
      n3 = int(input("What is the next number?:"))
      n1 = result
      n2 = n3
