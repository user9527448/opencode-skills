# Common Anti-Patterns

## 1. String Concatenation in Loops

```python
# ❌ Anti-Pattern: O(n²) due to repeated string creation
result = ""
for item in items:
    result += str(item)

# ✅ Fix: O(n) with join
result = ''.join(str(item) for item in items)
```

## 2. Linear Search in Nested Loops

```python
# ❌ Anti-Pattern: O(n²) or O(n³)
for i in range(len(items)):
    for j in range(len(items)):
        if items[i] in other_list:  # O(n) lookup
            process(items[i])

# ✅ Fix: O(n) or O(n²) with hash set
other_set = set(other_list)
for i in range(len(items)):
    for j in range(len(items)):
        if items[i] in other_set:  # O(1) lookup
            process(items[i])
```

## 3. Repeated Function Calls with Same Input

```python
# ❌ Anti-Pattern: O(n) each time
def get_user_name(user_id):
    return db.query(f"SELECT name FROM users WHERE id = {user_id}")

for action in actions:
    name = get_user_name(action.user_id)  # Repeated calls
    print(f"{name}: {action}")

# ✅ Fix: Cache results
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_user_name(user_id):
    return db.query(f"SELECT name FROM users WHERE id = {user_id}")
```

## 4. Unnecessary List Creation

```python
# ❌ Anti-Pattern: Creates unnecessary list
def count_positive(numbers):
    return len([x for x in numbers if x > 0])

# ✅ Fix: Use generator
def count_positive(numbers):
    return sum(1 for x in numbers if x > 0)
```

## 5. Deep Copying When Shallow Copy Suffices

```python
import copy

# ❌ Anti-Pattern: Deep copy is expensive
new_dict = copy.deepcopy(original_dict)

# ✅ Fix: Shallow copy for simple structures
new_dict = original_dict.copy()  # or dict(original_dict)
```

## 6. Checking Length Inside Loops

```python
# ❌ Anti-Pattern: len() called every iteration (minor in Python, but matters in some languages)
for i in range(len(items)):
    if i < len(items) - 1:  # Unnecessary check
        process(items[i])

# ✅ Fix: Iterate directly
for item in items[:-1]:
    process(item)
# Or use enumerate
for i, item in enumerate(items):
    if i < len(items) - 1:
        process(item)
```

## 7. Over-Engineering with Classes

```python
# ❌ Anti-Pattern: Unnecessary class for simple operation
class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

result = Adder(1, 2).add()

# ✅ Fix: Simple function
def add(a, b):
    return a + b

result = add(1, 2)
```

## 8. Premature Optimization

```python
# ❌ Anti-Pattern: Optimize before measuring
def process(data):
    # Complex "optimized" code that's hard to maintain
    # but no evidence this is the bottleneck
    ...

# ✅ Fix: Profile first, then optimize
# 1. Write clear, simple code
# 2. Profile to find actual bottlenecks
# 3. Optimize only what matters
```

## 9. Global State for Caching

```python
# ❌ Anti-Pattern: Global state causes thread safety issues
_cache = {}

def get_data(key):
    if key not in _cache:
        _cache[key] = fetch_from_db(key)
    return _cache[key]

# ✅ Fix: Use local cache or proper caching library
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_data(key):
    return fetch_from_db(key)
```

## 10. Ignoring Algorithm Complexity

```python
# ❌ Anti-Pattern: Using wrong algorithm for data size
def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return None
# O(n²) - slow for large arrays

# ✅ Fix: Choose appropriate algorithm
def find_duplicate(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return item
        seen.add(item)
    return None
# O(n) - much faster
```
