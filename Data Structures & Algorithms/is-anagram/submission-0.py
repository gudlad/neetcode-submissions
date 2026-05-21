from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # return False
        if Counter(s) == Counter(t):
            return True
        return False