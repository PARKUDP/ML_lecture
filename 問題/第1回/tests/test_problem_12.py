import unittest
from problems import problem_12

class TestProblem12(unittest.TestCase):
    def test_solve(self):
        answer = problem_12.solve()
        # 正解は 12
        self.assertEqual(answer, 12)

if __name__ == '__main__':
    unittest.main()
