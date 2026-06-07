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

"""
max_left = max(height[0:i])   # excludes height[i]
max_right = max(height[i+1:]) # excludes height[i]
So if height[i] was a tall middle bar, max_left and max_right could be smaller than height[i] → negative!
But in prefix/suffix:
pythonprefix[i] = max(prefix[i-1], height[i])  # INCLUDES height[i]
suffix[i] = max(suffix[i+1], height[i])  # INCLUDES height[i]
Current element is always included so minimum is always >= height[i]. That's the key difference!
Submit and then let's do two pointers!Sonnet 4.6 Low
"""