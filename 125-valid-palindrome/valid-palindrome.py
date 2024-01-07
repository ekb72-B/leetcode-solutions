class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        raceacar
        
        '''
        s1 = s.lower().strip()
        ns = []
        res = True
        for char in s1:
            if char.isalnum():
                ns.append(char)

        p1 = 0
        p2 = len(ns)-1
        while p1 < p2:
            if ns[p1] == ns[p2]:
                res = True
                p1 += 1
                p2 -= 1
            else:
                return False
        return res


        