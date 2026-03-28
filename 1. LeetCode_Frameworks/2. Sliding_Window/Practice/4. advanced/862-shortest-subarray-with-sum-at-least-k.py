from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        result = float('inf')

        for r in range(n + 1):
            while dq and prefix[r] - prefix[dq[0]] >= k:
                result = min(result, r - dq.popleft())
            while dq and prefix[r] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(r)

        return result if result != float('inf') else -1
