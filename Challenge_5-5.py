# 로그인
id = "ilovepython"
pw = "123456"
s = input("아이디를 입력하세요.: ")
if s == id:
    p = input("비밀번호를 입력하세요.: ")
    if p == pw:
        print("환영합니다.")
        print("보안에 취약한 비밀번호를 사용하고 있습니다.")
        print("비밀번호 변경 페이지로 이동하시기 바랍니다.")
    else: 
        print("비밀번호가 맞지 않습니다.")
else:
    print("등록되지 않은 사용자입니다.")
    