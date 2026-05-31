class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_=sorted(nums)
        curr_streak = 1
        best_streak = 1
        i = 0
        while i < len(nums_)-1:
            if nums_[i+1]-nums_[i]==1:
                curr_streak+=1
                best_streak = max(best_streak, curr_streak)
            elif nums_[i+1]-nums_[i]==0:
                i+=1
                continue
            else:
                best_streak = max(best_streak, curr_streak)
                curr_streak = 1
            i+=1
        return max(best_streak, curr_streak)

