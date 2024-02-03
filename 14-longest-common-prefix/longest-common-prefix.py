class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min(len(s) for s in strs)
        print(minlen)
        if minlen == 0:
            return ''
    
        if len(strs) < 2:
            return strs[0]

        '''
        go through all the strings at once comparing their values
        
        if strs[x][0] is the same, incrememnt 1 and stop if it ever isn't.
        turn them all to arrays?

        '''
        for i in range(minlen):
            for st in strs:
                print('here', st, strs[0][i], st[i])
                val = strs[0][i]
                if st[i] != val:
                    return st[:i]
                else:
                    continue

        
        return st[:i+1]
        


