import player
import computer
import janken_judge
# ユーザの手
U_hand = -1
# PCの手
P_hand = -1
win = 0
lose = 0
Tie = 0

for _ in range(3):
    U_hand = player.user_pon()
    P_hand = computer.cpu_pon()
    judge = janken_judge.judge(U_hand,P_hand)
    if judge == 'win':
        win += 1
    elif judge == 'lose':
        lose += 1
    elif judge == 'Tie':
        Tie += 1

print("【最終結果】")
if win > lose:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの総合勝利です!")
elif win < lose:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nコンピューターの総合勝利です!")
else:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの引き分けです!")
    