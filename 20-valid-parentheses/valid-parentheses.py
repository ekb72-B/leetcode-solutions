class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(' : ')', '{' : '}', '[' : ']'}
        bstack = []
        for bracket in s:
            if bracket in brackets:
                bstack.append(bracket)
            elif len(bstack) == 0 or bracket != brackets[bstack.pop()]:
                return False

        return len(bstack) == 0