from 第1回.problems.problem_2 import is_even

def test_is_even():
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(10) == True
    assert is_even(7) == False