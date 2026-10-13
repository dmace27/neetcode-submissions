class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 # length of the substring
        n = len(s)
        d = {} # hashmap to store the frequency of the chars
        i = 0 # left side of the window
        j = 1 # right side of the window
        d[s[0]] = 1
        d[s[1]] = 1
        while j < n - 1:
            # checking the length of the hashmap
            if len(d) == j - i + 1:
                # add a letter to the right of the window
                j += 1
                if not s[j] in d:
                    d[s[j]] = 1
                else:
                    d[s[j]] += 1
            # remove a letter from the left of the window
            else:
                if d[s[i]] > 1:
                    d[s[i]] -= 1
                else:
                    # if the char is no longer in the window, delete the entry
                    del d[s[i]]
                i += 1
                if i == j:
                    j += 1
                    if not s[j] in d:
                        d[s[j]] = 1
                    else:
                        d[s[j]] += 1
            if len(d) > l:
                l = len(d)

        return l



        


             
        