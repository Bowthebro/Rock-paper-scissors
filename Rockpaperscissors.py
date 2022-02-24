import random
print("would you like to play?\n y or n")
yes_no = input()   
rock_paper_scissors = ["rock", "paper", "scissors"]

def game():

    print("rock paper scissors")
    
    user_input = input()
    robot_input = random.choice(rock_paper_scissors)
    print(robot_input)

def define_rules(user_input):
    if user_input == "rock":
        print("bruh") 

while yes_no == "y":
    game()
