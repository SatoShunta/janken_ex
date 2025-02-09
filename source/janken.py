# janken.py
from player import pon as human_pon
from computer import pon as cpu_pon
from janken_judge import judge

def janken_main():
    user_wins = 0
    cpu_wins = 0

    for _ in range(3):
        user_hand = human_pon()
        cpu_hand = cpu_pon()

        print(f"あなたの手: {user_hand}, コンピュータの手: {cpu_hand}")

        result = judge(cpu_hand, user_hand)
        print(f"結果: {result}")

        if result == "あなたの勝ち":
            user_wins += 1
        elif result == "コンピュータの勝ち":
            cpu_wins += 1

    print("\n最終結果:")
    print(f"あなたの勝ち数: {user_wins}")
    print(f"コンピュータの勝ち数: {cpu_wins}")

    if user_wins > cpu_wins:
        print("あなたの総合勝利！")
    elif cpu_wins > user_wins:
        print("コンピュータの総合勝利！")
    else:
        print("総合引き分け！")

if __name__ == "__main__":
    janken_main()