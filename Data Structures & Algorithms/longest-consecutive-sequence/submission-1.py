class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set()
        n=len(nums)
        for i in range(0,n):
            h.add(nums[i])
        longest=0
        for num in h:
            if num-1 not in h:
                x=num #1
                count=1
                while x+1 in h:
                    count+=1
                    x+=1 #2
                longest=max(longest,count)
        return longest
