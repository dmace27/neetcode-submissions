class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = set(s)
        str2 = set(t)
        return ((str1 == str2) and (len(s) == len(t)))