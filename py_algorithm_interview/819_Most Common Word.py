#https://leetcode.com/problems/most-common-word/
'''
정규표현식
딕셔너리 모듈(collections)
-1.dafaultdict(int):디폴트값인 0을 기준으로 존재하지 않는 키를 조회할 경우에도 딕셔너리 아이템 생성
-2.Counter(dict):아이템에 대한 개수를 계산해서 딕셔너리로 리턴
'''
from collections import Counter
import collections
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph_list=[word.lower() for word in re.sub(r'[^\w]',' ',paragraph).split() if re.sub(r'[^\w]','',word).lower()  not in banned]

        # paragraph_list=[word for word in paragraph.split().remove(',') if word not in banned]
        
        counts=Counter(paragraph_list)
        print(paragraph_list)

        max_val=0
        max_word=''
        for word,count in counts.items():
            if word=='':
                pass
            
            if count>max_val:
                max_val=count
                max_word=word
                print(max_word)

        return max_word
    
    def mostCommonWord_book_ver(self, paragraph, banned):
        paragraph_list=[word.lower() for word in re.sub(r'[^\w]',' ',paragraph).split() if re.sub(r'[^\w]','',word).lower()  not in banned]
        #정규식으로 문자열 변환->문자열 lower()->split()으로 텍스트별로 분리된 리스트 생성
        words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        counts=collections.defaultdict(int)
        print(counts)
        #키 존재 유무 확인 필요 없이 바로 카운트 가능
        for word in words:
            counts[word]+=1
        return max(counts,key=counts.get)
            
        return max_word
solution=Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
result=solution.mostCommonWord_book_ver(paragraph,banned)
print(result)