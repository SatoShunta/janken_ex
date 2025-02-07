# ユーザの手
U_hand = -1

def user_pon():
    while(True):
        U_hand = int(input('1.グー 2.チョキ 3.パー\nグー、チョキ、パーのいずれかを入力してください＞'))
        if(U_hand == 1 or U_hand == 2 or U_hand == 3):
            if U_hand == 1:
                print(f'あなたの手：グー')
            elif U_hand == 2:
                print(f'あなたの手：チョキ')
            else:
                print(f'あなたの手：パー')
            return U_hand
            break
        else:
            print('1,2,3のどれかを入力してください')
