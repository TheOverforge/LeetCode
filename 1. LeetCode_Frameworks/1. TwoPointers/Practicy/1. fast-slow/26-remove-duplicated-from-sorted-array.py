class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow