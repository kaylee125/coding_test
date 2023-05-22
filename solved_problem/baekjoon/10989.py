'''카운팅정렬(계수정렬)
최대입력 크기 만큼의 배열을 만들고, 입력받는 숫자마다 해당 인덱스에 해당하는 값에+1씩 더해준다.
그 다음 다시 배열의 크기 만큼 반복문을 돌며 배열의 값이 0이 아닌 경우 배열의 값 만큼 반복하여 인덱스를 출력한다.
여기서 배열의 인덱스가 곧 입력받은 숫자다.
0부터 반복을 돌기 때문에 자동으로 정렬된 값 순서대로 출력된다.

카운팅정렬은 메모리를 절약할 수 있지만 시간이 오래 걸릴 수 있다는 단점이 있음.'''

import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(sys.stdin.readline())
arr=[0]*10001

for _ in range(n):
    num=int(sys.stdin.readline())
    arr[num]+=1

for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)
