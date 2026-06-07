class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixmax = [0]*n
        prefixmax[0]= height[0]
        for i in range(1,n):
            prefixmax[i]= max(prefixmax[i-1], height[i])


        suffixsum = [0]*n
        suffixsum[n-1]= height[n-1]
        for i in range(n-2,-1,-1): 
            suffixsum[i] = max(suffixsum[i+1], height[i])

        total = 0
        for i in range(1, len(height)-1):
            total += min(prefixmax[i],suffixsum[i]) - height[i]
        return total

