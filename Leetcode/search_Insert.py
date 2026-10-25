from typing import List

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ix0, ixn = 0, len(nums) - 1
        while ixn >= ix0:
            mid = (ixn + ix0) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                ix0 = mid + 1
            elif target < nums[mid]:
                ixn = mid - 1
        return ixn + 1

Solution().searchInsert([1, 3, 5, 6], 2)

# Time Complexity: O(log n)
# Space Complexity: O(1)