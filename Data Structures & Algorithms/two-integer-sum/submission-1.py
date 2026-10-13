class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        answer = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                answer.append(d[nums[i]])
                answer.append(i)
                break
        
        return answer
        
        
