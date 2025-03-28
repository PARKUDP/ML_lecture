import unittest
from lesson_one.problems import problem_3

class TestProblem3(unittest.TestCase):
    def test_solve(self):
        answer = problem_3.solve()
        # テスト例：キーワードが含まれているか簡易チェック
        self.assertIn("従来", answer)
        self.assertIn("データ", answer)

if __name__ == '__main__':
    unittest.main()
