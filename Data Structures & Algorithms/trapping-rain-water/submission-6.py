class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suffixmax = [0]*n
        suffixmax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffixmax[i] = max(suffixmax[i+1], height[i])
        prefix = height[0]
        total = 0
        for i in range(1, n-1):
            prefix = max(prefix, height[i])
            total += min(prefix, suffixmax[i]) - height[i]
        return total




        
        