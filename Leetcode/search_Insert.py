from typing import List


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