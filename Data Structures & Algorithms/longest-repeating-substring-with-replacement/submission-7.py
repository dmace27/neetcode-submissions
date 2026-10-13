class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 1
        cd = {} # freq map of the current letters in the window
        new = True
        longest = 1
        mf = 0

        if n == 0:
            return 0
        else:
            cd[s[0]] = 1
            mf += 1


        while r < n:
            if s[r] not in cd:
                cd[s[r]] = 0
            cd[s[r]] += 1
            
            # check for most frequent letter
            mf = max(mf, cd[s[r]])
            
            if k < ((r - l + 1) - mf):
                cd[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))

            r += 1
        return longest

