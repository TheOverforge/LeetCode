class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1                             # last real element in nums1
        p2 = n - 1                             # last element in nums2
        write = m + n - 1                      # write position from the end

        while p2 >= 0:                         # while nums2 still has elements
            if p1 >= 0 and nums1[p1] > nums2[p2]:  # nums1 value is larger
                nums1[write] = nums1[p1]       # place nums1[p1] at write
                p1 -= 1                        # move nums1 pointer left
            else:                              # nums2 value is larger or nums1 is exhausted
                nums1[write] = nums2[p2]       # place nums2[p2] at write
                p2 -= 1                        # move nums2 pointer left
            write -= 1                         # move write pointer left