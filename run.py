import random

Name = input("enter your name here ")
print("Welcome",name, "To The Hangman Game fruit Guessing Game ")
print("------------------")
print("You Have 10 Guess Good Luck!!") 

wordDictionary = [ "apple" ,"apricots" ,"avocado" ,"banana", "blackberries" ,'blackcurrant' ,"blueberries"]

### Choose a random word
randomWord = random.choice(wordDictionary)




