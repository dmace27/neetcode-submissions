class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                answer.append(d[nums[i]])
                answer.append(i)
                return answer
            else:
                d[target-nums[i]] = i