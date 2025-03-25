import unittest
from problems import problem_11

class TestProblem11(unittest.TestCase):
    def test_solve(self):
        answer = problem_11.solve()
        self.assertIn("分割", answer)
        self.assertIn("訓練データ", answer)
        self.assertIn("テストデータ", answer)

if __name__ == '__main__':
    unittest.main()
