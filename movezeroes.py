"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
"""

class Solution:
    def moveZeroes(self, num):
        nonZero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[nonZero], nums[curr] = nums[curr], nums[nonZero] # you have to swap the values in the same line for swap to work
                nonZero += 1

# Lessons L