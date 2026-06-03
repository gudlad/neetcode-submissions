class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        slist=[]
        for char in s:
            if char.isalnum():
                slist.append(char.lower())
        return "".join(slist) == "".join(slist)[::-1]
        """

        left=0
        right=len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left+=1
            while left< right and not s[right].isalnum():
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True

        
        