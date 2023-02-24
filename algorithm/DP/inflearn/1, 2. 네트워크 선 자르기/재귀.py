import sys
input = sys.stdin.readline

#DFS(7)=7미터 길이의 선을 자르는 경우의 수
def DFS(len):
    if line[len]>0: #리스트에 값이 있다면, 이미재귀호출된 것이고 중복 재귀호출 방지를 위해 리스트값에 있던 값을 반환해줌
        return line[len]

    if len==1 or len==2:
        return len

    else:
        line[len]=DFS(len-1)+DFS(len-2)
        print(line[len])
        return line[len]

if __name__== "__main__":
    n=int(input())
    line=[0]*(n+1)
    print(DFS(n))