import random
def get_valid_word(words):
    word = random.choice(words)  
    words = [ 'apple' , 'apricots' , 'avocado' ,'banana' , 'blackberries' ,'blackcurrant' ,'blueberries']
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def Hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_upperacse)
    used_letters = set()

turns = 10
guessmade = ''
abcdefghijklmnopqrstuvwxyz

while len(word)>0:
    main_word = "" 
    
    for letter in word:
        if letter in guessmade:
            main_word = main_word+letter
    else:
        main_word=main_word+"_"

        if main_word == word:
            print(main_word)
            print("well done you have won! ;)")
            break

    print("Guess The Furit", main_word)
    guess = input()

    if guess in valid_entry:
        guessmade = guessmade+guess
        
    else:
            print("enter the right character")
            guess = input()

if guess not in word:
turns = turns -1

if turns == 10:
    Print("You have ten turns left")
    Print("----------")

if turns == 9:
    print("You have nine turns left")
    Print("----------")
    Print("     O     ")

if turns == 8:
    Print("You have eight turns left")
    Print("----------")
    Print("     O     ")
    Print("     |    ")
    
if turns == 7:
    Print("You seven turns left")
    Print("----------")
    Print("     O     ")
    Print("     |    ")

if turns == 6:
    Print("You have six turns left")
    Print("----------")
    Print("     O     ")
    Print("     |    ")
    Print("     /    ")
   
if turns == 5:
    Print("You have five turns left")
    Print("----------")
    Print("     O     ")
    Print("     |    ")
    Print("    / \  ")

if turns == 4:
    Print("You have four turns left")
    Print("----------")
    Print("    \ O     ")
    Print("     |    ")
    Print("    / \  ")
    
if turns == 3:
    Print("You have three turns left")
    Print("----------")
    Print("    \ O /   ")
    Print("      |    ")
    Print("     / \  ")

if turns == 2:
    Print("You have two turns left")
    Print("----------")
    Print("    \ O /      | ")
    Print("      |    ")
    Print("     / \  ")

if turns == 1:
    Print("You have one turn left")
    Print("----------")
    Print("    \ O /   ")
    Print("      |    ")
    Print("     / \  ")

if turns == 0:
    Print("You have lost!!!")
    Print(" try you luck next time")
    Print("----------")
    Print("     O__|   ")
    Print("    /|\   ")
    Print("    / \  ")
    
    

Name = input("enter your name here ")
print("Welcome",name, "To The Hangman Game fruit Guessing Game ")
print("------------------")
print("You Have 5 Guess Good Luck!!")

thehangman()