"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List
import time


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        print(f"List nums: {nums}")
        """
        We embrace O(n) over O(n^2). Basics on Time complexity:
        - **Constant Time Complexity:** O(1) - The algorithm takes the same amount of time regardless of the input size.
        - **Linear Time Complexity:** O(n) - The algorithm's running time grows linearly with the input size.
        - **Quadratic Time Complexity:** O(n^2) - The algorithm's running time grows quadratically with the input size.
        """
        # Time complexity (0(n^2))
        # for each in range(len(nums)):
        #     nums_pair = nums[:each] + nums[each + 1:]
        #     for each_pair in range(len(nums_pair)):
        #         if nums[each] + nums_pair[each_pair] == target:
        #             pair_index = [x for x, y in enumerate(nums) if y == nums[each] and x != each][0] if nums[each] == \
        #                                                                                                 nums_pair[
        #                                                                                                     each_pair] \
        #                 else nums.index(
        #                 nums_pair[each_pair])
        #             print(f"Indices of integer array that sums upto target:{target} => {each}, {pair_index}")
        #             return [each, pair_index]

        # Time complexity (0(n))
        num_dict = {}
        for index, elem in enumerate(nums):
            complement = target - elem
            if complement in num_dict:
                print(f"Indices of integer array that sums upto target:{target}: {index}, {num_dict[complement]}")
                return [num_dict[complement], index]
            num_dict[elem] = index


Solution().twosum([3, 3, 3], 6)
