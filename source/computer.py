import random
# PCの手
P_hand = [1,2,3]

def cpu_pon():
    pc = P_hand[random.randint(0,2)]
    if pc == 1:
        print('CPUの手：グー')
        return pc
    elif pc == 2:
        print('PUの手：チョキ')
        return pc
    else:
        print('PUの手：パー')
        return pc