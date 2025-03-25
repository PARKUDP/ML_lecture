import unittest
from problems import problem_9

class TestProblem9(unittest.TestCase):
    def test_solve(self):
        answer = problem_9.solve()
        self.assertIn("分類", answer)
        self.assertIn("回帰", answer)

if __name__ == '__main__':
    unittest.main()
