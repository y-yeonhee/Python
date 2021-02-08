"""
문제
자연수 과 정수 가 주어졌을 때 이항 계수
를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력

를 출력한다.
"""
a, b = map(int, input().split())
eh = 1
for i in range(0, b):
    eh = eh * a
    a = a - 1
for j in range(2, b + 1):
    eh = eh // j
print(eh)
