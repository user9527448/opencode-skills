# Space Optimization Patterns

## O(n) → O(1) In-place Operations

```python
# Before: O(n) space - Creates new array
def reverse_array(arr):
    return arr[::-1]

# After: O(1) space - In-place reversal
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

## O(n) → O(1) with Two Pointers

```python
# Before: O(n) space - Store all values
def has_cycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

# After: O(1) space - Floyd's cycle detection
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True
```

## O(n) → O(1) by Modifying Input

```python
# Before: O(n) space - New array for result
def remove_duplicates(arr):
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result

# After: O(1) space - In-place with set tracking
def remove_duplicates(arr):
    seen = set()
    write_idx = 0
    for item in arr:
        if item not in seen:
            seen.add(item)
            arr[write_idx] = item
            write_idx += 1
    return arr[:write_idx]
```

## List → Generator

```python
# Before: O(n) space - All items in memory
def read_large_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

# After: O(1) space - Lazy evaluation
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Usage
for line in read_large_file('huge.txt'):
    process(line)
```

## O(n²) → O(n) with Bit Manipulation

```python
# Before: O(n) space - Track seen numbers
def find_single_number(nums):
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
    for num, count in seen.items():
        if count == 1:
            return num

# After: O(1) space - XOR operation
def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
# Works because: a ^ a = 0, a ^ 0 = a
```

## Recursion → Iteration

```python
# Before: O(n) space - Call stack
def sum_list_recursive(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + sum_list_recursive(arr, idx + 1)

# After: O(1) space - Iteration
def sum_list_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

## Matrix → Flattened Array

```python
# Before: O(n²) space - 2D array
def create_matrix(n, m):
    return [[0] * m for _ in range(n)]

# After: O(n) space - 1D array with index mapping
def create_matrix(n, m):
    return [0] * (n * m)

def get_element(flat, n, m, row, col):
    return flat[row * m + col]

def set_element(flat, n, m, row, col, value):
    flat[row * m + col] = value
```
