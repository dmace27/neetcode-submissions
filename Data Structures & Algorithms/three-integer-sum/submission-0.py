class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        # sort array
        for i1 in range(n):
            for i2 in range(i1+1, n):
                if nums[i1] > nums[i2]:
                    temp = nums[i1]
                    nums[i1] = nums[i2]
                    nums[i2] = temp

        i = 0
        j = n - 1
        while i < j:
            initial = nums[i] + nums[j]
            for k in range(i+1, j):
                if initial + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
            
            if initial >= 0:
                j -= 1
            elif initial < 0:
                i += 1
            
            
        
        return ans
