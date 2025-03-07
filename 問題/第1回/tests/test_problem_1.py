from 第1回.problems.problem_1 import calculate_average

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([10, 20, 30, 40, 50]) == 30.0
    assert calculate_average([-5, 5, 10, 0]) == 2.5
    assert calculate_average([0, 0, 0, 0, 0]) == 0.0