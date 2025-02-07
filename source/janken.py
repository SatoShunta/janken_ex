import random
# ユーザの手
U_hand = -1
# PCの手
P_hand = [1,2,3]
win = 0
lose = 0
Tie = 0

for _ in range(3):
  print('1.グー 2.チョキ 3.パー\nグー、チョキ、パーのいずれかを入力してください＞')
  U_hand = int(input())
  print(f'あなたの手：{U_hand}')
  P_hand[random.randint(0,2)]
  if U_hand == 1:
      if P_hand == 1:
          print('引き分けです。')
          Tie += 1
      elif P_hand == 2:
          print('あなたの勝ちです。')
          win += 1
      else :
          print('CPUの勝ちです。')
          lose += 1
  elif U_hand == 2:
      if P_hand == 1:
          print('CPUの勝ちです。')
          lose += 1
      elif P_hand == 2:
          print('引き分けです。')
          Tie += 1
      else :
          print('あなたの勝ちです。')
          win += 1
  else:
      if P_hand == 1:
          print('あなたの勝ちです。')
          win += 1
      elif P_hand == 2:
          print('CPUの勝ちです。')
          lose += 1
      else :
          print('引き分けです。')
          Tie += 1
print("【最終結果】")
if win > lose:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの総合勝利です!")
elif win < lose:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nコンピューターの総合勝利です!")
else:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの引き分けです!")