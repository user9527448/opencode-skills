# Functional Programming Optimization

## Core Techniques

### Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# O(2ⁿ) → O(n)

# Custom memoization
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

### Lazy Evaluation

```python
# Generator - compute on demand
def fibonacci_stream():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take only what's needed
from itertools import islice
first_10 = list(islice(fibonacci_stream(), 10))
```

### Fusion (Deforestation)

```python
# Before: Multiple traversals (O(3n))
result = list(filter(lambda x: x > 0,
                map(lambda x: x * 2,
                    data)))

# After: Single traversal (O(n))
result = [x * 2 for x in data if x > 0]

# Or fused generator
result = (x * 2 for x in data if x > 0)
```

### Tail Recursion

```python
# Before: Stack overflow for large n
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# After: Tail recursive (Python doesn't optimize, but shows pattern)
def factorial(n, acc=1):
    if n <= 1:
        return acc
    return factorial(n - 1, n * acc)

# Best: Iterative
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

## Function Composition

```python
from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# Usage
process = compose(
    lambda x: x * 2,
    lambda x: x + 1,
    lambda x: x ** 2
)
result = process(3)  # ((3**2) + 1) * 2 = 20
```

## Immutable Data Structures

```python
from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple

# Immutable tuple
Point = Tuple[int, int]
p = (1, 2)

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

# Frozen dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

## FP-Specific Optimizations

| Technique | When to Use | Impact |
|-----------|-------------|--------|
| Memoization | Pure functions, repeated calls | Time → Space |
| Lazy Evaluation | Large/infinite sequences | Compute only needed |
| Fusion | Multiple map/filter | Single traversal |
| Currying | Partial application | Reuse configurations |
| Point-free | Readable composition | Declarative style |
