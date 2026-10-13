class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ds = {}
        dt = {}

        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = 0
            ds[s[i]] += 1
        

        for i in range(len(t)):
            if t[i] not in dt:
                dt[t[i]] = 0
            dt[t[i]] += 1

        for i in ds:
            if i not in dt or ds[i] != dt[i]:
                return False
        
        return True
