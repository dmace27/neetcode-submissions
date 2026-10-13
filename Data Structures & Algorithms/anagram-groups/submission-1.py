class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        freq_tables = {}

        for s in strs:
            word = {}
            for ch in s:
                if ch not in word:
                    word[ch] = 0
                
                word[ch] += 1
            wordt = tuple(sorted(word.items()))
            if wordt not in freq_tables:
                freq_tables[wordt] = []
            freq_tables[wordt].append(s)
        

        for i in freq_tables:
            answer.append(freq_tables[i])
        
        return answer
