class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        que = deque(s.split(' '))
        
        while que:
            val = que.pop()
            if val != '':
                return len(val)
        return 0