'''
topdown방식 
'''
 
import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 8/'
sys.stdin=open(base+'7, 8. 알리바바와 40인의 도둑/in1.txt', "r")


def DFS(x,y):
    if x==0 and y==0:
        return a[0][0]

    else:
        
        

if __name__=='__main__':
    n=int(input())
    a=[]
    for _ in range(n):
        a.append(list(map(int,input().split())))
    print(DFS(n-1,n-1))