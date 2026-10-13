class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 1 + k
        n = len(s)
        d = {}
        r = 1
        l = 0
        m = 0
        ch = '0'
        # total frequency map
        total = {}
        for i in s:
            if i not in total:
                total[i] = 1
            else:
                total[i] += 1
            # finding most frequent letter
            if total[i] > m:
                m = total[i]
                ch = i
        if k + m >= n:
            return n
        # setup initial window
        else:
            d[s[0]] = 1
            if s[1] in d:
                d[s[1]] += 1
            else:
                d[s[1]] = 1
        
        # sliding window
        while r+1 < n:
            #q = 0
            #for i in d:
            #    if d[i] > q:
            #        q = d[i]
            
            q = d[ch]
            # if the window passes the condition -> extend window
            # if k + the frequency of the most popular letter in the window is 
            # greater than or equal to the size of the window -> the window passes
            if q + k >= (r - l + 1):
                # only checks for a new longest window if the current window is valid
                if r - l + 1 > length:
                    length = r - l + 1
                
                r += 1
                if s[r] in d:
                    d[s[r]] += 1
                else:
                    d[s[r]] = 1


            # if the window fails the condition -> retract window
            else:
                d[s[l]] -= 1
                l += 1
        return length
            

            