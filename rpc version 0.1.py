import random
print("would you like to play?\n y or n")   
rock_paper_scissors = ["rock", "paper", "scissors"]
print("Valid inputs are: rock, paper and scissors")

def game():
    print("wanna play?")
    yes_no = input()
    while yes_no == "y":
        print("rock paper scissors")
    
        user_input = input()
        robot_input = random.choice(rock_paper_scissors)
        print(robot_input)
    
        if user_input != rock_paper_scissors:
            print("incorrect input")
            continue

        elif user_input == robot_input:
            print("draw")
            continue

    else:
        exit

print("END")