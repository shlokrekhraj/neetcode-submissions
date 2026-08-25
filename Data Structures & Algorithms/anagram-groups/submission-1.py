from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res={}
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key= tuple(count)# as tuple goes with dict and list can't
            if key not in res:
                res[key]=[s]# we can't use append as it goes only with list not with tupple
            else:
                res[key].append(s)
        return list(res.values())