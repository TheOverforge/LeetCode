class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]
        max_sum = window_sum

        for r in range(k, len(nums)):
            left = r - k
            window_sum = window_sum + nums[r] - nums[left]
            max_sum = max(max_sum, window_sum)

        return max_sum / k