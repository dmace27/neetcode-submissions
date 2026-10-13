class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l, r, n = 0, 0, 1, len(s)
        window = set()
        
        window.add(s[l])
        while 1:
            if s[r] not in window:
                window.add(s[r])
                if len(window) > longest:
                    longest = len(window)
            else:
                while s[r] in window:
                    window.discard(s[l])
                    l += 1
            
            if r == n - 1:
                break
            
            r += 1
                
        return longest