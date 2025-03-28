import unittest
from lesson_one.problems import problem_7

class TestProblem7(unittest.TestCase):
    def test_solve(self):
        answer = problem_7.solve()
        # 正解は3
        self.assertEqual(answer, 3)

if __name__ == '__main__':
    unittest.main()
