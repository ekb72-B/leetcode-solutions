class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        re = text.split(' ')
        rd = {}
        ctr = 0

        # check if the word has any values that are in brokenletters

        for word in re:
            check = True 
            for char in brokenLetters:
                if char in word:
                    check = False

            if check:
                ctr += 1

        return ctr
            
                    
        
        



                     

        