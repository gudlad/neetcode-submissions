class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ndict={}
        # for word in strs:
        #     key=''.join(sorted(word))
        #     if key not in ndict:
        #         ndict[key]=[]
        #     ndict[key].append(word)
        # return list(ndict.values())
        ndict={}
        for word in strs:
            freql=[0]*26
            for char in word:
                freql[ord(char)-ord('a')]+=1
            # list not hashable so conver to tuple to use as a key in dict
            key= tuple(freql)
            if key not in ndict:
                ndict[key]=[]
            ndict[key].append(word)
        return list(ndict.values())

