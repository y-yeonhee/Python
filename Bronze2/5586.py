"""
문제
입력으로 주어지는 문자열에서 연속으로 3개의 문자가 JOI 또는 IOI인 곳이 각각 몇 개 있는지 구하는 프로그램을 작성하시오. 문자열은 알파벳 대문자로만 이루어져 있다. 예를 들어, 아래와 같이 "JOIOIOI"에는 JOI가 1개, IOI가 2개 있다.



입력
첫째 줄에 알파벳 10000자 이내의 문자열이 주어진다.

출력
첫째 줄에 문자열에 포함되어 있는 JOI의 개수, 둘째 줄에 IOI의 개수를 출력한다.
"""


line = input()
count1 = 0
count2 = 0
size = len(line)
for i in range(0,size-2):
    if line[i]=="J" and line[i+1]=="O" and line[i+2]=="I":
        count1 = count1+1
    if line[i]=="I" and line[i+1]=="O" and line[i+2]=="I":
        count2 = count2+1
print(count1)
print(count2)