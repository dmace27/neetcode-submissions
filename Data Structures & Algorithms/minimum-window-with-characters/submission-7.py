class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        ft = {}
        for i in t:
            ft[i] = ft.get(i, 0) + 1
        
        required = len(ft)
        formed = 0
        fs = {}
        l, r = 0, 0

        shortest, sl, sr = len(s) + 1, None, None

        while r < len(s):
            fs[s[r]] = fs.get(s[r], 0) + 1

            if s[r] in ft and fs[s[r]] == ft[s[r]]:
                formed += 1
            
            while l <= r and formed == required:
                if (r - l + 1) < shortest:
                    shortest = r - l + 1
                    sr = r
                    sl = l
                
                fs[s[l]] -= 1
                if s[l] in ft and fs[s[l]] < ft[s[l]]:
                    formed -= 1
                
                l += 1
            
            r += 1

        if sl != None:
            return s[sl:sr + 1]
        else:
            return ""