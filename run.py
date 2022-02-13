import random 

wordlist = [ foxglove ,frazzled ,frizzled , blitz , blizzard , boggle , stretch , stronghold ,stymied ,zigzagging , zilch , zipper , zodiac ,zombie , equip , cycle ,jinx ,larynx , vixen]

word = random.choice(wordlist).lower()

guessed_correctly = []

guessed_incorrectly = []

tires = 5

hangman_count = -1 
while tries > 0:
    output =''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
            else:
                output +='_'
