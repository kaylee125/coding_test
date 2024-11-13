"""
가장 많이 팔린책
책 별로 카운트
갯수가 동일할 경우 알파벳 순서대로
"""

N=int(input())

books={}
for  _ in range(N):
    book=input()
    if book in books:
        books[book]+=1
    else:
        books[book]=1

sort_lst=sorted(books.items(),key=lambda x:(-x[1],x[0]))
print(sort_lst[0][0])