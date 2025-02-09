import sys
import os
sys.path.append(os.path.abspath('../source'))
import unittest
from janken_judge import judge

class TestJankenJudge(unittest.TestCase):

    def test_draw(self):
        # 引き分けのケース
        self.assertEqual(judge('グー', 'グー'), "引き分け")
        self.assertEqual(judge('チョキ', 'チョキ'), "引き分け")
        self.assertEqual(judge('パー', 'パー'), "引き分け")

    def test_cpu_win(self):
        # コンピュータの勝ち
        self.assertEqual(judge('グー', 'チョキ'), "コンピュータの勝ち")
        self.assertEqual(judge('チョキ', 'パー'), "コンピュータの勝ち")
        self.assertEqual(judge('パー', 'グー'), "コンピュータの勝ち")

    def test_user_win(self):
        # あなたの勝ち
        self.assertEqual(judge('チョキ', 'グー'), "あなたの勝ち")
        self.assertEqual(judge('パー', 'チョキ'), "あなたの勝ち")
        self.assertEqual(judge('グー', 'パー'), "あなたの勝ち")

if __name__ == "__main__":
    unittest.main()
