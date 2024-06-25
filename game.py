# int num = intpu{"Enter the number of players"}

import random



def calculator(flag,  score1, score2 ):
    roll = random.randint(1,6)
    print("You rolled a: ", roll)
    if roll ==1: 
        if flag ==0 : 
            score1 = 0
            print("Your score is: ", score1)
            flag = 1
            print("Now it is your turn player 2")
        elif flag ==1 : 
            score2 = 0
            print("Your score is: ", score2)
            flag = 0
            print("Now it is your turn player 1")
    else:       
        if flag == 0: 
            score1 = score1 + roll
            print("Your score is: ", score1)
        elif flag == 1: 
            score2 = score2 + roll 
            print("Your score is: ", score2)

    return flag,score1,score2
    
score1 =0
score2 = 0
flag = 0 

print("The game begins now player 1 will start!")

while score1 <50 and score2 <50:
    char = input("Do you want to roll the dice? (y/n): " )
    if char == 'y': 
        flag,score1, score2 = calculator(flag,score1,score2)
    if char == 'n': 
        if flag == 0: 
            print("Your total score is: ", score1)
            flag = 1
            print("Now it is your turn player 2!")
            print("Your total score is: ", score2)

        else: 
            print("Your total score is:" , score2)
            flag = 0
            print("Now it is your turn player 1!")
            print("Your total score is: ", score1)

if(score1>50) :
    print("Player 1 is the winner!")
if(score2>50) :
    print("Player 2 is the winner") 
        




