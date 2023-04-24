'''
고려해야할 점
좌표범위 내의 값만 허용
방문한 길의 정방향 역방향을 고려하기 ->(0, 0)에서 (0,1)을 가는 것과 (0,1)에서 (0,0)을 가는 것은 똑같은 길

좌표에서 방문가능한 좌표로 이동한다면, 간선을 set에 저장해둔다.
(출발지점x, 출발지점y, 도착지점x, 도착지점y)
(도착지점x, 도착지점y, 출발지점x, 출발지점y)
겹치는 길이 있을 수 있으므로 set을 사용하고 len을 return 한다.
'''

def solution(dirs):
    answer = set()

    #이중배열 만들기
    grid = [[0 for y in range(11)] for x in range(11)]
    for i in range(11):
        for j in range(11):
            grid[i][j]=(i-5,j-5)

    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    #현재좌표       
    cur_x,cur_y=(0,0)
    #미래좌표
    next_x,next_y=(0,0)

    for d in dirs:
        next_x,next_y=cur_x+command[d][0],cur_y+command[d][1]
        if -5<=next_x<=5 and -5<=next_y<=5:
            answer.add((next_x,next_y,cur_x,cur_y))
            answer.add((cur_x,cur_y,next_x,next_y)) 
            cur_x,cur_y=next_x,next_y

    return len(answer)//2

print(solution("LULLLLLLU"))
