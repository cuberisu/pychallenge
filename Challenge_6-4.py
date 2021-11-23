# 4 구구단
for i in range(1, 10): # 1~9단 
    print(i, "단")
    for j in range(1, 10):  # 1~9
        print(i*j, end=" ")     # 곱한 값 출력 후 띄어쓰기
    print("")   # 1cycle 끝나면 줄 개행