class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        mid = (start + end)//2 
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vstart = 0
        vend = 0
        while start < end:
            if s[start] in vowels:
                vstart += 1
            if s[end] in vowels:
                vend += 1
            start += 1
            end -= 1 
        return vstart == vend 