# 종달새가 랜덤으로 노래해요

import random
time = random.randint(1, 24)    # 1시부터 24시까지 난수

print("좋은 아침입니다. 지금 시각은", str(time)+"시입니다.")

if time <= 5 or time >= 12:
    print("네?! 지금이 아침입니까??")

if time >= 6 and time <= 9:
    print("종달새가 노래를 부르네요!")
elif time >= 14 and time < 16:
    print("종달새는 노래를 부르네요!")
else:
    print("종달새가 지금은 노래를 안 부르고 싶다네요.")