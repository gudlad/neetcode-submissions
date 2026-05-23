class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         ndict={}
         result=[]
         for num in nums:
            ndict[num]=ndict.get(num,0)+1
         freql = list(ndict.items())
         freql.sort(key=lambda x: x[1], reverse=True)
         topKl= freql[:k]  
         return [item[0] for item in topKl]
