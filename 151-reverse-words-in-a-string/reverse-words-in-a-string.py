class Solution:
    def reverseWords(self, s: str) -> str:
        # iterate through the word backwards, if u meet a space then put the rest of the word in a result 
        a = s.split()
        res = ''

        for i in a[::-1]:
            res += i +' '
            
        return res[:-1]