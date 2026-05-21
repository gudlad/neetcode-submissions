class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        numdic=dict()
        for i in nums:
            numdic[i]=numdic.get(i,0)+1
        for j in numdic.values():
            if j>=2:
                return True
        return False

            
        