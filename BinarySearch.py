'''
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        low=0
        high=len(nums)
        while low<high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid
        return low
