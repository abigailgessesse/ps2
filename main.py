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
# TODO: YOUR NAME HERE: __________________________
#_______________________________________________________________________________________________________________________

def get_user_choice():
    """
    Ask the user for their move and save it! 
    Problem 1: 10 points possible
    """
    # TODO: Prompt the user to enter their choice.
    user_choice = None # Change None to be the user's input!

    return user_choice  # Return the user's choice (No need to modify this line)

# You can test your function by running pytest -k test_get_user_choice in the terminal!
# This test is a practice to get you started, so make sure it passes before you continue!


#_______________________________________________________________________________________________________________________

def get_computer_choice():
     """
     Generates a random choice for the computer.
     Problem 2: 15 points possible
     """
     
     # TODO: Generate a random number between 1 and 3 using the 'random' module.
     # Call this variable 'computer_choice'. This will be the computer's choice.
     # HINT: You might find this link to be helpful! https://www.w3schools.com/python/ref_random_randint.asp
     
     computer_choice = None  # Change None to be your random number!
     
     # TODO: Convert the number into rock (1), paper (2), or scissors (3) using if statements.
     # Set the computer_choice variable to the string value of the choice. 
     # HINT: Make sure to use the exact strings "rock", "paper", or "scissors".

     
     
     return computer_choice  # Return the computer's choice (No need to modify this line)

# You can test your function by running pytest -k test_get_computer_choice in the terminal!
# After each function you MUST make sure ALL your tests pass before you continue!

#_______________________________________________________________________________________________________________________

def clean_input(user_choice):
     """
     This function should clean the user's input to ensure it is lowercase and has no leading/trailing whitespace.
     Use the string methods we have learned in class to do this!
     Problem 3: 20 points possible
     """
     
     # TODO: Set user_choice to be a lowercase version of itself
     
     # TODO: Set user_choice to be itself, but with leading/trailing whitespace removed

     return None  # Return the cleaned user choice

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
    
    # TODO: Check if the user's input is a string, and set the variable to True if it is and False if not.
    # Clean the user's input using your clean_input function ONLY if the input is a string.
    is_string = None

    
    # TODO: Check if the user's input is either "rock", "paper", or "scissors", and set the variable to a boolean value.
    is_valid_choice = None
    

    
    # TODO: If the user's input is a string AND a valid choice, RETURN True. Otherwise, RETURN False.
    return None  # Return the result

# You can test your function by running pytest -k test_validate_input in the terminal!

#_______________________________________________________________________________________________________________________

def check_winner(user_choice, computer_choice):
     """
     Determines the winner based on user and computer choices.
     
     Don't worry about handling user errors here, we will have already checked for those.
     Problem 5: 25 points possible
     """
     
     result = None # Initialize the result variable

     # YOUR CODE HERE
     is_input_valid = validate_input(user_choice)  # No need to modify this line
     # TODO: if the user input is not valid, result should be "Invalid Input Try Again Next Time!."
  
     
     # TODO: Determine the winner by using if statements.
     
     # Here is an example of how to compare the user and computer choices
     if user_choice == "rock" and computer_choice == "scissors":
         result = "You win!"
         
     # TODO: If the user wins, your result should be "You win!"
     
     # TODO: If the computer wins, your result should be "Better luck next time!"
     
     # TODO: If the user and computer choices are the same, your result should be "It's a tie!"
    
     return result  # Return the result

# You can test your function by running pytest -k test_check_winner in the terminal!

# Now that you have completed all the functions, we can play the game! Run the main.py file to play the game!

#_______________________________________________________________________________________________________________________

def start_game():
     # No need to modify this function!
     user_choice = get_user_choice()  # Get user choice
     computer_choice = get_computer_choice()  # Get computer choice 
     print("The computer chose:", computer_choice)
     print(check_winner(user_choice, computer_choice))  # Determine the winner
     return

# Run uncomment the line below this and run python3 main.py in the terminal to play the game!
# start_game() 

# BE SURE TO COMMENT THE LINE ABOVE OUT BEFORE RUNNING YOUR TESTS AND SUBMITTING YOUR CODE!