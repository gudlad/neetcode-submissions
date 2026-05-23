import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # 1. approach
         # ndict={}
         # result=[]
         # for num in nums:
         #    ndict[num]=ndict.get(num,0)+1
         # freql = list(ndict.items())
         # freql.sort(key=lambda x: x[1], reverse=True)
         # topKl= freql[:k]  
         # return [item[0] for item in topKl]

         # 2. using max heap
          result=[]
          ndict={}
          for num in nums:
            ndict[num]=ndict.get(num,0)+1
          max_h = [(-freq,num) for num, freq in ndict.items()]
          heapq.heapify(max_h)
          for _ in range(k):
            freq, num = heapq.heappop(max_h)
            result.append(num)
          return result
         




         # 3. using bucket sort


