class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        n = len(s2)

        # if s1 is longer than s2 then s1 cannot be in s2
        if n < r + 1:
            return False
        
        # frequency map of s1
        f = {}
        for i in range(r + 1):
            if s1[i] not in f:
                f[s1[i]] = 0
            f[s1[i]] += 1
        
        # frequency map of current f2
        f2 = {}
        for i in range(r):
            if s2[i] not in f2:
                f2[s2[i]] = 0
            f2[s2[i]] += 1
        
        for i in range(r, n):
            tag = False
            # increment
            if s2[i] not in f2:
                f2[s2[i]] = 0
            f2[s2[i]] += 1

            # compare maps
            for i in f:
                if i not in f2 or f[i] != f2[i]:
                    tag = True
                    break
            
            if tag == False:
                return True
            



        return False

