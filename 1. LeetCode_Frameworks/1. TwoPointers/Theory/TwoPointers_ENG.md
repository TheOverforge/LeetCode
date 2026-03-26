<div align="center">

![Framework](https://img.shields.io/badge/Framework_1-Two_Pointers-7c3aed?style=for-the-badge&logoColor=white)

![Language](https://img.shields.io/badge/Python-3b1f6e?style=flat-square&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Patterns-3-7c3aed?style=flat-square&logoColor=white)

</div>

# Two Pointers Framework

## 1. Where it fits in the bigger picture

LeetCode is easier to study as a **system**, not as a random set of tasks:

- **11 frameworks**
- **30 core patterns**
- the first framework: **Two Pointers**

The main idea is simple: do not memorize isolated solutions. Learn to **recognize the structure of a problem** and choose the right approach quickly.

---

## 2. What Two Pointers is

**Two Pointers** is an approach where we use **two indices / two pointers** moving through:

- one array;
- one string;
- a linked list;
- two different sequences.

The goal is to:

- avoid unnecessary nested loops;
- reduce time complexity;
- solve problems in **O(n)** or **O(n + m)** instead of **O(n²)**.

---

## 3. When this framework usually appears

Two Pointers often appears when:

- there is **one or two sequences**;
- we need to find pairs, intersections, or matches;
- we need **in-place modification**;
- we need to move **from both ends**;
- the array is already **sorted**, or sorting helps.

---

## 4. Main recognition flow

```text
Two Pointers
│
├── Is there more than one sequence?
│   └── Yes → one pointer for each
│
└── Only one sequence
    ├── Do we need in-place modification?
    │   └── Yes → fast & slow
    │
    └── Otherwise → left & right
```

### Questions to ask yourself

1. Do I have **two sequences**?
2. Do I have **one sequence** that must be modified **in place**?
3. Do I have **one sequence** where the answer can be found **from both ends**?

---

## 5. Main types of Two Pointers

### 5.1. One pointer for each sequence

#### Idea

If there are **two sequences**, a common move is to place **one pointer on each**.

#### When to use

- intersection of two sorted arrays;
- merge of two sorted arrays;
- comparing two strings;
- synchronized traversal of two structures.

#### General logic

- if the left value is smaller, move the left pointer;
- if the right value is smaller, move the right pointer;
- if they are equal, process the match and move both.

#### Example

```python
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            result.append(nums1[p1])
            p1 += 1
            p2 += 1

    return result
```

#### Complexity

- **Time:** `O(n + m)`
- **Memory:** `O(k)` for the result

#### Green flags

- two sequences;
- sorted data or data that can be sorted;
- need `intersection`, `merge`, or `common elements`.

---

### 5.2. Fast and Slow

#### Idea

If there is **one sequence** and it must be modified **in place**, we often use:

- `fast` — scans all elements;
- `slow` — points to where the next valid element should go.

#### When to use

- Move Zeroes
- Remove Duplicates from Sorted Array
- Remove Element
- filtering without creating a new array

#### Intuition

`fast` scans the array.  
Whenever it finds a useful element, that element is moved to position `slow`, and then `slow` advances.

#### Example

```python
from typing import List

def move_zeroes(nums: List[int]) -> List[int]:
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums
```

#### Complexity

- **Time:** `O(n)`
- **Memory:** `O(1)`

#### Green flags

- the statement says `in-place`;
- extra space is not allowed;
- elements must be removed, grouped, or moved;
- relative order must be preserved.

---

### 5.3. Left / Right pointers

#### Idea

If there is **one sequence**, we can place:

- `left` at the beginning,
- `right` at the end,

and gradually **shrink the search range**.

#### When to use

- Two Sum II
- Valid Palindrome
- Container With Most Water
- pair search in a sorted array

#### General logic

- if the current pair works, the answer is found;
- if the sum is too small, move `left`;
- if the sum is too large, move `right`.

#### Example

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]
```

#### Complexity

- **Time:** `O(n)`
- **Memory:** `O(1)`

#### Green flags

- the array is sorted;
- we need a pair of elements;
- the range can be narrowed from both sides;
- the problem is about palindrome or edge comparison.

---

## 6. Arrays vs Linked Lists

Two Pointers is used not only in arrays and strings, but also in **linked lists**.

### In arrays and strings

It is convenient because:

- indices are available;
- `left`, `right`, `fast`, and `slow` are easy to manage;
- values are easy to compare.

### In linked lists

Two Pointers is often used for:

- finding the middle of a list;
- cycle detection;
- finding the `k`-th node from the end;
- splitting a list.

---

## 7. What you should know before studying Two Pointers

Useful prerequisites:

- arrays
- linked lists
- selection sort

### Why this matters

**Arrays**
- indexing;
- swap;
- boundaries;
- iteration.

**Linked Lists**
- `next` references;
- pointer movement;
- keeping links safe.

**Selection Sort**
- working with indices;
- finding minimums;
- understanding moving boundaries.

---

## 8. Signs that a problem may be Two Pointers

### Common phrases

- `sorted array`
- `in-place`
- `remove duplicates`
- `move zeroes`
- `find pair`
- `palindrome`
- `intersection`
- `merge`

### What should trigger your attention

- `without extra space`
- `preserve relative order`
- `two arrays`
- `two strings`
- `leftmost / rightmost`

---

## 9. Common mistakes

1. Wrong loop boundaries  
   For example, `left <= right` instead of `left < right`.

2. Moving the wrong pointer  
   The comparison is correct, but the pointer update is wrong.

3. Losing relative order  
   Common in problems like Move Zeroes.

4. Ignoring the sorted property  
   Some solutions only work when the data is sorted.

5. Mixing up `fast/slow` and `left/right`  
   These are different subpatterns.

---

## 10. Quick templates

### One pointer for each sequence

```python
p1 = 0
p2 = 0

while p1 < len(a) and p2 < len(b):
    if a[p1] < b[p2]:
        p1 += 1
    elif a[p1] > b[p2]:
        p2 += 1
    else:
        # handle match
        p1 += 1
        p2 += 1
```

### Fast and Slow

```python
slow = 0

for fast in range(len(nums)):
    if condition(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

### Left / Right

```python
left = 0
right = len(nums) - 1

while left < right:
    if condition_met:
        return answer
    elif need_move_left:
        left += 1
    else:
        right -= 1
```

---

## 11. Summary

### Two Pointers is a family of approaches

1. **One pointer for each sequence**
   - two sequences
   - merge / intersection / compare

2. **Fast and Slow**
   - one sequence
   - in-place modification

3. **Left / Right**
   - one sequence
   - movement from both ends

### Main idea

Do not focus on the problem title. Focus on the **problem structure**:

- two sequences → pointer for each
- one sequence + in-place → fast & slow
- one sequence + two ends → left & right

---

## 12. Practice problems

### Fast and Slow

- Move Zeroes
- Remove Duplicates from Sorted Array
- Remove Element

### One pointer for each

- Intersection of Two Sorted Arrays
- Merge Sorted Array
- Compare Strings with Backspaces

### Left / Right

- Two Sum II
- Valid Palindrome
- Container With Most Water