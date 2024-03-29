import sys 

'''
- 0. 주어진 웅덩이의 좌표는 겹치지 않으므로 웅덩이의 시작 위치가 작은 순으로 오름차순 정렬한다.
- 1. 웅덩이를 하나씩 탐색하며 그 웅덩이를 커버할 수 있는 널판지의 개수를 센다.
- 2. 이때 이전 웅덩이에서 널판지를 걸쳤을 때 현재 탐색 중인 웅덩이까지 조금이라도 커버한다면 그 길이를 계산해주고 널판지를 추가한다. 
     만약 길이가 닿지 않는다면 해당 널판지의 위치를 현재 웅덩이의 시작 위치로 초기화한다.
- 3. 모든 웅덩이를 탐색한 뒤 총 사용한 널판지의 개수를 출력한다.
'''

sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt', "r")
n,l=map(int,input().split())
pool=[list(map(int,input().split()))for _ in range(n)]
pool.sort(key=lambda x:x[0])

