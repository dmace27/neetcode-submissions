class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        n = size - 1

        a = 0
        b = 1
        while a != b:
            if nums[a] == nums[b]:
                return nums[a]
            else:
                b = nums[b]
                b = nums[b]
                a = nums[a]