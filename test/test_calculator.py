import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

from src import calculator

def test_add():
    operator = "+"

    assert calculator.operations[operator](2, 3) == 5
    assert calculator.operations[operator](20, 30) == 50
    assert calculator.operations[operator](2, -3) == -1
    assert calculator.operations[operator](3, -3) == 0

def test_sub():
    operator = "-"

    assert calculator.operations[operator](4, 3) == 1
    assert calculator.operations[operator](20, 30) == -10
    assert calculator.operations[operator](2, -3) == 5
    assert calculator.operations[operator](3, -3) == 6

def test_multiply():
    operator = "*"

    assert calculator.operations[operator](2, 3) == 6
    assert calculator.operations[operator](20, 30) == 600
    assert calculator.operations[operator](2, -3) == -6
    assert calculator.operations[operator](3, -3) == -9

def test_divide():
    operator = "/"

    assert calculator.operations[operator](3, 2) == 1.5
    assert calculator.operations[operator](30, 15) == 2
    assert calculator.operations[operator](-4, 2) == -2
    assert calculator.operations[operator](3, -3) == -1