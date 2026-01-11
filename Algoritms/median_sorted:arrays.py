class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## Merge two sorted arrays , if array is odd return central , if
        # it is even 2 central alues and divide them by 2

        nums3 = sorted(nums1+nums2)
        if len(nums3) % 2 == 1:
            return nums3[len(nums3)//2]
        else:
            n1 = nums3[(len(nums3)//2) - 1] 
            n2 = nums3[len(nums3)//2]
            return (n1 + n2) / 2
