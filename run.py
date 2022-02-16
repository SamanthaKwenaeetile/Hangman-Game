import random
def thehangman():

words_list = [ 'apple' , 'apricots' , 'avocado' ,'banana' , 'blackberries' ,'blackcurrant' ,'blueberries']

word = random.choice(words_list)

turns = 5
guessmade = ''
valid_entry = set('abcdefghijklmnopqrstuvwxyz')

while len(word)>0:
    main_word = ""
    missed = 0

    print("guess the word", main_word)
    guess = input()

    if guess in valid_entry:
        guessmade = guessmade+guess

    else:
            print("enter the right character")
            guess = input()


Name = input("enter your name here ")
print("Welcome",name, "To The Hangman Game fruit Guessing Game ")
print("------------------")
print("You Have 5 Guess Good Luck!!")

thehangman()