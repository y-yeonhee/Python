"""
입력
첫째 줄에 케이크 수 a를 구성하는 자연수 a.x, a.y, a.z 가 차례대로 주어진다. (1 ≤ a.x, a.y, a.z ≤ 100)

둘째 줄에 케이크 수 c를 구성하는 자연수 c.x, c.y, c.z 가 차례대로 주어진다. (1 ≤ c.x, c.y, c.z ≤ 100)

출력
문제의 조건을 만족하는 b.x, b.y, b.z를 하나의 공백을 사이에 두고 차례대로 출력한다.

b는 1 ≤ b.x, b.y, b.z ≤ 100 이고 반드시 유일하게 존재한다.
"""

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx-az, int(cy/ay), cz-ax)
