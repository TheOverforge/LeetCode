class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0                  # empty array -> no unique elements

        slow = 1                               # next position for a unique value

        for fast in range(1, len(nums)):       # scan from the second element
            if nums[fast] != nums[slow - 1]:   # found a new unique value
                nums[slow] = nums[fast]        # write it into the unique section
                slow += 1                      # expand the unique section

        return slow                            # number of unique elements