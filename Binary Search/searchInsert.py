class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Duplicated elements ?
        
        if target in nums:
            return bisect.bisect_left(nums, target)
        else:
            ordered = bisect.insort_left(nums,target)
            idx = bisect.bisect_left(nums, target)
            return idx
