<div align="center">

![Framework](https://img.shields.io/badge/Framework_2-Sliding_Window-7c3aed?style=for-the-badge&logoColor=white)

![Language](https://img.shields.io/badge/Python-3b1f6e?style=flat-square&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Patterns-3-7c3aed?style=flat-square&logoColor=white)

</div>

# Sliding Window Framework

## 1. Where it fits in the bigger picture

LeetCode is easier to study as a **system**, not as a random set of tasks:

- **11 frameworks**
- **30 core patterns**
- the second framework: **Sliding Window**

The main idea is simple: do not memorize isolated solutions. Learn to **recognize the structure of a problem** and choose the right approach quickly.

---

## 2. What Sliding Window is

**Sliding Window** is an approach where we look at a **group of adjacent elements** in an array or string and move that group to the right, updating the answer efficiently without recalculating from scratch.

The goal is to:

- avoid unnecessary nested loops;
- solve problems in **O(n)** instead of **O(n²)**;
- work with **subarrays** and **substrings**.

---

## 3. When this framework usually appears

Sliding Window often appears when:

- we need to find something among **consecutive elements**;
- there is a constraint on the **length** or **composition** of a subarray;
- we need to find the **maximum / minimum / best** subarray;
- the data is an array or a string.

---

## 4. Main recognition flow

```text
Sliding Window
│
├── Is the window size fixed?
│   └── Yes → Fixed-size window
│
└── Window size is not fixed
    ├── Do elements split into non-overlapping groups?
    │   └── Yes → Non-overlapping windows
    │
    └── Need to find the best subarray by some condition?
        └── Yes → Variable-size window
```

### Questions to ask yourself

1. Is the window length **fixed** (is `k` given)?
2. Does the array split into **separate groups**, each element in exactly one group?
3. Do we need to find an **optimal subarray** with a variable length?

---

## 5. Main types of Sliding Window

### 5.1. Fixed-size window

#### Idea

If we need to find a characteristic among **`k` consecutive elements**, we use a fixed-size window.

First, we calculate the sum of the first window of length `k`.
Then we slide the window to the right:
- subtract the element that left from the left;
- add the element that entered from the right.

Each transition to the next window takes **O(1)**.

#### When to use

- maximum sum of `k` consecutive elements;
- average value for each window of length `k`;
- number of substrings of a fixed length.

#### Key transition formula

`new_window = old_window - left_element + right_element`

#### Example — LeetCode 643

```python
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
```

#### Complexity

- **Time:** `O(n)`
- **Memory:** `O(1)`

#### Green flags

- the problem gives a number `k`;
- we need to look at all windows of the same length;
- we need a sum, average, or other aggregation over a subarray.

---

### 5.2. Non-overlapping windows

#### Idea

If the array naturally splits into **groups**, and each element belongs to **exactly one group**, we use non-overlapping windows.

Two pointers:
- `l` — start of the current group;
- `r` — end of the current group.

We move `r` to the right while the group condition holds. We process the window `[l, r]`, then move to the next group: `l = r + 1`.

#### When to use

- compress consecutive numbers into ranges;
- split an array into groups by some condition;
- process blocks of identical or sequential elements.

#### Example

```python
def compress_ranges(nums: list[int]) -> list[str]:
    l = 0
    r = 0
    result = []

    while l < len(nums):
        while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
            r += 1

        if r != l:
            result.append(f"{nums[l]}->{nums[r]}")
        else:
            result.append(f"{nums[l]}")

        l = r + 1
        r = r + 1

    return result
```

#### Complexity

- **Time:** `O(n)` — both pointers only move forward
- **Memory:** `O(n)` — if the result is stored in a separate array

#### Green flags

- groups follow one after another;
- each element belongs to exactly one group;
- groups do not overlap.

---

### 5.3. Variable-size window

#### Idea

If we need to find the **best subarray** or **best substring** satisfying some condition, we use a variable-size window.

Two pointers:
- `l` — left boundary of the window;
- `r` — right boundary of the window.

We try to **expand the window to the right as much as possible**.
When we can no longer expand — we update the answer and shrink the window from the left.

#### The key is choosing the window state

**Window state** is a value that describes the current subarray and helps quickly decide: can we expand the window or should we shrink it.

For example, if we can replace at most `k` zeros with ones — the window state is `zeros_count`.

#### When to use

- longest substring without repeating characters;
- maximum length subarray with at most `k` bad elements;
- minimum subarray satisfying a condition.

#### Example — LeetCode 3

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r - l + 1)

        return result
```

#### Complexity

- **Time:** `O(n)` — both pointers only move to the right
- **Memory:** `O(1)`

#### Green flags

- we need to find the maximum / minimum / best subarray;
- there is a condition the window must satisfy;
- the window length changes.

---

## 6. What you should know before studying Sliding Window

Useful prerequisites:

- arrays
- two pointers
- hash maps (for some problems)

### Why this matters

**Arrays**
- indexing;
- working with boundaries;
- iterating over elements.

**Two Pointers**
- moving two pointers;
- understanding left and right boundaries;
- shrinking and expanding a range.

**Hash Maps**
- counting character frequencies;
- quickly checking the window condition;
- needed in substring problems.

---

## 7. Signs that a problem may be Sliding Window

### Common phrases

- `subarray`
- `substring`
- `contiguous`
- `window`
- `k elements`
- `longest` / `shortest`
- `maximum` / `minimum`

### What should trigger your attention

- `at most k` — at most `k` of something
- `without repeating` — no repeated characters
- `consecutive elements` — elements in a row
- `fixed length` — fixed size

---

## 8. Common mistakes

1. **Wrong window state**
   The wrong variable is chosen to describe the current window.

2. **Forgetting to update state when shrinking**
   When shifting `l` to the right, the window state is not updated.

3. **Wrong initialization**
   Especially relevant for variable-size: `r = -1` is needed so the window starts empty.

4. **Mixing up Fixed-size and Variable-size**
   If the problem gives `k` — most likely fixed-size. If not — variable-size.

5. **Unnecessary recalculation**
   Recalculating the entire window instead of using the transition formula.

---

## 9. Quick templates

### Fixed-size window

```python
window = sum(nums[:k])
best = window

for r in range(k, len(nums)):
    l = r - k
    window = window + nums[r] - nums[l]
    best = max(best, window)
```

### Non-overlapping windows

```python
l = 0
r = 0

while l < len(nums):
    while r + 1 < len(nums) and condition(r):
        r += 1

    # process window [l, r]

    l = r + 1
    r = r + 1
```

### Variable-size window

```python
l = 0
r = -1
result = 0

while l < len(nums):
    while r + 1 < len(nums) and can_expand(r + 1):
        update_state(r + 1)
        r += 1

    result = max(result, r - l + 1)

    remove_from_state(l)
    l += 1
```

---

## 10. Summary

### Sliding Window is a family of approaches

1. **Fixed-size window**
   - window length is fixed (`k`)
   - transition formula: `new = old - left + right`

2. **Non-overlapping windows**
   - array splits into non-overlapping groups
   - each element belongs to exactly one group

3. **Variable-size window**
   - window length changes
   - the key is choosing the right window state

### Main idea

Do not focus on the problem title. Focus on the **problem structure**:

- fixed `k` → fixed-size window
- non-overlapping groups → non-overlapping windows
- best subarray by condition → variable-size window

---

## 11. Practice problems

### Fixed-size window

- Maximum Average Subarray I
- Substrings of Size Three with Distinct Characters
- Find All Anagrams in a String

### Non-overlapping windows

- Summary Ranges
- Missing Ranges of Sorted Array

### Variable-size window

- Longest Substring Without Repeating Characters
- Max Consecutive Ones III
- Minimum Size Subarray Sum
