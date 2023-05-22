n=int(input())

for i in range(1,n+1):
    #각 자리수 map함수로 더하기
    hap=sum(map(int,str(i)))
    m=hap+i #분해합=각자릿수의 합+생성자
    if m==n:
        print(i)
        break
    if i==n: #생성자 i와 입력값이 같다는 건 생성자가 없다는 뜻
        print(0)

