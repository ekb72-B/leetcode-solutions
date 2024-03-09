class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        so = sorted(arr)
        dic = {}
        val = 1
        res = []

        for i in so:
            if i not in dic:
                dic[i] = val
                val += 1

        for i in arr:
            res.append(dic[i])
        
        return res

        