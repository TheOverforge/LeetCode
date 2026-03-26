<div align="center">

![Topic](https://img.shields.io/badge/Algorithm-Binary_Search-7c3aed?style=for-the-badge&logoColor=white)

![Language](https://img.shields.io/badge/Python-3b1f6e?style=flat-square&logo=python&logoColor=white)
![Problem](https://img.shields.io/badge/LeetCode_704-7c3aed?style=flat-square&logoColor=white)

</div>

# Binary Search

A clean and easy-to-follow explanation of the binary search algorithm based on a LeetCode-style solution.

---

## What is Binary Search?

**Binary Search** is an algorithm used to find an element in a **sorted array**.

Instead of checking elements one by one, it repeatedly looks at the **middle of the current range** and removes the half where the target definitely cannot be.

That is why it is much faster than a normal linear search.

---

## Main Requirement

Binary search works only if the array is **sorted in ascending order**.

Example:

```text
[-1, 0, 3, 5, 9, 12]
```

---

## Core Idea

We keep two search boundaries:

- `low` — left boundary
- `high` — right boundary

On each step:

1. Find the middle index
2. Compare the middle value with `target`
3. If they are equal — return the index
4. If the middle value is greater — move left
5. If the middle value is smaller — move right

---

## Python Code (LeetCode Format)

```python
class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid

            if guess > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
```

---

## Code Breakdown

### `low = 0`
The left boundary starts at the first index of the array.

### `high = len(nums) - 1`
The right boundary starts at the last valid index.

### `while low <= high`
As long as the search range still exists, we continue searching.

### `mid = (low + high) // 2`
We calculate the middle index of the current range.

### `guess = nums[mid]`
We take the value at index `mid`.

### `if guess == target`
If we found the target, we return its index immediately.

### `if guess > target`
If the middle value is greater than `target`, then the target can only be in the **left half**.

So we do:

```python
high = mid - 1
```

### `else`
If the middle value is smaller than `target`, then the target can only be in the **right half**.

So we do:

```python
low = mid + 1
```

### `return -1`
If the loop ends and the element was not found, we return `-1`.

That is exactly what LeetCode 704 requires.

---

## Example Walkthrough

Array:

```text
[-1, 0, 3, 5, 9, 12]
```

Target:

```text
9
```

### Step 1
- `low = 0`
- `high = 5`
- `mid = (0 + 5) // 2 = 2`
- `guess = nums[2] = 3`

`9 > 3`, so we move right.

### Step 2
- `low = 3`
- `high = 5`
- `mid = (3 + 5) // 2 = 4`
- `guess = nums[4] = 9`

Element found.

Answer: `4`

---

## Why is it Fast?

A normal search checks elements one by one.

Binary search **cuts the search range in half** every step.

Examples:

- `100` elements → about `7` steps
- `1,000` elements → about `10` steps
- `1,000,000` elements → about `20` steps
- `1,000,000,000` elements → about `30` steps

---

## Complexity

**Time Complexity:** `O(log n)`

This means that even when the array grows a lot, the number of operations increases very slowly.

Binary search is much faster than linear search `O(n)` on large sorted data.

---

## What You Should Remember

- the array must be **sorted**
- the search is done using **indexes**
- each step checks the **middle of the range**
- if `target` is smaller, go left
- if `target` is greater, go right
- if found, return the index
- if not found, return `-1`

---

## Conclusion

Binary Search is one of the most important basic algorithms.

It teaches a simple but powerful idea:

> Do not check everything if you can immediately eliminate half of the wrong options.

That is what makes the algorithm fast, elegant, and extremely useful in programming problems.
