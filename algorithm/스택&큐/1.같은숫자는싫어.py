def solution(arr):
    stack=[arr[0]] #배열의 첫번째 값은 stack 첫번째 원소로 삽입

    for x in arr:
        # 만약 스택의 마지막 원소와 x의 값이 같다면
        # 스택에 값이 있어야하고, 스택의 마지막 원소가 x와 달라야함
        if x!=stack[-1]:
            stack.append(x)

    return stack

print(solution([1,1,3,3,0,1,1]))