import unittest
from problems import problem_13

class TestProblem13(unittest.TestCase):
    def test_solve(self):
        answer = problem_13.solve()
        self.assertIn("間違ったルール", answer)
        self.assertIn("たくさん", answer)

if __name__ == '__main__':
    unittest.main()
