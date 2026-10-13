class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
    
        longest, l, r, n = 1, 0, 1, len(s)
        window = set()
        
        if n > 0:
            window.add(s[l])
        while r < n:
            
            if s[r] not in window:
                window.add(s[r])
                if len(window) > longest:
                    longest = len(window)
                r += 1
            else:
                window.discard(s[l])
                l += 1
                
        return longest