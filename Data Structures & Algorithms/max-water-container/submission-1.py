class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        n = len(heights)
        l = 0
        r = 1

        def currArea(lh, li, rh, ri):
            height = min(lh, rh)
            length = abs(ri - li)
            area = height * length
            return area
        
        while l < r:
            a = currArea(heights[l], l, heights[r], r)
            if a > largest:
                largest = a
            
            if (l == r-1) and (r == n-1):
                break

            elif (l == r-1):
                r+= 1
                continue

            elif (r == n-1):
                l += 1
                continue

            elif (heights[l] >= heights[r]):
                r += 1
                continue

            else:
                l += 1
                continue
        
        return largest


