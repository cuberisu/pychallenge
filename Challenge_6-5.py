# 5....? 초등생을 위한 덧셈뺄셈 문제 발생기
import random
while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sign = random.randint(1, 2)     # 연산자 결정

    if sign == 1:   # 덧셈 당첨
        print(num1, "+", num2, "=", end=" ")
        ans = input()  # 정답 입력시키기
        if ans == str(num1 + num2):     # 엔터키만 치면 ValueError나는 거 방지
            print("잘했어요!!")
        else:
            print("다음번에는 잘할 수 있죠?")
    
    elif sign == 2:   # 뺄셈 당첨
        if num1 >= num2:    # 정답이 양수로 나오게 하기
            print(num1, "-", num2, "=", end=" ")
            ans = input()
            if ans == str(num1 - num2):
                print("잘했어요!!")
            else:
                print("다음번에는 잘할 수 있죠?")      
        elif num1 < num2:    # 정답이 양수로 나오게 하기
            print(num2, "-", num1, "=", end=" ")
            ans = input()
            if ans == str(num2 - num1):
                print("잘했어요!!")
            else:
                print("다음번에는 잘할 수 있죠?")              