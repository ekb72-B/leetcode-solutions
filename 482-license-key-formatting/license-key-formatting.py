class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # take all items and turn to caps
        s = s.upper()[::-1]
        res = ''
        ctr = 0

        if len(s) == 1:
            if s[0].isalnum():
                return s
        # after turning all to upper, now go in and remove dashes.
        for i in range(len(s)):
            if s[i].isalnum() and ctr %(k) != 0:
                res+= s[i]
                ctr += 1

            elif s[i].isalnum() and ctr % (k) == 0:
                res += '-'
                res += s[i]
                ctr += 1

        # if res:
        #     if res[0] == '-':
        #         res = res[1:][::-1]

        return res[1:][::-1]
        # starting from the back, add - when you see x number of items

            
                