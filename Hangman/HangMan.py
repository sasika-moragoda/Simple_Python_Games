import random
import string
from pyparsing import one_of
from WordFile import word_list

def selectValidWord(word_list):
    '''
    select a random letter from the given word list and check that word contain "-" or " ".
    if it contain "-" or " ", then keep choosing word till find a clean one_of
    '''

    selected_word = random.choice(word_list)
    while "-" in selected_word or " " in selected_word:
        selected_word = random.choice(word_list)
    
    return selected_word.upper()

def display():
    word = selectValidWord(word_list)
    word_letters = set(word)    #letters in the selected word get to a list
    alphabet = set(string.ascii_uppercase)  #26 letters in english alphabet in a list
    used_letters = set() #user already guessed letters
    lives = 9

    while len(word_letters) > 0 and lives > 0:

        print("You have guessed these lettrs : ", " ".join(used_letters)) #print used_letters list with out ","

        guessing_word = [letter if letter in used_letters else "-" for letter in word]
        print("word : ", " ".join(guessing_word))

        print("You have" , lives, "lives left")
        guessed_letter = input("You have lives left guess a letter : ").upper()
        print("\n")

        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
            else:
                lives -=1
                print("Wrong guess")
        
        elif guessed_letter in used_letters:
            print("Letter", guessed_letter, "already guessed")

        else:
            print("This input", guessed_letter, "is not a letter")

    if lives == 0:
        print("You lost the word is", word,)
    else:
        print("WOW!!!\nYou guessed the correct word" ,word)


selectValidWord(word_list)
display()