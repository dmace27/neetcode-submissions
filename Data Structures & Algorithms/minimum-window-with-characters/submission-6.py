class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if m > n:
            return ""

        shortest = n + 1
        sl, sr = -2, -2
        ft, fs = {}, {}

        for i in t:
            ft[i] = ft.get(i, 0) + 1
        
        l, r = 0, 0

        while r < n:
            fs[s[r]] = fs.get(s[r], 0) + 1

            while l <= r:
                pos = True
                for i in ft:
                    if i not in fs or fs[i] < ft[i]:
                        pos = False
                        break
                if pos:
                    if (r - l + 1) < shortest:
                        shortest = r - l + 1
                        sl = l
                        sr = r

                    fs[s[l]] -=1
                    l += 1
                else:
                    break
            r += 1
        
        if sl != -2:
            return s[sl:sr + 1]
        else:
            return ""


