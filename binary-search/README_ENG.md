# Binary Search

## What it is

**Binary Search** is an algorithm for finding an element in a **sorted array**.  
It works faster than a regular search because at each step it **discards half of the array**.

---

## Main condition

Binary search works **only with sorted data**.

Example of a valid array:

[1, 3, 5, 7, 9]

---

## Algorithm idea

At each step, the algorithm:

1. Takes the left boundary.
2. Takes the right boundary.
3. Finds the middle.
4. Compares the middle value with the target number.
5. If found, returns the index.
6. If the target is smaller, continues searching in the left part.
7. If the target is greater, continues searching in the right part.

---

## Important to understand

Binary search divides **not the values themselves**, but the **range of indices**.

That means:

- `low` — left index
- `high` — right index
- `mid = (low + high) // 2` — middle index
- `guess = list[mid]` — value at that index

---

## Example

Array:

index:   0  1  2  3  4  
value:   1  3  5  7  9

We are looking for `3`.

### Step 1
- `low = 0`
- `high = 4`
- `mid = (0 + 4) // 2 = 2`
- `guess = list[2] = 5`

`3 < 5`, so we search in the left part.

### Step 2
- `low = 0`
- `high = 1`
- `mid = (0 + 1) // 2 = 0`
- `guess = list[0] = 1`

`3 > 1`, so we search in the right part.

### Step 3
- `low = 1`
- `high = 1`
- `mid = (1 + 1) // 2 = 1`
- `guess = list[1] = 3`

The element is found. The answer is index `1`.

---

## Python code

```python
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))   # 1
print(binary_search(my_list, -1))  # None



Why it is fast

A regular search checks elements one by one.
Binary search cuts the search area in half each time.

Example:

100 elements → about 7 steps maximum
1,000 elements → about 10 steps maximum
1,000,000,000 elements → about 30 steps maximum
Complexity

Time complexity: O(log n)

This means that as the array size grows, the number of operations grows slowly.

Binary search is much faster than linear search O(n) on large datasets.

What to remember
the array must be sorted
the search works with indices
the algorithm compares the value in the middle of the array
if the element is smaller than the middle value, go left
if it is greater, go right
if it is equal, return the index
Conclusion

Binary search is a basic and very important algorithm that shows how search can be accelerated with the right strategy: instead of checking everything one by one, it discards half of the data at each step.