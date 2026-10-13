class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using prefix and suffix sums in a two pass

        ans = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            ans[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) -1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans