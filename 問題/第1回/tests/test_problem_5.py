import unittest
from problems import problem_5

class TestProblem5(unittest.TestCase):
    def test_solve(self):
        answer = problem_5.solve()
        # キーワードの簡易チェック
        self.assertIn("転ん", answer)
        self.assertIn("データ", answer)

if __name__ == '__main__':
    unittest.main()
