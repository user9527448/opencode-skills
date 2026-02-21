---
name: code-complexity-optimizer
description: Algorithm complexity optimization skill. Analyzes time/space complexity, guides optimization through interactive Q&A, and provides tradeoff analysis. Trigger with "code optimization" or "complexity optimization".
license: MIT
compatibility: opencode
metadata:
  author: user9527448
  tags:
    - optimization
    - complexity
    - performance
    - algorithms
  triggers:
    - "代码优化"
    - "code optimization"
    - "complexity optimization"
    - "时间复杂度优化"
    - "空间复杂度优化"
    - "性能优化"
    - "algorithm optimization"
---

# Code Complexity Optimizer

## Overview

Systematic algorithm optimization through complexity analysis. Analyzes time complexity (O(n), O(log n), O(n²), etc.) and space complexity, guides optimization via interactive Q&A, and provides clear tradeoff recommendations.

## Trigger Conditions

**Use this skill when user requests:**
- "代码优化" / "code optimization"
- "复杂度优化" / "complexity optimization"
- "时间复杂度优化" / "time complexity optimization"
- "空间复杂度优化" / "space complexity optimization"
- "性能优化" / "performance optimization"
- "算法优化" / "algorithm optimization"
- Or mentions O(n), Big O notation, performance bottlenecks

---

## Phase 1: Code Analysis

### Step 1.1: Identify Target Code

If user hasn't specified code to optimize:
```
请提供需要优化的代码片段或指出具体文件/函数位置。
```

### Step 1.2: Analyze Current Complexity

**MANDATORY: Before any optimization, analyze and document:**

| Aspect | Current Value | Evidence |
|--------|---------------|----------|
| Time Complexity | O(?) | Identify loops, recursion, nested operations |
| Space Complexity | O(?) | Identify data structures, recursion depth, allocations |
| Input Size Range | n = ? | Typical input sizes the code handles |
| Bottleneck | ? | What operation dominates runtime |

**Analysis Checklist:**
- [ ] Count loop iterations (nested loops → O(n²), O(n³))
- [ ] Identify recursion depth and branching
- [ ] Check data structure operations (hash map lookup vs array search)
- [ ] Note string operations (concatenation in loops)
- [ ] Identify redundant computations

**Common Complexity Patterns:**

| Pattern | Time | Space | Example |
|---------|------|-------|---------|
| Single loop | O(n) | O(1) | Linear search |
| Nested loops | O(n²) | O(1) | Bubble sort |
| Binary recursion | O(2ⁿ) | O(n) | Fibonacci naive |
| Divide & conquer | O(n log n) | O(log n) | Merge sort |
| Hash map lookup | O(1) avg | O(n) | Dictionary access |
| Sorting | O(n log n) | O(n) | Built-in sort |

---

## Phase 2: Clarify Optimization Goals

### Step 2.1: Ask Clarifying Questions

**If user hasn't specified optimization direction, ask:**

```
我分析了代码的当前复杂度：
- 时间复杂度: O(?)
- 空间复杂度: O(?)

请告诉我您的优化目标：
1. 【优先时间】希望减少运行时间（牺牲空间换时间）
2. 【优先空间】希望减少内存占用（牺牲时间换空间）
3. 【平衡优化】在时间和空间之间寻找平衡
4. 【自动判断】让我根据实际情况选择最优方案
```

### Step 2.2: Understand Constraints

Ask about:
- **Input size**: How large is n typically? (10, 1000, 10⁶?)
- **Frequency**: How often is this code called?
- **Environment**: Memory constraints? Time limits?
- **Correctness**: Can algorithms change? Must maintain exact behavior?

---

## Phase 3: Optimization Strategy Selection

### Time Optimization Strategies

| Strategy | When to Use | Tradeoff |
|----------|-------------|----------|
| Hash Map / Set | Frequent lookups | +Space |
| Memoization | Repeated subproblems | +Space |
| Precomputation | Known input patterns | +Space |
| Lazy Evaluation | Not all results needed | Complexity |
| Two Pointers | Sorted/linked structures | - |
| Sliding Window | Contiguous subarrays | - |
| Binary Search | Sorted data | - |
| Early Exit | Search with conditions | - |

### Space Optimization Strategies

| Strategy | When to Use | Tradeoff |
|----------|-------------|----------|
| In-place Algorithm | Array modifications | +Time |
| Generator/Iterator | Large sequences | +Time |
| Reference Passing | Large objects | Mutable state |
| Bit Manipulation | Boolean flags | Complexity |
| Streaming | Large datasets | +Time |
| Recursion → Iteration | Deep recursion | Stack |

### Balanced Optimization

| Strategy | Time Impact | Space Impact |
|----------|-------------|--------------|
| Optimal data structures | ↓ | ↓ |
| Algorithm replacement | ↓ | ↔ |
| Code simplification | ↓ | ↓ |

---

## Phase 4: Optimization Execution

