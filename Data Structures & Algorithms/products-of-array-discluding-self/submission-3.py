class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        prod = 1
        zero = 0
        zeroB = False

        for i in range(n):
            if nums[i] == 0:
                zero += 1
                zeroB = True
            else:
                prod *= nums[i]
        
        if zero <= 1:
            for i in range(n):
                if nums[i] == 0:
                    answer[i] = prod
                elif zeroB == True:
                    answer[i] = 0
                else:
                    answer[i] = int(prod / nums[i])


        return answer
        
        
        

