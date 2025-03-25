import unittest
from problems import problem_2

class TestProblem2(unittest.TestCase):
    def test_solve(self):
        answer = problem_2.solve()
        # 文字列に "経験" と "データ" が含まれていればOKとする
        self.assertIn("経験", answer)
        self.assertIn("データ", answer)

if __name__ == '__main__':
    unittest.main()
