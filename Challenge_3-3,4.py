# 자판기 거스름돈 & 주석

money = int(input("투입한 돈: "))   # 변수 money에 투입한 금액을 정수형으로 입력받기
price = int(input("물건 값: "))     # 변수 price에 물건값을 정수형으로 입력받기

change = money - price  # 총 거스름돈
print("거스름돈:", change)

coin500s = change//500  # 500원 개수
change %= 500   # change//동전금액 의 나머지가 남은 거스름돈
coin100s = change//100  # 100원 개수
change %= 100
coin50s = change//50    # 50원 개수
change %= 50
coin10s = change//10    # 10원 개수
change %= 10

print("500원 동전 개수:", coin500s) # 거스름돈에 포함된 각 동전들의 개수를 출력
print("100원 동전 개수:", coin100s)
print("50원 동전 개수:", coin50s)
print("10원 동전 개수:", coin10s)