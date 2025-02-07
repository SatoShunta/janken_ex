win = 0
lose = 0
Tie = 0
 
def judge(U_hand,P_hand):
    if U_hand == 1:
        if P_hand == 1:
            print('引き分けです。')
            return 'Tie'
        elif P_hand == 2:
            print('あなたの勝ちです。')
            return 'win'
        else :
            print('CPUの勝ちです。')
            return 'lose'
    elif U_hand == 2:
        if P_hand == 1:
            print('CPUの勝ちです。')
            return 'lose'
        elif P_hand == 2:
            print('引き分けです。')
            return 'Tie'
        else :
            print('あなたの勝ちです。')
            return 'win'
    else:
        if P_hand == 1:
            print('あなたの勝ちです。')
            return 'win'
        elif P_hand == 2:
            print('CPUの勝ちです。')
            return 'lose'
        else :
            print('引き分けです。')
            return 'Tie'

