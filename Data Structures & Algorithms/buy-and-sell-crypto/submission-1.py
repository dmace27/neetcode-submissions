class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        l, r = 0, 1
        n = len(prices)

        while r < n:
            curr = prices[r] - prices[l]

            if curr > most:
                most = curr
            
            # pointer movement
            if curr <= 0:
                l += 1

                if l == r:
                    r += 1
            
            elif curr > 0:
                r += 1
            
                
        return most
            