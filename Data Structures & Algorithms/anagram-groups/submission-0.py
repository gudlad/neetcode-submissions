class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ndict = {}
        for i in strs:
        	ndict[''.join(sorted(i))]=[]
        for i in strs:
            if ''.join(sorted(i)) in ndict.keys():
                	ndict[''.join(sorted(i))].append(i)
        result = []
        for i in ndict.values():
            temp = []
            for j in i:
                temp.append(j)
            result.append(temp)
        return result
        

