"""
문제
당신은 어떤 물건이라도 20% 할인해주는 쿠폰을 가지고 있다.

원래 가격이 주어질 때, 쿠폰을 사용하면 얼마가 되는지 알려주는 프로그램을 작성하시오.

입력
첫 번째 줄에 테스트케이스의 수가 주어진다.

각 줄에는 물건의 원래가격이 소수점 둘째자리까지 주어진다.

출력
할인된 가격을 달러 단위로 출력한다.

나누어떨어지지 않을 때는 소수점 셋째 자리에서 반올림해서 둘째 자리까지 출력한다.
"""

price = []
result = []
case = int(input())
for i in range(0,case):
    temp = float(input())
    price.append(temp)
for i in range(0,case):
    result.append(price[i] * 0.8)
for i in range(0, case):
    print('$%.2f' %result[i])



