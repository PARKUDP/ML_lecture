import unittest
from problems import problem_1

class TestProblem1(unittest.TestCase):
    def test_solve(self):
        answer = problem_1.solve()
        # テスト例：回答の中に「データを見て」「ルールを学ぶ」などのキーワードが含まれるか簡易チェック
        self.assertIn("データ", answer)
        self.assertIn("ルール", answer)

if __name__ == '__main__':
    unittest.main()