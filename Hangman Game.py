import random
import hangman_words # from hangman_words import word_list
import hangman_art # from hangman_art import stages
from replit import clear

#Update the word list to use the 'word_list' from hangman_words.py

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stages = hangman_art.stages
logo = hangman_art.logo

end_of_game = False
lives = 6


print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()


    if guess in display:
        print(f"You've already guessed {guess}")
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
