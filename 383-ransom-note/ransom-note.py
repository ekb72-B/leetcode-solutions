class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}

        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char,'', 1)
            else:
                return False

        return True