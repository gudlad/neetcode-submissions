class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ndict={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in ndict:
                ndict[key]=[]
            ndict[key].append(word)
        return list(ndict.values())