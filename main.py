import random
import hangman_art
import hangman_words
from replit import clear

choice = input(
    "Do you want to play in Engish or Spanish?\n¿Quieres jugar en inglés o español?\n\nType '1' for English or '2' for Spanish.\nTeclea '1' para inglés o '2' para español.")
print(choice)

# English

if choice == "1":
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(hangman_art.logo)

    display = []
    for _ in range(word_length):
        display += "_"

    print(f"{' '.join(display)}")

    guessed = []
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear()
        if guess in guessed:
            print("You already entered that letter. Try a different one.")
        guessed += guess

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"Sorry, your guess of '{guess}' is not in the word.\nYou lost a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")
        # print(f"Your guesses so far are: {' '.join(guessed)}")

        if "_" not in display:
            end_of_game = True
            print("Well done! You win.")

        print(hangman_art.stages[lives])

# Spanish

if choice == "2":
    chosen_word = random.choice(hangman_words.word_list_es)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6