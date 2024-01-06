class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        digs = ''

        for dig in digits:
            digs += str(dig)

        res = int(digs) + 1
        # result is an int. turn back to string/ back to array

        for char in str(res):
            arr.append(int(char))

        return arr