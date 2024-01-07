class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using two stacks
        # reverse one of the strings then pop
        return sorted(s) == sorted(t)