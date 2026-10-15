class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        n = len(nums)
        if n == 1 or k == 1:
            return nums

        answer = [None] * (n - k + 1)

        #ingest initial window
        cm = -10001
        for i in range (r):
            cm = max(nums[i], cm)

        for i in range(r, n):
            # ingest new number
            cm = max(nums[i], cm)
            # add to list
            answer[l] = cm

            if nums[l] != cm:
                l += 1
                continue
            else:
                l += 1
                cm = nums[l]
                for j in range(l, i+1):
                    cm = max(cm, nums[j])


        return answer




