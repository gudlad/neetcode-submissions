from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # if Counter(s) == Counter(t):
        #     return True
        # return False
        if len(s) != len(t):
            return False
        dictn=dict()
        for char in s:
            dictn[char]=dictn.get(char,0)+1
        for char in t:
            if char not in dictn:
                return False
            dictn[char]-=1
            if dictn[char] < 0:
                return False
        return True
        

