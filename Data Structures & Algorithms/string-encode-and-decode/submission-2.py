class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        n = len(strs)
        if n < 100:
            enc += "0"
        if n < 10:
            enc += "0"
        
        enc += str(n)

        for i in range(n):
            length = len(strs[i])
            if length < 100:
                enc += "0"
            if length < 10:
                enc += "0"
            enc += str(length)
            enc += strs[i]
        
        return enc

    def decode(self, s: str) -> List[str]:
        n = int(s[0:3])
        p = 3
        answer = []
        for i in range(n):
            length = int(s[p:(p+3)])
            p += 3
            word = s[p:(p+length)]
            p+= length
            answer.append(word)
        
        return answer
        
        
        
