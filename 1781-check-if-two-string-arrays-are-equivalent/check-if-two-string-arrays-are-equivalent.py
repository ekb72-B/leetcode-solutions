class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.wordAdd(word1) == self.wordAdd(word2)

    def wordAdd(self,word):
        res = ''
        for char in word:
            res += char
        return res
        