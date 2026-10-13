class Solution:
    def trap(self, height: List[int]) -> int:
        n, area = len(height), 0
        l, r = 0, n - 1

        left = [0] * n
        right = [0] * n

        lm, rm = 0, 0
        for i in range(n):
            left[i] = lm
            if height[i] > lm:
                lm = height[i]
        
        for i in range(n-1, 0, -1):
            right[i] = rm
            if height[i] > rm:
                rm = height[i]

        for i in range(n):
            mi = min(left[i], right[i])
            if height[i] < mi:
                area += (mi - height[i])
        
        return area
            

       


