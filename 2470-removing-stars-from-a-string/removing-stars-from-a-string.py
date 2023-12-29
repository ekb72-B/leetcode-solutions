class Solution:
    def removeStars(self, s: str) -> str:
        # use two pointers?
        # split it into 2 stacks and start popping there
        

        # iterate, when you see a star, remove the item that preceded it
        # append values into result array bit if you see a star, then remove the last item of the result array and skip the star as well
        res = ''
        for i in s:
            if i != '*':
                res += i
            elif i == '*':
                res = res[:-1]
        return res

        