# https://leetcode.com/problems/reverse-string/
#문자열 뒤집는 함수 작성

#1. 내가 푼 방법
def reverseString_me(list):
    res=[]
    for s in list[::-1]:
        res.append(s)
    return res
#2.투 포인터를 이용한 스왑->두개의 포인터를 지정하고 범위를 좁혀가며 스왑하기
def reverseString_Twopointer(list):
    left,right=0,len(list)-1
    while left<right:
        list[left],list[right]=list[right],list[left]
        left+=1
        right-=1
    return list
#3.파이써닉한 코드
def reverseString(list):
    list.reverse()
    return list


print(reverseString_me(["h","e","l","l","o"]))
print(reverseString_Twopointer(["h","e","l","l","o"]))
print(reverseString(["h","e","l","l","o"]))

