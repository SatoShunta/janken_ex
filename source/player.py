# player.py
def pon():
    while True:
        user_input = input("じゃんけんの手を入力してください (1: グー, 2: チョキ, 3: パー): ")

        if user_input in ['1', '2', '3']:
            if user_input == '1':
                return 'グー'
            elif user_input == '2':
                return 'チョキ'
            elif user_input == '3':
                return 'パー'
        else:
            print("無効な入力です。1, 2, 3のいずれかを半角数字で入力してください。")