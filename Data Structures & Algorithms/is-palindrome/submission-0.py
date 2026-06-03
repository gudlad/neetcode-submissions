class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist=[]
        for char in s:
            if char.isalnum():
                slist.append(char.lower())
        return "".join(slist) == "".join(slist)[::-1]
        