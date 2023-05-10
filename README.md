# 10Day-100DaysOfPythonGPT-Calculator
Day 10 of the [100 Days of Code with Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) from Udemy.

## What is 100DaysOfPythonGPT?

100 Days of Python is a Python Bootcamp from Udemy that provides 100 days of Python pratical content with lessons and projects. The GPT part is something I'm adding to the course and infers that I shall use ChatGPT's engine and/or API in some way on each and every one of those 100 projects. Furthermore, I shall also practice using PyTest to test these projects and applications at least in some level.

## TipCalculator

Tip Calculatos is the second project of the second Day of the bootcamp. Its purpose is to develop the ability to do math with Python and understand the logical order of operations.

The actual project consists of reading from the console a bill value, a tip percentage and the number of people spliting it. The result should be the expected payment of each person with two decimal points.

I tried using ChatGPT's API to create the tests with PyTest for the functionality, but it was a failure. The prompt I provided was followed properly (mostly, it seemed to sometimes forget the first line of imports) but it either dit not understand the code or is bad at math, because 3 out of every 5 tests created failed due to wrong math.

In the end I have a `test_gpt_tip_calculator.py` file that was created by ChatGPT and a `test_tip_calculator.py` that is the same code but with math corrected. The first one will fail 3 out of the 5 tests.

## Project Structure

 - [src/](src/) - The `tip_calculator.py` file holds the console interface (to be used by a user) and the actual function (to be tested) because GPT's tests wouldn't test it as an interface;
 - [test/](test/) - The `create_test_gpt.py` holds the script to generate a test for the functions above and `test_gpt_tip_calculator.py` file holds the tests created by the API (wich are wrong). The `test_tip_calculator.py` file holds the corrected tests.;
 - [include/](include/) - The `gpt.py` file holds the `get_completion` function that accesses the ChatGPT API. 
