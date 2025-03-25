import unittest
from problems import problem_4

class TestProblem4(unittest.TestCase):
    def test_solve(self):
        answer = problem_4.solve()
        # 活用例のキーワードが含まれているかチェック
        self.assertIn("顔認識", answer)
        self.assertIn("YouTube", answer)
        self.assertIn("自動翻訳", answer)
        self.assertIn("自動運転", answer)

if __name__ == '__main__':
    unittest.main()
