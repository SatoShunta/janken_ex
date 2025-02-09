# computer.py
import random

def pon():
    # 1から3のランダムな数字を生成
    computer_choice = random.choice([1, 2, 3])

    # 生成された数字に対応するじゃんけんの手を返す
    if computer_choice == 1:
        return 'グー'
    elif computer_choice == 2:
        return 'チョキ'
    elif computer_choice == 3:
        return 'パー'