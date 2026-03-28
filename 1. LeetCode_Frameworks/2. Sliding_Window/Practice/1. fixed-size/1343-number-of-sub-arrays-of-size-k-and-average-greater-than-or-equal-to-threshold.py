from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        count = 0

        if window_sum / k >= threshold:
            count += 1

        for r in range(k, len(arr)):
            l = r - k
            window_sum = window_sum + arr[r] - arr[l]
            if window_sum / k >= threshold:
                count += 1

        return count
