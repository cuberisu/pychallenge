# random 모듈을 활용한 주사위 게임

import random
print("주사위 게임!")
dice = random.randrange(6)+1    # randrange(6)하면 0~5 정수. 주사위 눈은 1부터 있으니까 +1
print(dice,"이(가) 나왔습니다!")