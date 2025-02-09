import sys
import os
sys.path.append(os.path.abspath('../source'))
import unittest
from unittest.mock import patch
from janken import janken_main

class TestJanken(unittest.TestCase):

    @patch('player.pon')
    @patch('computer.pon')
    @patch('janken_judge.judge')
    def test_janken_main(self, mock_judge, mock_cpu_pon, mock_human_pon):
        # モックの設定: プレイヤーとコンピュータの手を固定
        mock_human_pon.return_value = 'グー'  # ユーザーの手
        mock_cpu_pon.return_value = 'チョキ'  # コンピュータの手
        mock_judge.return_value = 'あなたの勝ち'  # 勝者を固定

        # janken_mainのテスト
        with patch('builtins.print') as mock_print:
            janken_main()  # ゲーム実行

            # printの呼び出しを確認して、結果が期待通りかチェック
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
        # モックの設定: プレイヤーとコンピュータの手を引き分けに設定
        mock_human_pon.return_value = 'グー'  # ユーザーの手
        mock_cpu_pon.return_value = 'グー'  # コンピュータの手
        mock_judge.return_value = '引き分け'  # 勝者を引き分けに設定

        # janken_mainのテスト（引き分け結果）
        with patch('builtins.print') as mock_print:
            janken_main()  # ゲーム実行

            # printの呼び出しを確認して、結果が期待通りかチェック
            mock_print.assert_any_call('あなたの手: グー, コンピュータの手: グー')
            mock_print.assert_any_call('結果: 引き分け')
            mock_print.assert_any_call('最終結果:')
            mock_print.assert_any_call('あなたの勝ち数: 0')
            mock_print.assert_any_call('コンピュータの勝ち数: 0')
            mock_print.assert_any_call('総合引き分け！')

if __name__ == "__main__":
    unittest.main()
