class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m, shortest = len(s), len(t), len(s)
        if m > n:
            return ""
        sl, sr = -1, -1
        l, r = 0, 0
        ft, fs = {}, {}
        tag = True

        # freq map for t and initial window in s
        for i in range(m):
            if t[i] not in ft:
                ft[t[i]] = 0
            ft[t[i]] += 1
            if s[i] not in fs:
                fs[s[i]] = 0
            fs[s[i]] += 1
        # initial condition check
        for i in ft:
            if i not in fs or fs[i] < ft[i]:
                tag = False
                break
        if tag:
            return s[0:m]

        fs[s[m - 1]] -= 1
        while r < n:
            pos = True
            # ingest new index
            if s[r] not in fs:
                fs[s[r]] = 0
            fs[s[r]] += 1
            # condition check
            for i in ft:
                if i not in fs or fs[i] < ft[i]:
                    pos = False
                    break
        
            # move pointers
            # if the current window is valid:
            # move the left pointer in until it isn't valid
            while pos:
                if shortest > (r - l + 1):
                    shortest = r - l + 1
                    sl = l
                    sr = r
                fs[s[l]] -= 1
                l += 1
                # cond check while we reel the left in
                for i in ft:
                    if i not in fs or fs[i] < ft[i]:
                        pos = False
                        break
                    
            r += 1
        

        if sl != -1:
            return s[sl:sr + 1]
        else:
            return ""
                    
        


