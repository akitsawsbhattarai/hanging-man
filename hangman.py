import os
from wordlist import words
import random
import string
from termcolor import colored


def word_to_be_guessed(words):
    # random word by computer
    main_word = random.choice(words).upper()
    return main_word


def input_letter():
    letter = input('guess the letter ...  => ').upper()
    return letter
 
   
def display():
    print (colored("Game Started...", 'blue')) 

    
def find_index(mainword, letter):
    mainword_list = list(mainword) 
    indexes = [i for i, j in enumerate(mainword_list) if j == letter]
    print(indexes)
    return indexes
    
   
def matched_display(letter, indexes, string):
    string = string.replace(' ','')
    list_string = list(string)
    for index in indexes:
        list_string[index] = letter
        word=' '.join(list_string)
    return word
    
 
def hanging_man(count):
    man=("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
    if count == 6:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |       \n"
              "  |        \n"
              "  |        \n"
              "__|__\n")
    elif count == 5:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |        \n"
              "  |        \n"
              "__|__\n")
    elif count == 4:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |     |  \n"
              "  |        \n"
              "__|__\n")
    elif count == 3:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|   \n"
              "  |        \n"
              "__|__\n")
    elif count == 2:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\  \n"
              "  |        \n"
              "__|__\n")
    elif count == 1:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\  \n"
              "  |    /   \n"
              "__|__\n")
    elif count == 0:
        return ("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\  \n"
              "  |    / \  \n"
              "__|__\n")
        
    
        
    
   
def hangman_main():
        
    word_guessed_by_user = []
    alphabet = set(string.ascii_uppercase)
    
    mainword = word_to_be_guessed(words)
    
    if '-' in mainword or ' ' in mainword:
        print("/'-' or space is present")
    # print(f"'{mainword}'")
    stored_word = list(mainword)
    guessed_word = ''
    matchedguessedword =''
    
    for i in mainword:
        guessed_word +="_ "
    
    # print(*['_'for i in mainword], sep=' ', end='')
    # print()
     
    chance = 6
    already_guessed = False
    
    while len(stored_word)> 0 and chance>0:
        print()
        print(*['_'for i in mainword], sep=' ', end='') 
        print()     
        print()     
        print()     
        print(colored(f'you have {chance} chance left'))
        print(hanging_man(chance)) 
        print(colored(f'match word: {matchedguessedword}','green'))
     
        if already_guessed :
            print('You already guessed  it! Try another one.')  
            already_guessed = False 
        else:
            print()   
        print()
        
        letter = input_letter()  
        if letter in alphabet:
            if letter in word_guessed_by_user:
                already_guessed = True
                
            else:
                word_guessed_by_user.append(letter)
                if letter not in  mainword:
                    chance-=1
                                       
                    
                while letter in stored_word:
                    index = stored_word.index(letter)
                    addindex = find_index(mainword, letter)
                    matchedguessedword=matched_display(letter, addindex, guessed_word)
                    guessed_word = matchedguessedword
                    print(colored(matchedguessedword,'green'))
                    
                    stored_word.pop(index)
                    
      
            # print(stored_word)

        else:
            print('invalid character')
        print ('word guessed till now: ' , end='')
        for letter in word_guessed_by_user:
            if letter in mainword:
                print(colored(letter+' ', 'green'), end='')
            else:
                print(colored(letter+' ', 'red'), end='')
    
        os.system('cls')
    
        
    print()
     
    print(hanging_man(chance))  
    if guessed_word.replace(' ','') == mainword:   
        print(colored('whoa! you made it!','green'))
    else :
        print(colored(f'Sorry! you are hanged! The correct word is {mainword}','red'))
        
 
def play_game(): 
    print('------------------------------------------------------------------')
    print()
    continue_game = (input('do you  want to play? Y/N=> ')).lower()        
    if continue_game == 'y':
        os.system('cls')
        return True
    else :
        return False   
         
        
    
      
while play_game():
    display() 
    print() 
    hangman_main()
    print()
    

