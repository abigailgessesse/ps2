import random

# Today we are playing rock, paper, scissors! Since we need someone to practice with,
# let's write a program that will play the game with us. We will write multiple functions to get this all working.
# Go line by line and complete the TODOs and instructions in each function.

# MAKE SURE TO RUN THE TESTS FOR EACH FUNCTION BEFORE MOVING ON TO THE NEXT ONE!
# Each test that fails will directly effect your grade, so make sure to test your functions!

# In order, the functions you will need to write are:
# get_user_choice
# get_computer_choice
# clean_input
# validate_input
# check_winner
# YOUR NAME HERE: Abigail Gessesse
#_______________________________________________________________________________________________________________________

def get_user_choice():
    """
    Ask the user for their move and save it! 
    Problem 1: 10 points possible
    """
    user_choice = input("Enter your choice: ")

    return user_choice  # Return the user's choice (No need to modify this line)

# pytest -k test_get_user_choice



#_______________________________________________________________________________________________________________________

def get_computer_choice():
     """
     Generates a random choice for the computer.
     Problem 2: 15 points possible
     """
     # ANOTHER OPTION: computer_choice = choices[random.randint(0, 2)]
     # choices = ["rock", "paper", "scissors"]
     number = random.randint(1, 3)
     if number == 1:
        computer_choice = "rock"
     elif number == 2:
        computer_choice = "paper"
     else:  # number == 3
        computer_choice = "scissors"
 
     return computer_choice

# pytest -k test_get_computer_choice

#_______________________________________________________________________________________________________________________

def clean_input(user_choice):
     """
     This function should clean the user's input to ensure it is lowercase and has no leading/trailing whitespace.
     Use the string methods we have learned in class to do this!
     Problem 3: 20 points possible
     """
     user_choice = user_choice.lower()
     user_choice = user_choice.strip()

     return user_choice

# You can test your function by running pytest -k test_clean_input in the terminal!


#_______________________________________________________________________________________________________________________

def validate_input(user_choice):
    """
    Users can be tricky! Let's make sure they enter a valid choice.
    We need to check:
     - The input is a string
     - The input is either "rock", "paper", or "scissors"
     - 
     Problem 4: 15 points possible
    """ 

    if type(user_choice) == str:
        is_string = True
        user_choice = clean_input(user_choice)
    else:
        is_string = False

    is_valid_choice = False
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        is_valid_choice = True

    if is_string and is_valid_choice:
        return True
    else:
        return False

# You can test your function by running pytest -k test_validate_input in the terminal!

#_______________________________________________________________________________________________________________________

def check_winner(user_choice, computer_choice):
     """
     Determines the winner based on user and computer choices.


     Problem 5: 25 points possible
     """
     
     result = " "
     is_input_valid = validate_input(user_choice)
     if is_input_valid == False:
         return "Invalid Input Try Again Next Time!"

     # User and Computer Tie
     if user_choice == computer_choice:
        result = "It's a tie!"
     # User win cases
     elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
     elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
     elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
     # Computer win cases
     else:
        result = "Better luck next time!"
    
     return result

# pytest -k test_check_winner

#_______________________________________________________________________________________________________________________

def start_game():
     # No need to modify this function!
     user_choice = get_user_choice()  # Get user choice
     computer_choice = get_computer_choice()  # Get computer choice 
     print("The computer chose:", computer_choice)
     print(check_winner(user_choice, computer_choice))  # Determine the winner
     return


# start_game() 

