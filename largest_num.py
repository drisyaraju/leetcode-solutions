#Given an array of integers nums, return the value of the largest element in the array
class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for num in nums:
            if largest<num:
                largest=num
        return largest