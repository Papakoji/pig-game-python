# int num = intpu{"Enter the number of players"}

import random



def roll():
     return random.randint(1,6) 

    
while True: 
     num = int(input("Enter the number of players (2-4): "))
     if 2 <= num <= 4: 
          break
     else :
          print("Invalid entry")

scores = [0 for _ in range(num)]
print(len(scores))
max_score = 50

while max(scores) < max_score:
     for index in range(num):
        print("Player number ", index+1, " it is your turn now")
        current_score = 0
        print("Your current score right now is ", current_score)
        while True:
             char = input("Do you want to roll the dice? (y/n)")
             if(char.lower()!='y'):
                  break
             
             val= roll()
             if val==1: 
                current_score = 0
                print("You rolled a 1.Your turn is done now!")
                break
             else: 
                print("You just rolled a ", val)
                current_score += val
                print("Your current score is ", current_score)
        scores[index] += current_score
        print("Your final score now is :", current_score)  

win = max(scores)
winner = scores.index(win)
print("The winner is ", winner+1, " ! Their score is: ", win)
        
          
          
        




