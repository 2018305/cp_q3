환율 = {"달러": 1320,
        "엔": 950,
        "위안": 182}
user = input("입력: ")
num, currency = user.split()
print("철수가 가지고 있는 돈의 원화 가치는", float(num) * 환율[currency], "원 입니다.")
