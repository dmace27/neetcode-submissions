class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        n = size - 1

        a = 0
        b = 0
        while (1):
            b = nums[b]
            b = nums[b]
            a = nums[a]
            
            if a == b:
                return a