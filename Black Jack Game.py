# import random module
import random

# display bank notes
bank = [1, 5, 25, 50, 100, 200]
money_in_bank = 1000
print(f"You have ${money_in_bank}.")
print(f"${bank[0]}, ${bank[1]}, ${bank[2]}, ${
      bank[3]}, ${bank[4]}, ${bank[5]}")

# Player Deal
player_deal_amount = int(input("How much do you want to deal?"))
print(f"Your Deal amount = ${player_deal_amount}")

# randomly select cards
card = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "k", "q"]
num_to_select = 2  # set the number to select here.
player_cards = random.sample(card, num_to_select)
print(f"Your cards are: {player_cards}.")

for index in range(len(player_cards)):
    if player_cards[index] == "a":
        player_cards[index] = 11
    elif player_cards[index] in ["j", "k", "q"]:
        player_cards[index] = 10

# print(player_cards)
player_card_1 = player_cards[0]
player_card_2 = player_cards[1]
player_total = player_card_1 + player_card_2
print(f"Your sum = {player_total}")
second_player_input = input(
    "Enter 'Hit' to deal another card, or 'Stand' to deal current cards:").lower()

should_continue = True
while should_continue:
    if second_player_input == "hit":
        next_card = random.choice(card)
        print(f"Your cards are: {next_card}.")
        if next_card == "a":
            next_card = 11
        elif next_card in ["j", "k", "q"]:
            next_card = 10
        second_player_input = input(
            "Enter 'Hit' to deal another card, or 'Stand' to deal current cards:").lower()
        if second_player_input == "stand":
            should_continue = False

    elif second_player_input == "stand":
        should_continue = False

    new_player_total = player_total + next_card
    player_total = new_player_total
    print(f"Your sum = {player_total}")


dealer_cards = random.sample(card, num_to_select)
print(f"Dealer cards = {dealer_cards}")
for index in range(len(dealer_cards)):
    if dealer_cards[index] == "a":
        dealer_cards[index] = 11
    elif dealer_cards[index] in ["j", "k", "q"]:
        dealer_cards[index] = 10

# print(dealer_cards)
dealer_card_1 = dealer_cards[0]
dealer_card_2 = dealer_cards[1]
dealer_threshold = 17
dealer_total = dealer_card_1 + dealer_card_2
print(f"Dealer sum = {dealer_total}")
while dealer_total < dealer_threshold:
    print(f"initial dealer sum is less than 17. \nDealer gets another card.")
    next_dealer_card = random.choice(card)
    print(f"Dealer's new card = {next_dealer_card}")
    if next_dealer_card == "a":
        next_dealer_card = 11
    elif next_dealer_card in ["j", "k", "q"]:
        next_dealer_card = 10
    new_dealer_total = dealer_total + next_dealer_card
    dealer_total = new_dealer_total
    if dealer_total >= dealer_threshold:
        print(f"Dealer's new sum = {dealer_total}")

if player_total > dealer_total:
    print("You win")
    money_in_bank += player_deal_amount
    print(f"Your new balance: ${money_in_bank}")

elif player_total < dealer_total and dealer_total <= 21:
    print("You lose.")
    money_in_bank -= player_deal_amount
    print(f"Your new balance: ${money_in_bank}")

elif player_total == dealer_total:
    print("It's a draw")
    money_in_bank = money_in_bank

else:
    print("You win")
    money_in_bank += player_deal_amount
    print(f"Your new balance: ${money_in_bank}")

next_player_input = input(
    "Enter 'Yes' to deal again, or 'No' to exit the game:").lower()

play_again = False
while play_again:
    if next_player_input == "yes":
        play_again = True
        print(next_player_input)
