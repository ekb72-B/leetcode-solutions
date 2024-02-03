class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min(len(s) for s in strs)
        print(minlen)
        if minlen == 0:
            return ''
        for i in range(minlen):
            for st in strs:
                val = strs[0][i]
                if st[i] != val:
                    return st[:i]
        return st[:i+1]
        


