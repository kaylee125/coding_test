sugar=int(input())
bags=0

while sugar>=0:
    if sugar%5==0: #5의 배수가 되면 몫만큼 봉지를 추가하고 반복문 종료
        bags+=sugar//5
        break
    sugar-=3 #1.설탕이 5의 배수가 될때까지 3키로 봉지에 설탕을 담는다.
    bags+=1
else:
    bags=-1

print(bags)
