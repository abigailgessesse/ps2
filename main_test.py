# DO NOT ALTER THIS FILE AT ALL!!!
import pytest
from unittest.mock import patch
from main import (
    get_user_choice,
    get_computer_choice,
    clean_input,
    validate_input,
    check_winner
)

# Group: get_user_choice
@patch('builtins.input', return_value='rock')
def test_get_user_choice(mock_input):
    assert get_user_choice() == 'rock'

@patch('builtins.input', return_value='rock')
def test_get_user_choice_rock(mock_input):
    assert get_user_choice() == 'rock'

# Group: get_computer_choice
@patch('random.randint', return_value=1)
def test_get_computer_choice_rock(mock_randint):
    assert get_computer_choice() == 'rock'

@patch('random.randint', return_value=2)
def test_get_computer_choice_paper(mock_randint):
    assert get_computer_choice() == 'paper'

@patch('random.randint', return_value=3)
def test_get_computer_choice_scissors(mock_randint):
    assert get_computer_choice() == 'scissors'

# Group: clean_input
def test_clean_input():
    assert clean_input('  Rock ') == 'rock'
    assert clean_input(' PAPER') == 'paper'
    assert clean_input('scissors ') == 'scissors'

def test_clean_input_rock():
    assert clean_input('  Rock ') == 'rock'

def test_clean_input_paper():
    assert clean_input(' PAPER') == 'paper'

def test_clean_input_scissors():
    assert clean_input('scissors ') == 'scissors'

# Group: validate_input
def test_validate_input():
    assert validate_input('rock') is True
    assert validate_input('paper') is True
    assert validate_input('scissors') is True
    assert validate_input('lizard') is False
    assert validate_input(123) is False

def test_validate_input_rock():
    assert validate_input('rock') is True

def test_validate_input_paper():
    assert validate_input('paper') is True

def test_validate_input_scissors():
    assert validate_input('scissors') is True

def test_validate_input_invalid():
    assert validate_input('lizard') is False

def test_validate_input_number():
    assert validate_input(123) is False

# Group: check_winner
def test_check_winner():
    assert check_winner('rock', 'scissors') == 'You win!'
    assert check_winner('scissors', 'rock') == 'Better luck next time!'
    assert check_winner('paper', 'rock') == 'You win!'
    assert check_winner('rock', 'rock') == "It's a tie!"
    assert check_winner('invalid', 'rock') == "Invalid Input Try Again Next Time!"

def test_check_winner_scissors_rock():
    assert check_winner('scissors', 'rock') == 'Better luck next time!'

def test_check_winner_paper_rock():
    assert check_winner('paper', 'rock') == 'You win!'

def test_check_winner_tie():
    assert check_winner('rock', 'rock') == "It's a tie!"

def test_check_winner_invalid():
    assert check_winner('invalid', 'rock') == "Invalid Input Try Again Next Time!"
