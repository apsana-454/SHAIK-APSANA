import random

def choose_word():
    words = ['apple', 'banana', 'python', 'guitar', 'planet']
    return random.choice(words)

def display_masked(word, guessed_letters):
    return ' '.join([ch if ch in guessed_letters else '_' for ch in word])

def play_hangman():
    MAX_INCORRECT = 6                       
    word = choose_word()                   
    guessed_letters = []                   
    incorrect = 0

    print("Welcome to Hangman! Guess the word, one letter at a time.")
    print(f"You have {MAX_INCORRECT} incorrect guesses allowed.\n")

    while incorrect < MAX_INCORRECT and not all(ch in guessed_letters for ch in word):
     
        print("Word:           ", display_masked(word, guessed_letters))
        print("Guessed letters:", ', '.join(guessed_letters) if guessed_letters else "None")
        print(f"Incorrect guesses left: {MAX_INCORRECT - incorrect}")

        guess = input("Enter a single letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            incorrect += 1
            print("Wrong guess.\n")

    if all(ch in guessed_letters for ch in word):
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you're out of guesses. The word was:", word)

if __name__ == "__main__":
    play_hangman()
