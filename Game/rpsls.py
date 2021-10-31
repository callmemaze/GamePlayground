# Rock-paper-scissors-lizard-Spock template

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

#Converts name to numnber
def nameToNumber(name):
    pass
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        print("Invalid!")

#Converts number to name
def numberToName(number):
    pass
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
        print("Invalid!")

        
def rpsls(playerChoice):
    print("")
    print("Player Choice is:",playerChoice)
    choice=nameToNumber(playerChoice)
    randomGuess=random.randrange(0,5)
    compGuess=numberToName(randomGuess)
    print("Computer Choice:",compGuess)
    if((choice-randomGuess)%5==1 or (choice-randomGuess)%5==2):
        print("Player Wins!")
    elif ((choice-randomGuess)%5==-3 or (choice-randomGuess)%5==-4):
        print("Player Wins!")
    elif((choice-randomGuess)%5==-1 or (choice-randomGuess)%5==-2):
        print("Computer Wins!")
    elif((choice-randomGuess)%5==3 or (choice-randomGuess)%5==4):
        print("Computer Wins!")
    else:
        print("Draw!")

#Tester
#rpsls(input("Enter:"))
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
