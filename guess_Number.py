import random

""" guess game from 1 - 50 """
keyNumber = random.randint(1,50)

print ("Pick a number from 1 to 50")

# user has only 3 chances
for chances in range(1,4):
    print("Guess please")
    guess = int(input())

    if guess < keyNumber:
        print("Number picked it's too low")
    elif guess > keyNumber:
        print("Number picked it's too high")
    else:
        print("correct!")
        break
if guess == keyNumber:
    print("Congratualtions you won! ,you did it in:"+ str(chances)+"tries")
else:
    print("You lose , better luck next time !, the number was:"+str(keyNumber))