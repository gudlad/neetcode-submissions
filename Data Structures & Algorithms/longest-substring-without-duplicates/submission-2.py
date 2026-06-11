class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxL = 0
        for i in range(len(s)):
            charDict = {}
            for j in range(i, len(s)):
                if s[j] in charDict:
                    break
                length = j-i+1
                maxL = max(maxL,length)
                charDict[s[j]]=j
        return maxL

