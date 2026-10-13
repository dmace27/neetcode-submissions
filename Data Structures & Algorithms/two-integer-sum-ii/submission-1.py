class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        

        while l < r:
            s = numbers[l] + numbers[r]
            # win condition
            if s == target:
                answer = []
                answer.append(l+1)
                answer.append(r+1)
                return answer
            # if the sum
            elif s > target:
                r -= 1
            elif s < target:
                l += 1
            
