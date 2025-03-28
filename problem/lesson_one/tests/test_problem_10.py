import unittest
from lesson_one.problems import problem_10

class TestProblem10(unittest.TestCase):
    def test_solve(self):
        answer = problem_10.solve()
        self.assertIn("花", answer)
        self.assertIn("品種", answer)

if __name__ == '__main__':
    unittest.main()
