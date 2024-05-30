
"""
문제설명:최대공약수와 최소공배수 구하기
핵심내용: 최소공배수는 두수의 곱/최대공약수
        최대공약수 구하는 방법 아래 로직 외에 유클리드 호제법 많이 사용함
"""
a,b =map(int,input().split())
a_list=[x for x in range(1,a+1) if a%x==0]
b_list=[x for x in range(1,a+1) if b%x==0]

# 최대공약수
max_val=0
for i in range(len(a_list)):
    if a_list[i] in b_list:
        max_val=a_list[i]
    else:
        pass

min_val=(a*b)/max_val
print(max_val)
print(int(min_val))
