class Solution:
    def isValid(self, s: str) -> bool:
        # do this using a stack where you split the values into 2
        # use one stack 

        sstack = []
        brackdic = {
            '(': ')', 
            '{' : '}', 
            '[' : ']'
        }

        for bracket in s:
            if bracket in brackdic:
                sstack.append(bracket)
            elif len(sstack) == 0 or bracket != brackdic[sstack.pop()]:
                return False

        return len(sstack) == 0

            
        

        