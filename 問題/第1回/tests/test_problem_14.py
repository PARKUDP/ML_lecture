import unittest
from problems import problem_14

class TestProblem14(unittest.TestCase):
    def test_solve(self):
        answer = problem_14.solve()
        # キーワードの簡易チェック
        self.assertIn("写真", answer)
        self.assertIn("ラベル", answer)
        self.assertIn("フィードバック", answer)

if __name__ == '__main__':
    unittest.main()
