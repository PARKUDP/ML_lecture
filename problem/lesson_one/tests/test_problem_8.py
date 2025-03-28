import unittest
from lesson_one.problems import problem_8

class TestProblem8(unittest.TestCase):
    def test_solve(self):
        answer = problem_8.solve()
        self.assertIn("試行錯誤", answer)
        self.assertIn("報酬", answer)

if __name__ == '__main__':
    unittest.main()
