class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        seq = {}

        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
        
        for i in s:
            # if i is a starter
            if (i-1) not in s:
                seq[i]=1
                x = i

                while x+1 in s:
                    x = x+1
                    seq[i]+= 1
            
        longest = 0
        for i in seq:
            if seq[i] > longest:
                longest = seq[i]
                
        return longest
            
        