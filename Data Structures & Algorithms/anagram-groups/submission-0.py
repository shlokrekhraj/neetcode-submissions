from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs: # This loop picks one word at a time.
            count = [0] * 26 # 26 0's which looks like:- 1010...1 for "act" but after we do ord(ch)-ord('a'), then we go on for other s.
            for ch in s: # each char in word "act"
                count[ord(ch) - ord('a')] += 1 # eg:ord of a=100 hence, 100-100=0, for c=102, 102-100=2 HENCE: count[0]+1=>0+1=2, count[2]+1=>2, count[20]+1=>2
# If a letter appears once, it becomes 1, If it appears twice, it becomes 2
            key = tuple(count) #convert list to tuple as List cannot be dictionary keys

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return list(res.values())