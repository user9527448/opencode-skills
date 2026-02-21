# Time Optimization Patterns

## O(n²) → O(n) via Hash Map

```python
# Before: O(n²) - Nested loops with linear search
def find_pairs(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None

# After: O(n) - Single pass with hash map
def find_pairs(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
```

## O(n) → O(log n) via Binary Search

```python
# Before: O(n) - Linear search
def find_sorted(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# After: O(log n) - Binary search (requires sorted array)
def find_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## O(2ⁿ) → O(n) via Memoization

```python
# Before: O(2ⁿ) - Exponential recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# After: O(n) - Memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Or bottom-up DP (O(1) space)
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## O(n log n) → O(n) via Counting

```python
# Before: O(n log n) - Sort then find duplicates
def find_duplicates(arr):
    arr.sort()
    duplicates = []
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] and arr[i] not in duplicates:
            duplicates.append(arr[i])
    return duplicates

# After: O(n) - Hash map counting
from collections import Counter

def find_duplicates(arr):
    counts = Counter(arr)
    return [item for item, count in counts.items() if count > 1]
```

## O(n × m) → O(n + m) via Pre-processing

```python
# Before: O(n × m) - For each query, scan array
def range_sum(arr, queries):
    results = []
    for start, end in queries:
        results.append(sum(arr[start:end+1]))
    return results

# After: O(n + m) - Prefix sum
def range_sum(arr, queries):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    
    results = []
    for start, end in queries:
        results.append(prefix[end+1] - prefix[start])
    return results
```

## Multiple Passes → Single Pass

```python
# Before: O(3n) - Multiple passes
positive = [x for x in data if x > 0]
doubled = [x * 2 for x in positive]
result = [x for x in doubled if x < 100]

# After: O(n) - Single pass
result = [x * 2 for x in data if x > 0 and x * 2 < 100]
```
