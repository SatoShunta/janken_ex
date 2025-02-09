import sys
import os
sys.path.append(os.path.abspath('../source'))  # sourceフォルダを検索パスに追加

import unittest
from computer import pon

class TestPonFunction(unittest.TestCase):
    def test_pon_output(self):
        possible_outputs = {'グー', 'チョキ', 'パー'}
        
        # 何度か実行して全てのパターンが含まれるか確認
        for _ in range(100):
            self.assertIn(pon(), possible_outputs)

if __name__ == "__main__":
    unittest.main()
