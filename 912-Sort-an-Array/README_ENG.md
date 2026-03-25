# 912. Sort an Array

Documentation for LeetCode 912 with explanations for the two Python solutions in this folder:

- `912(1).py` - a simple and readable `merge sort`
- `912(2).py` - a more optimized `merge sort` with a shared temporary buffer

---

## Problem Statement

We need to sort the array `nums` in ascending order and return the sorted result.

Example:

```text
Input:  [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

---

## Why Merge Sort Fits This Problem

`Merge sort` is a strong choice here because it:

- guarantees `O(n log n)` time
- works reliably on large inputs
- is easy to express recursively
- matches the kind of algorithmic approach expected in LeetCode problems

The idea is straightforward:

1. Split the array into two halves
2. Sort each half separately
3. Merge the two sorted halves into one final array

---

## Solution 1: `912(1).py`

This is the classic educational version of `merge sort`.

```python
class Solution(object):
    def sortArray(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        return merge_sort(nums)
```

### How It Works

1. If the array has `0` or `1` element, it is already sorted
2. The array is split into left and right halves
3. Both halves are sorted recursively
4. The `merge()` function combines the two sorted halves

### Pros

- very easy to read
- excellent for learning the idea behind `merge sort`

### Cons

- it uses slices like `arr[:mid]` and `arr[mid:]`
- new lists are created at many recursion steps
- in Python, this adds extra memory and copying overhead

---

## Solution 2: `912(2).py`

This is a more practical and efficient version of the same algorithm.

```python
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
```

### Why This Version Is Better

- it does not create subarrays with slicing
- it works with index boundaries `left` and `right`
- it reuses a single shared `temp` array
- it can skip the merge step if both neighboring parts are already in order

This check:

```python
if nums[mid] <= nums[mid + 1]:
    return
```

means the left half is already less than or equal to the right half at the boundary, so the current merge can be skipped.

### How It Works

1. Recursively sort the range `left..right`
2. After both halves are sorted, call `merge()`
3. Inside `merge()`, compare elements and write them into `temp`
4. Copy the sorted range back into `nums`

---

## Merge Sort Example

Take this array:

```text
[5, 2, 3, 1]
```

Split:

```text
[5, 2]   [3, 1]
```

After recursive sorting:

```text
[2, 5]   [1, 3]
```

After the final merge:

```text
[1, 2, 3, 5]
```

---

## Complexity

### `912(1).py`

- Time: `O(n log n)`
- Space: higher than classic `O(n)` because Python slices create extra lists

### `912(2).py`

- Time: `O(n log n)`
- Space: `O(n)` because of the shared `temp` array

---

## When to Use Each Version

- use `912(1).py` when readability and learning are the priority
- use `912(2).py` when performance matters more

---

## Main Idea to Remember

The power of `merge sort` comes from not trying to sort the entire array at once. Instead, we:

- break the problem into smaller parts
- solve each part recursively
- merge already sorted results

That is what gives the algorithm its stable `O(n log n)` performance.

---

## Conclusion

This folder shows two solid versions of the same algorithm:

- the first one is best for understanding the concept
- the second one is better for an efficient LeetCode submission

If you want to learn `merge sort`, start with `912(1).py`.
If you want the stronger practical version, focus on `912(2).py`.
