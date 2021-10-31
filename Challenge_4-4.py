# time 모듈로 작성한 코드에서 print() 요소들 쉼표로 나열하기

import time     # time 모듈. time() 함수는 1970.01.01부터 지금까지의 초를 반환함
now = time.time()
thisYear = int(1970 + now//(365*24*3600))

print("올해는", thisYear, "입니다.")
age = int(input("몇 살이신지요? "))
print("2050년에는", age+2050-thisYear, "살 이시군요.")