### Step 4.1: Propose Changes

**Format:**
```
优化方案: [Strategy Name]

当前复杂度: Time O(?), Space O(?)
优化后复杂度: Time O(?), Space O(?)

改进点:
- [具体改进1]
- [具体改进2]

权衡说明:
- [时间/空间变化]
- [适用场景]

是否应用此优化？
```

### Step 4.2: Apply Changes

When user confirms:
1. **Make minimal changes** - Don't refactor unrelated code
2. **Preserve behavior** - Output must be identical
3. **Add comments** - Explain optimization rationale
4. **Keep original available** - User may want to compare

### Step 4.3: Verify Correctness

**MANDATORY after optimization:**
- [ ] Run existing tests
- [ ] Test with edge cases
- [ ] Compare outputs before/after
- [ ] Check for new bugs

---

## Phase 5: Complexity Verification

### Provide Final Report

```
优化完成报告

代码: [function/file name]

优化前:
- 时间复杂度: O(?)
- 空间复杂度: O(?)

优化后:
- 时间复杂度: O(?)
- 空间复杂度: O(?)
- 实际提升: [Expected improvement]

使用策略:
- [Strategy 1]
- [Strategy 2]

注意事项:
- [Any tradeoffs or caveats]
```

---

## Decision Tree for Autonomous Optimization

When user selects "自动判断" (auto-decide), follow this logic:

```
IF input_size < 100:
    → Prefer readability, minimal optimization
ELIF input_size < 10000:
    → Standard optimizations (hash maps, early exits)
ELIF input_size < 1000000:
    → Aggressive time optimization
ELSE:
    → Consider streaming, chunking, external algorithms

IF memory_constrained:
    → Prefer in-place, iterators, streaming
IF time_critical:
    → Prefer precomputation, caching, hash structures
```

---

## Common Optimization Patterns

### 1. O(n²) → O(n) via Hash Map

```python
# Before: O(n²)
for i in range(n):
    for j in range(n):
        if arr[i] + arr[j] == target:
            return (i, j)

# After: O(n)
seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        return (seen[target - num], i)
    seen[num] = i
```

### 2. O(n) → O(log n) via Binary Search

```python
# Before: O(n)
for i, val in enumerate(sorted_arr):
    if val == target:
        return i

# After: O(log n)
left, right = 0, len(sorted_arr) - 1
while left <= right:
    mid = (left + right) // 2
    if sorted_arr[mid] == target:
        return mid
    elif sorted_arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### 3. O(2ⁿ) → O(n) via Memoization

```python
# Before: O(2ⁿ)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# After: O(n)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### 4. Space O(n) → O(1) In-place

```python
# Before: O(n) space
result = arr[::-1]

# After: O(1) space
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why Bad | Fix |
|--------------|---------|-----|
| Premature optimization | Wastes time, harms readability | Profile first |
| String concat in loop | O(n²) due to copying | Use join/buffer |
| Copying large arrays | Wastes memory | Use references/views |
| Deep recursion | Stack overflow | Convert to iteration |
| Global state for caching | Thread safety issues | Use local cache |
| Over-engineering | Maintenance burden | Keep it simple |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────┐
│        COMPLEXITY OPTIMIZATION              │
├─────────────────────────────────────────────┤
│ TIME ↓                                      │
│   Nested loops    → Hash map / Set         │
│   Repeated calc   → Memoization            │
│   Linear search   → Binary search (sorted) │
│   Full scan       → Early exit             │
├─────────────────────────────────────────────┤
│ SPACE ↓                                     │
│   New arrays      → In-place modify        │
│   Full list       → Generator/Iterator     │
│   Deep recursion  → Iterative              │
│   Object copies   → References             │
├─────────────────────────────────────────────┤
│ BALANCED                                    │
│   Wrong data struct → Right data struct    │
│   Naive algorithm  → Optimal algorithm     │
└─────────────────────────────────────────────┘
```

---

## Example Workflow

**User**: "优化这段代码的代码优化"

```python
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates
```

**Agent Response**:
```
分析结果:
- 时间复杂度: O(n³) - 双重循环 O(n²) × not in 检查 O(n)
- 空间复杂度: O(n) - duplicates 数组
- 瓶颈: 嵌套循环 + 线性查找

优化方案建议:

1. 【优先时间】使用集合去重
   - 时间: O(n²) → O(n)
   - 空间: O(n) (增加一个集合)
   
2. 【平衡优化】使用 Counter
   - 时间: O(n)
   - 空间: O(n)
   
请选择优化方向，或让我自动判断？
```

---

## Integration Notes

- Works with `test-driven-debugging` skill for verifying optimizations
- Works with `safe-refactoring` skill for complex restructuring
- Use `code-review-guardian` skill after optimization for quality check

---

## Limitations

- Cannot optimize external library code
- Requires test coverage for safety
- Some optimizations are language-specific
- May not apply to all coding paradigms
