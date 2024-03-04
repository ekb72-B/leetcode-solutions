class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterdict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = ['']
        if not digits:
            return []

        for digit in digits:
            temp = []
            for letter in letterdict[digit]:
                for res in result:
                    temp.append(res + letter)
            result = temp
       
        return result