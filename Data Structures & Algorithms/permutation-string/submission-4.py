class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        n = len(s2)

        # if s1 is longer than s2 then s1 cannot be in s2
        if n < r:
            return False
        
        # frequency map of s1
        f = {}
        for i in range(r):
            if s1[i] not in f:
                f[s1[i]] = 0
            f[s1[i]] += 1
        
        # frequency map of current f2
        f2 = {}
        for i in range(r - 1):
            if s2[i] not in f2:
                f2[s2[i]] = 0
            f2[s2[i]] += 1
        
        for i in range(r-1, n):
            tag = False
            # increment
            if s2[i] not in f2:
                f2[s2[i]] = 0
            f2[s2[i]] += 1

            # compare maps
            if len(f) != len(f2):
                tag = True
            else:
                for j in f:
                    if j not in f2 or f[j] != f2[j]:
                        tag = True
                        break
            
            if not tag:
                return True
            
            f2[s2[i - r + 1]] -= 1
            if f2[s2[i - r + 1]] == 0:
                del f2[s2[i - r + 1]]

          
        return False

