"""
문제
아래 예제 출력과 같은 J박스를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 박스의 크기가 주어진다. 박스의 크기는 10보다 작거나 같다.

출력
각 테스트 케이스에 대해서, 입력으로 주어지는 크기의 J박스를 출력한다. 박스와 박스 사이에는 빈 줄을 하나 출력한다.
"""
s_list=[]
T = int(input())
for i in range(0,T):
    s_list.append(int(input()))
for k in range(0,T):
    size = s_list[k]
    for j in range(0,size):
        if j==0 or j==size-1:
            print("#"*size)
        else:
            print("#"+'J'*(size-2)+"#")
    print("")