class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best_streak = 0
        num_set =set(nums)
        for num in num_set:
            if num-1 not in num_set:
                cur_streak = 1
                while (num + cur_streak) in num_set:
                    cur_streak +=1
                best_streak = max(best_streak, cur_streak)
        return best_streak

