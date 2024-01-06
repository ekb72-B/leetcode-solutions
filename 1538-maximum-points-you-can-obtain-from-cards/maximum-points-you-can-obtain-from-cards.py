class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # check whether first and last are the same. if so, check the numbers next to choose the direction you're going in
        start = 0 
        res = 0
        currsum = sum(cardPoints[:k])
        maxsum = currsum
        left = k-1
        right = len(cardPoints) -1

        for i in range(k):
            currsum += (cardPoints[right] - cardPoints[left])

            maxsum = max(maxsum, currsum)

            left -= 1
            right -=1
        
        return maxsum