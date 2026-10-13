class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        answer = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1

            while l < r:
                combo = nums[l] + nums[r] + nums[i]
                # win con
                if (combo == 0):
                    triple = [nums[l], nums[r], nums[i]]
                    triple.sort()
                    truple = tuple(triple)
                    
                    if truple not in answers:
                        answers.add(truple)
                        answer.append(triple)
                    break
                
                elif combo > 0:
                    r -= 1
                elif combo < 0:
                    l += 1
           
        return answer