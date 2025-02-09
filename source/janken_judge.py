# janken_judge.py
def judge(cpu_hand, user_hand):
    # 勝敗を判定する
    if cpu_hand == user_hand:
        return "引き分け"
    elif (cpu_hand == 'グー' and user_hand == 'チョキ') or \
         (cpu_hand == 'チョキ' and user_hand == 'パー') or \
         (cpu_hand == 'パー' and user_hand == 'グー'):
        return "コンピュータの勝ち"
    else:
        return "あなたの勝ち"