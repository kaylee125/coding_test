from collections import *

class Solution(object):
    def groupAnagrams(self, word_list):
        word_dict=defaultdict(list)
        for word in word_list:
            sorted_word=''.join(sorted(word))
            word_dict[sorted_word].append(word)

        return sorted(word_dict.values() ,key=lambda x:len(x),reverse=False)

                    

solution=Solution()
                     
Input= ["a"]
res=solution.groupAnagrams(Input)
print(res)
