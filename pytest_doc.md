# Pytest

Pytest is a very helpful tool to have as a programmer, but especially so in this class. All of your problem sets will be graded on your Pytest results, so lets take a look on how we get this set up and working!


# Setup

First thing first is making sure you install it by running this command in the terminal
```
pip3 install pytest
```

You can test if you have it by running 

```
pytest --version
```
## Running the Basic Command

Navigate to the folder that holds the tests. If there is a "No Tests Run" error, it is likley that the folder you are in is not where the tests are.

For the command itself there are a few options, but to run all tests in that folder, run
```
pytest
```

You should expect your output to look something like this

```
**____________________________ test_check_winner_tie _____________________________**

  

def test_check_winner_tie():

> assert check_winner('rock', 'rock') == "It's a tie!"

**E assert None == "It's a tie!"**

**E  +  where None = check_winner('rock', 'rock')**

  

**main_test.py**:87: AssertionError

**__________________________ test_check_winner_invalid ___________________________**

  

def test_check_winner_invalid():

> assert check_winner('invalid', 'rock') == "Invalid Input Try Again Next Time!"

**E AssertionError: assert None == 'Invalid Input Try Again Next Time!'**

**E  +  where None = check_winner('invalid', 'rock')**

  

**main_test.py**:90: AssertionError
**=========================== short test summary info ============================**
FAILED main_test.py::**test_check_winner_scissors_rock** - AssertionError: assert None == 'Better luck next time!'

FAILED main_test.py::**test_check_winner_paper_rock** - AssertionError: assert None == 'You win!'

FAILED main_test.py::**test_check_winner_tie** - assert None == "It's a tie!"

FAILED main_test.py::**test_check_winner_invalid** - AssertionError: assert None == 'Invalid Input Try Again Next Time!'

============================== **20 failed** in 0.18s ==============================
```

There will be more above, or if you have some tests passing that is great news as well!

Everytime you want to run this, make sure you have saved your work first!



## Selecting Specific Tests

This is a lot to look at! Sometimes only looking at a group of tests can be helpful for figuring out what is wrong.

By writing

```
pytest -k get_user_choice
```
We are able to just select the tests that are in that group. You can find the names of these groups by reading through the comments of the code.

```
**============================= test session starts ==============================**

platform darwin -- Python 3.11.5, pytest-8.3.4, pluggy-1.5.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

cachedir: .pytest_cache

rootdir: /Users/name/Desktop/Local Git/ps2

configfile: pytest.ini

**collected 20 items / 18 deselected / 2 selected**

  

main_test.py::test_get_user_choice PASSED  [ 50%]

main_test.py::test_get_user_choice_rock PASSED [100%]

  

======================= **2 passed**, 18 deselected in 0.03s =======================
```

## How to Know if you are Done?

After you have worked through all the problems, run
```
pytest
```

with **no selectors**

If you have no tests deselected, and it says

```
======================= **20 passed** =======================
```

(may not be 20 depending on the problem set)

This means your code is correct!

## Trouble Shooting

### Tests run but are failing
If your tests are failing, take at look at each error individually.

Here is the short error message.
```
FAILED main_test.py::**test_check_winner_paper_rock** - AssertionError: assert None == 'You win!'
```
You can see the test name is test_check_winner_paper_rock, and that the output provided was None, when 'You win!' was expected.

Let's take a look at the expanded test you would find above
```
**_________________________ test_check_winner_paper_rock _________________________**

  

def test_check_winner_paper_rock():

> assert check_winner('paper', 'rock') == 'You win!'

**E AssertionError: assert None == 'You win!'**

**E  +  where None = check_winner('paper', 'rock')**

  

**main_test.py**:84: AssertionError
```
With this, you can see that the test was running the check_winner() function, and the paramaters are paper and rock. 

Since paper should beat rock, the player **Should** be getting a win message, but right now, it is getting a different response. Use this information to figure out what to fix!

### Test is giving an error
If you are getting an error,
```
**=========================== short test summary info ============================**

ERROR main_test.py

!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!

=============================== **1 error** in 0.10s ===============================
```
This means your logic is not the problem, but that something is incorrect in your syntax. If this prevents your tests from running, **YOU MUST FIX IT!** It does not matter if your tests would be passing if you were not running the erroring test, you will still not get credit for any of them.

To fix this, start by reading from the bottom up and looking for a line number in the file you are writing in.
```
E File "/Users/user/Desktop/Local Git/ps2/main.py", line 26

E {

E IndentationError: unexpected indent
```
This tells me to look at line 26 in the file ```main.py``` for a ```{``` that is not supposed to be there.
### Tests will not run/ pytest is not found
If pytest is not found, then try running each of these commands and see if it fixes things.

##### Try to re install and run again
```pip3 install pytest```
then
```pytest``

##### Try to run it with more manually

```python3 -m pytest ```

If this does not work go and speak with a TA or Professor!

## Notes on Grading

- The code that you submit will be exactly what is run. 
- Do not change the grading file, it will be changed back.
- If your code does not run, we will not fix it for you!! 
