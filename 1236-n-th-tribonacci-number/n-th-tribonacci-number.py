class Solution:
    def tribonacci(self, n: int) -> int:
        tridict = {}
        tridict[0] = 0
        tridict[1] = 1
        tridict[2] = 1

        if n == 0 or n == 1:
            return n
        
        if n == 2:
            return 1

        for i in range(3, n+1):
            tridict[i] = tridict[i-1] + tridict[i-2] + tridict[i-3]

        return tridict[n]


        # while n not in tridict:
        #     if n-1 in tridict and n-2 in tridict and n-3 in tridict:
        #         return tridict[n-1] + tridict[n-2] + tridict[n-3]
        #     else:
        #         tridict[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        # return tridict[n]
        
        

       