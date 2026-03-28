from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window_sum = 0
        result = float('inf')

        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                result = min(result, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return result if result != float('inf') else 0
