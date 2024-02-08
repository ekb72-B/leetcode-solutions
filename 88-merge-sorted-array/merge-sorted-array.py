class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.


        two pointers and a temp

        p1 compare p2, the lesser one placed in temp and the used one increments. 
        always compare p1,p2,temp

        """
        l1end, l2end, lindx = m -1, n-1 , m+n -1

        while l2end >= 0:
            if l1end >=0 and nums1[l1end] > nums2[l2end]:
                nums1[lindx] = nums1[l1end]
                l1end -= 1

            else:
                nums1[lindx] = nums2[l2end]
                l2end -= 1

            lindx -= 1