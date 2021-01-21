"""
문제
2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.



입력
첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다. 다음 n개 줄에는 점의 좌표 (xi, yi)가 주어진다. (-106 ≤ xi, yi ≤ 106)

출력
각 사분면과 축에 점이 몇 개 있는지를 예제 출력과 같은 형식으로 출력한다.
"""

list=[]
one=0
two=0
three=0
four=0
other=0
n = int(input())
for i in range(0,n):
    x,y = map(int, input().split())
    if x>0 and y>0:
        one = one+1
    elif x>0 and y<0:
        four = four+1
    elif x<0 and y>0:
        two = two+1
    elif x<0 and y<0:
        three = three+1
    else:
        other = other+1
print("Q1: %d" %one)
print("Q2: %d" %two)
print("Q3: %d" %three)
print("Q4: %d" %four)
print("AXIS: %d" %other)