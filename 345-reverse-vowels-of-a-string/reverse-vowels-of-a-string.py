class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels =  {'a': 1, "A":1 ,'e': 1, "E": 1, 'i': 1, "I": 1, 'o': 1, "O":1, 'u': 1, "U": 1 }
        sarr = list(s)
        start = 0
        end = len(s)-1
        res = ''

        while start < end:
            if sarr[start] in vowels and sarr[end] in vowels:
                sarr[start],sarr[end] = sarr[end],sarr[start]
                start += 1
                end -= 1

            elif sarr[start] in vowels and sarr[end] not in vowels:
                end -= 1
            
            elif sarr[start] not in vowels and sarr[end] in vowels:
                start += 1

            else:
                start += 1
                end -= 1
            
        for i in sarr:
            res += i
        
        return res