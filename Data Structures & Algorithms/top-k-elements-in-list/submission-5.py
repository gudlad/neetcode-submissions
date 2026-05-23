class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fdict={}
        for num in nums:
            fdict[num]=fdict.get(num,0)+1
        
        bucket= [[] for _ in range(len(nums)+1)]
        
        for num, count in fdict.items():
            bucket[count].append(num)
        
        result =[]
        for i in range(len(bucket)-1,0,-1):
            for value in bucket[i]:
                result.append(value)
                if len(result)==k:
                    return result
        

        