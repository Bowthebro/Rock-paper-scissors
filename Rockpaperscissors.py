import random
print("would you like to play?\n y or n")
yes_no = input()   
rock_paper_scissors = ["rock", "paper", "scissors"]
valid_inputs = 

def game():

    print("rock paper scissors")
    
    user_input = input()
    robot_input = random.choice(rock_paper_scissors)
    print(robot_input)
    
    if user_input != str:
        continue

 

while yes_no == "y":
    game()
