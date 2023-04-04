#https://leetcode.com/problems/valid-palindrome/
#주어진 문자열이 팰린드롬인지 확인해라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.
import collections
import re


class Solution:
    '''
    (self, s: str) -> bool: 
        ==>클래스 내부의 메소드를 정의할 때 사용되는 메소드 선언 방식 중 하나
    - self는 인스턴스 자신을 참조하는데 사용되는 첫 번째 매개변수
    - s: str은 두 번째 매개변수, s는 문자열(string) 자료형을 가리킵니다. 
         이 매개변수는 함수나 메소드가 받는 인자의 데이터 타입을 명시하는 것이며, 이를 통해 함수나 메소드 내부에서 해당 인자에 대한 검사나 처리를 보다 쉽게 할 수 있습니다.
    - -> bool은 함수나 메소드의 반환 값의 데이터 타입을 명시, 이 경우에는 불리언(Boolean) 자료형을 반환한다는 것을 나타냅니다.

    '''
    def isPalindrome_list(self, s) :
        strs=[]
        for char in s:
            if char.isalnum(): #isalnum():영문자,숫자여부 판별 함수
                strs.append(char.lower())
        while len(strs)>1:
            if strs.pop(0)!=strs.pop(): #pop(0):시간복잡도 O(n)으로 높은 편
                return False
        return True
    
    #데크 자료형을 이용한 최적화
    def isPalindrome_deque(self, s: str) -> bool:
        strs=collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs)>1:
            if strs.popleft() != strs.pop(): # popleft -> 시간복잡도 O(1) /n번 수행시 O(n)
                return False
        return True
    
    #슬라이싱 사용
    def isPalindrome_slicing(self,s:str) ->bool:
        s=s.lower()
        #정규식으로 불필요한 문자 필터링()
        # 문자열 s에서 알파벳 소문자(a-z)와 숫자(0-9)를 제외한 모든 문자를 제거
        # ^은 negative을 나타내며, [^(a-z0-9)]는 알파벳 소문자와 숫자를 제외한 문자에 매치됨
        s=re.sub('[^a-z0-9]','',s)
        return s==s[::-1]
    

solution = Solution() #클래스 객체 셍성
test_case = "A man, a plan, a canal: Panama"
result = solution.isPalindrome_slicing(test_case) #클래스 객체 내 함수 호출
print(result) # 결과 : True 