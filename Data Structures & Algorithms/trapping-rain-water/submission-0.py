class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        for i in range(1,len(height)-1):
            max_left = max(height[0:i])
            max_right = max(height[i+1:])
            total += max(0, min(max_left, max_right)-height[i])
        return total

        