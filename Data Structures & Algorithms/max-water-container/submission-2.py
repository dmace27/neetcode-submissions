class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        l = 0
        r = n-1

        while (l < r):
            leng = r - l
            area = min(heights[l], heights[r]) * leng
            if area > max_area:
                max_area = area
            
            # two pointer logic
            if (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
            
        
        return max_area

        