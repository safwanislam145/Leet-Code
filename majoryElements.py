"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2  
"""

# Solution

class Solution:
    def majorityElement(self,nums):
        count={}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num]=1
            
        for num in count:
            if count[num] >= len(nums)//2:
                return num
        return 0
                