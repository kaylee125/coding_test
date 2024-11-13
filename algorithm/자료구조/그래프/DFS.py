"""
DFS(깊이우선탐색)
- 구현방식
    - 재귀함수나 스택으로 구현
    - 한 경로를 끝까지 탐색한 후 다음 경로로 이동
- 특징
    - 전위순회(pre) ,중위순회(in) ,후위순회(post)와 같은 트리 순회방식이 dfs의 일종임
- 응용
    - 모든 노드를 방문해야할때 유용
    - 트리의 깊이나 경로를 찾는 문제에 적합
"""

#인접행렬
adj=[[0]*13 for _ in range(13)]
adj[0][1]=adj[0][7]=1
adj[1][2]=adj[1][5]=1

# for row in adj:
#     print(row)

def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)


dfs(0)