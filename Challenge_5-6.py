# 골키퍼

import random

options = ["좌측 상단", "좌측 하단", "중앙", "우측 상단", "우측 하단"]
computer_choice = random.choice(options)    
# choice(list)는 list 요소 중 하나를 랜덤으로 택하는 함수
user_choice = input("어디를 수비하시겠어요? (좌측 상단, 좌측 하단, 중앙, 우측 상단, 우측 하단) ")

print("슛은", computer_choice+"으로 날아갔습니다.")
if computer_choice == user_choice:
    print("수비에 성공했습니다.")
else:
    print("패널티 킥이 성공했습니다.")