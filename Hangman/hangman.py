import random
import hangman_words
import hangman_ascii_arts


# Welcome the player
print(hangman_ascii_arts.welcome_message)

# Choose a word
word = random.choice(hangman_words.words).upper()
word = "ANTEAT"
length = len(word)
guess = ["_"] * length

lives = 6
while lives>0:
    print(hangman_ascii_arts.HANGMANPICS[6-lives])
    print("Word = ", "".join(guess))
    new_guess = input("Enter your guess: ").upper()
    if new_guess in word:
        for j in range(length):
            if word[j] == new_guess:
                guess[j] = new_guess
        if "_" not in guess:
            print(hangman_ascii_arts.win_message)
            break
    else:
        lives -= 1
        if lives == 0:
            print(hangman_ascii_arts.HANGMANPICS[-1])
            print(hangman_ascii_arts.lose_message)
    
print("The word was :",word)


