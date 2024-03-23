class Solution:
    def sortSentence(self, s: str) -> str:
        vals = s.split()
        dic = {}
        res = [0] * len(vals)
        result = ''

        for i in vals:
            idx = i[-1]
            dic[idx] = i[:-1]
            res[int(idx)-1] = i[:-1]
        
        for i in res:
            result += i + ' '

        return result.strip()
                   
    