class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chardict = {}
        for char in magazine:
            if char in chardict:
                chardict[char] += 1
            else:
                chardict[char] = 1

        for char in ransomNote:
            if char in chardict and chardict[char] >0:
                chardict[char] -= 1
            else:
                return False 

        return True
