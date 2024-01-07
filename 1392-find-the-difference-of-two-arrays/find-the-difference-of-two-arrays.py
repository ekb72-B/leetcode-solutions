class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []

        return [self.adder(set1,set2), self.adder(set2,set1)]

    def adder(self,setx, sety):
        res = []
        for i in setx:
            if i not in sety:
                res.append(i)
        return res
        