# Python Optimization Guide

## Anti-Patterns

| Anti-Pattern | Complexity | Solution |
|--------------|------------|----------|
| `for i in range(len(list))` | O(n) access | `for item in list` |
| String concat in loop | O(n²) | `''.join(list)` |
| `list.index(x)` in loop | O(n²) | Use `dict` or `set` |
| `x in list` check | O(n) | `x in set` → O(1) |
| Deep list copies | O(n) space | Use `itertools.islice` |
| `dict.keys()` / `dict.values()` list | O(n) | Iterate directly |

## Optimization Patterns

### List Comprehension vs Loop

```python
# Before: O(n) with append overhead
result = []
for x in data:
    if x > 0:
        result.append(x * 2)

# After: O(n) but faster
result = [x * 2 for x in data if x > 0]
```

### Dictionary Lookups

```python
# Before: O(n) for each lookup
for item in items:
    if item in target_list:  # O(n)
        process(item)

# After: O(1) for each lookup
target_set = set(target_list)
for item in items:
    if item in target_set:  # O(1)
        process(item)
```

### String Building

```python
# Before: O(n²) - creates new string each time
result = ""
for item in items:
    result += str(item)

# After: O(n) - single join
result = ''.join(str(item) for item in items)
```

### Generator vs List

```python
# Before: O(n) memory - entire list in memory
result = [expensive_computation(x) for x in large_data]

# After: O(1) memory - lazy evaluation
result = (expensive_computation(x) for x in large_data)
```

### functools.lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# O(2ⁿ) → O(n) with memoization
```

### itertools Optimizations

```python
import itertools

# Chain multiple iterables without copying
combined = itertools.chain(list1, list2, list3)

# Slice without copying
from itertools import islice
first_100 = islice(large_iterable, 100)

# Unique values preserving order
def unique_everseen(iterable):
    seen = set()
    for element in iterable:
        if element not in seen:
            seen.add(element)
            yield element
```

## Python-Specific Gotchas

| Issue | Impact | Solution |
|-------|--------|----------|
| Global Interpreter Lock (GIL) | No true parallelism for CPU-bound | Use multiprocessing |
| List multiplication `[[0]]*n` | Same reference | `[[0] for _ in range(n)]` |
| Default mutable args | Shared state | Use `None` default |
| `+=` on tuples | Creates new tuple | Use list instead |
