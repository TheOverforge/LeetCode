class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        temp = [0] * n

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            # Если две части уже упорядочены, слияние можно пропустить
            if nums[mid] <= nums[mid + 1]:
                return

            merge(left, mid, right)

        def merge(left, mid, right):
            i = left
            j = mid + 1
            k = left

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1

            for p in range(left, right + 1):
                nums[p] = temp[p]

        merge_sort(0, n - 1)
        return nums