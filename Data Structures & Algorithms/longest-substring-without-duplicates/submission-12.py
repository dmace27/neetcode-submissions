class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        longest = 1
        l = 0
        r = 1
        n = len(s)
        window = set()

        if n == 0:
            return n
        elif n > 0:
            window.add(s[0])
        
        while r < n:
            if s[r] not in window:
                window.add(s[r])
                longest = max(longest, len(window))
                r += 1
            else:
                window.discard(s[l])
                l += 1
        
        return longest