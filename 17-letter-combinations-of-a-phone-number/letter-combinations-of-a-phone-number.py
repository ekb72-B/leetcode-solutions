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
            print(digit, temp)
            for letter in letterdict[digit]:
                print( letter, result , "here")
                for res in result:
                    print(res, "res")
                    temp.append(res + letter)
                    print(temp, "temp")
            result = temp
       
        return result