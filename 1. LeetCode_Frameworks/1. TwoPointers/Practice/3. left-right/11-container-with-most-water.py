class Solution(object):
    def maxArea(self, height):
        left = 0                               # left pointer
        right = len(height) - 1                # right pointer
        best = 0                               # best area found so far

        while left < right:                    # keep shrinking the range
            width = right - left               # container width
            area = min(height[left], height[right]) * width  # current area
            best = max(best, area)             # update best answer

            if height[left] < height[right]:   # shorter wall is on the left
                left += 1                      # move left pointer
            else:                              # shorter wall is on the right
                right -= 1                     # move right pointer

        return best                            # maximum area