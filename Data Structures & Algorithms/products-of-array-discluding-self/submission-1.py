class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        result = []
        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i!= j:
                    pdt*=nums[j]
            result.append(pdt)
        return result 
        """
        prefix=[1]*len(nums)
        sufix= [1]* len(nums)
        for i in range(1,len(nums)):
            prefix[i]= prefix[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            sufix[j]= sufix[j+1]*nums[j+1]
        return [prefix[i]*sufix [i] for i in range(len(nums))]
        



        