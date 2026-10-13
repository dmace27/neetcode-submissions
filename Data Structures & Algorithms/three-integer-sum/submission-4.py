class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        answer_set = set()
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
                    s = [nums[i], nums[k], nums[j]]
                    ts = tuple(s)
                    if ts not in answer_set:
                        answer_set.add(ts)
                        ans.append(s)
            
            # manually check the cases after where the initial solution was 0
            if initial == 0:
                # simulate j -= 1 and then increment i
                for k in range(i+1, j-1):
                    if nums[i] + nums[k] + nums[j-1] == 0:
                        s = [nums[i], nums[k], nums[j-1]]
                        ts = tuple(s)
                        if ts not in answer_set:
                            answer_set.add(ts)
                            ans.append(s)
                i += 1
            elif initial > 0:
                j -= 1
            elif initial < 0:
                i += 1

            
            
        
        return ans
