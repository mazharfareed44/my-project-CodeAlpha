#we are to creat a list of predefined 5 words here we go
predefined_words=["task","by","code","alpha","hangman"]
# here we are using random module which will be gving random numnber by itself
import random
random_word=random.choice(predefined_words)
# here we are using underscore to diplay progress to player and chosen hidden word by random module
game_proceeding=["_"]*len(random_word)
attempts_allowed=6
print("Welcome to Hangman,Check your guessing ability")
#here we join str and list to shwo our interphaseZ
print("word"," ".join(game_proceeding))
#now we will use while loop which will proceed untill we attempts are greater than zero and word is not completelu gussed
while attempts_allowed >0 and "_" in game_proceeding:
#here is player`s input means guess
    guess=input("enter your guess") .lower()
#here is used if condition which is checking guess is correct add it to pogress otherwsie decrease one attepmt from 6
    if guess in random_word:
        for index in range(len(random_word)):
               if random_word[index]==guess:
                    game_proceeding[index]=guess
        print("good move on:"," ".join(game_proceeding))
    else:
        attempts_allowed -=1
        print("oops its not correct! Attempts left",attempts_allowed)
# now this condition is shwoing if there is no space in progress mean all lettes are guessed and player has won else lost
if "_" not in game_proceeding:
            print("Hurrah! You won, the word was ",random_word)
else:
            print("Alas!,Bad luck this time,Game over,the word was",random_word)
                
