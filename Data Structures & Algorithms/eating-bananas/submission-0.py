class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = 0
        for i in piles:
            if m < i:
                m = i

        left = 0
        right = m

        if h == n:
            return m

        while left <= right:
            mid = (left + right) // 2
            
            # check if current mid is feasible
            cycles = 0
            for i in range(n):
                cycles += (piles[i] // mid)
                if piles[i] % mid != 0:
                    cycles += 1
            
            if cycles > h:
                left = mid + 1
            else:
                cycles2 = 0
                for i in range(n):
                    cycles2 += (piles[i] // (mid - 1))
                    if piles[i] % (mid - 1):
                        cycles += 1
                
                # if mid works but mid-1 doesnt -> mid is minimum
                if cycles2 > h:
                    return mid
                else:
                    right = mid - 1














          