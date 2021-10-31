# 카페 이익 계산
# 총 재료 비용이 100000원이었다고 하자. 이익을 계산해보자. 적자인지 흑자인지를 표시해보자.

basic = int(input("아메리카노 판매 개수: "))
basicprice = 2000
milk = int(input("카페라떼 판매 개수: "))
milkprice = 3000
foam = int(input("카푸치노 판매 개수: "))
foamprice = 3500

sales = basic*basicprice
sales = sales + milk*milkprice
sales = sales + foam*foamprice
print("총 매출은", sales, "원 입니다.")

if sales > 100000:
    print("흑자입니다.")
else:
    print("적자입니다.")