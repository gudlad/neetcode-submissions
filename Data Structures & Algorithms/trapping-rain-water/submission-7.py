class Solution:
    def trap(self, height: List[int]) -> int:  
        leftMax, rightMax = 0,0
        total = 0
        left,right = 0, len(height)-1
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                total += leftMax - height[left]
                left+=1
            else:
                total+= rightMax - height[right]
                right-=1
        return total
                                             