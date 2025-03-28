import unittest
from lesson_one.problems import problem_6

class TestProblem6(unittest.TestCase):
    def test_solve(self):
        answer = problem_6.solve()
        # 正解は1
        self.assertEqual(answer, 1)

if __name__ == '__main__':
    unittest.main()
