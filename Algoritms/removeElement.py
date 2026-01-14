class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0

        for element in nums:
            if element != val:
                nums[counter] = element
                counter +=1
        return counter
