def solution(array, commands):
    answer = []
    
    for x in range(len(commands)):
        i,j,k=commands[x]
        div_arr=array[i-1:j]
        answer.append(sorted(div_arr)[k-1])

        
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))