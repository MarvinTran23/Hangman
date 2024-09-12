import random


def get_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(word_list)


def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    guessed_letters = set()
    lives = 7
    round_count = 0

    def display():
        display_guessed_letters = ""
        for letter in word:
            if letter in guessed_letters:
                display_guessed_letters += letter
            else:
                display_guessed_letters += "_"

            display_guessed_letters += " "

        print(display_guessed_letters)

    round_count += 1
    print("Round", round_count)
    display()

    while lives > 0:

        user_guess = input("Guess a letter: ").lower()

        if user_guess in word_letters:
            guessed_letters.add(user_guess)
        elif user_guess in alphabet:
            lives -= 1
            print(f"Guessed letter is wrong! Lives: {lives}")
        elif len(user_guess) > 1:
            print("Invalid move: There are multiple letters in your input!")
            continue
        else:
            print("Guessed letter is not in alphabet!")
            continue

        if len(guessed_letters) == len(word_letters) and guessed_letters.issubset(word_letters):
            print(f"Congrats! You guessed the word \"{word}\"!")
            break

        print("_" * 30)
        round_count += 1
        print("Round", round_count)
        display()

    if lives <= 0:
        print("No lives are left!")
        print("Game over!")
        print(f"The word was \"{word}\"!")


play_game()
