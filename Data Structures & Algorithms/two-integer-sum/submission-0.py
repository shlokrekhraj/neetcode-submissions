class Solution:
     def twoSum(self, nums, target): # nos are [2, 7, 11, 15] and target is 9
        d = {} # dict(HASHMAP) to store value -> index
        for i in range(len(nums)): # range=4, i=0,1,2,3
            need = target - nums[i]
            if need in d: # first iteration: need=7, not in d hence store 2 with index 0 in hashmap; second iteration: need=2, is in dict, return [0, 1]
                return [d[need], i]
            d[nums[i]] = i # store nums[i] with index i in hashmap example: d={2:0, 7:1, 11:2, 15:3}
        return []