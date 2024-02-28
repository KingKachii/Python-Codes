#1. Introduce the calculator
print("Welcome to the tip calculator")

#2. Enter bill Amount
bill = float(input("What was the total bill? \n"))

#3. Enter tip percentage
tip_perc = float(
    input("What percentage tip would you like to give? 10, 12, or 15? \n"))

#4. Enter the number of persons the bill will be split into
persons = int(input("How many people to split the bill? \n"))

bill_total = bill * (1 + tip_perc / 100)
split_by_person = round(bill_total / persons, 2)
print(f"Each person should pay: ${split_by_person}")
