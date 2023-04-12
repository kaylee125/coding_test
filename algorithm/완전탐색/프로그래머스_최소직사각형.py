# 모든 명함들의 긴 모서리를 가로로 돌려서 겹쳐봅시다.
# 그 상태에서 지갑에 한번에 넣을 수 있으려면 세로길이는 어떻게 해야할지 상상해봅시다!
def solution(sizes):
    largest_x=0
    largest_y=0

    #긴 애를 가로 사이즈로 스위치 시키기
    for x in sizes:
        if x[1]>x[0]:
            x[0],x[1]=x[1],x[0]
        #가장 긴 가로
        if x[0] >largest_x:
            largest_x=x[0]
        #가장 긴 세로    
        if x[1]>largest_y:
            largest_y=x[1]

    answer=largest_x*largest_y #긴 애들 중에서 제일 긴 애 X 짧은 애들 중에서 제일 긴 애
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))