import sys
import os

sys.path.append(os.path.abspath('../source'))

import unittest
from unittest.mock import patch
from source.janken import janken_main


class TestJanken(unittest.TestCase):

    @patch('player.pon')
    @patch('computer.pon')
    @patch('janken_judge.judge')
    def test_janken_main(self, mock_judge, mock_cpu_pon, mock_human_pon):
        mock_human_pon.return_value = 'グー'
        mock_cpu_pon.return_value = 'チョキ'
        mock_judge.return_value = 'あなたの勝ち'

        with patch('builtins.print') as mock_print:
            janken_main()

            mock_print.assert_any_call('あなたの手: グー, コンピュータの手: チョキ')
            mock_print.assert_any_call('結果: あなたの勝ち')
            mock_print.assert_any_call('最終結果:')
            mock_print.assert_any_call('あなたの勝ち数: 3')
            mock_print.assert_any_call('コンピュータの勝ち数: 0')
            mock_print.assert_any_call('あなたの総合勝利！')

    @patch('player.pon')
    @patch('computer.pon')
    @patch('janken_judge.judge')
    def test_janken_main_draw(self, mock_judge, mock_cpu_pon, mock_human_pon):
        mock_human_pon.return_value = 'グー'
        mock_cpu_pon.return_value = 'グー'
        mock_judge.return_value = '引き分け'

        with patch('builtins.print') as mock_print:
            janken_main()

            mock_print.assert_any_call('あなたの手: グー, コンピュータの手: グー')
            mock_print.assert_any_call('結果: 引き分け')
            mock_print.assert_any_call('最終結果:')
            mock_print.assert_any_call('あなたの勝ち数: 0')
            mock_print.assert_any_call('コンピュータの勝ち数: 0')
            mock_print.assert_any_call('総合引き分け！')

if __name__ == "__main__":
    unittest.main()
