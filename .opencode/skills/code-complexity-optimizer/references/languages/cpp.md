# C/C++ Optimization Guide

## Anti-Patterns

| Anti-Pattern | Complexity | Solution |
|--------------|------------|----------|
| `std::vector::push_back` unreserved | O(n) reallocations | `reserve()` upfront |
| `std::list` for iteration | Cache misses | `std::vector` |
| `std::find` on vector | O(n) | Sorted vector + `binary_search` |
| Pass-by-value large objects | O(n) copy | Pass-by-reference |
| `std::map` for sequential access | O(log n) | `std::unordered_map` → O(1) |
| Iterator invalidation | Undefined behavior | Check validity rules |

## Optimization Patterns

### Vector Reservation

```cpp
// Before: Multiple reallocations
std::vector<int> vec;
for (int i = 0; i < 1000000; i++) {
    vec.push_back(i); // May reallocate multiple times
}

// After: Single allocation
std::vector<int> vec;
vec.reserve(1000000);
for (int i = 0; i < 1000000; i++) {
    vec.push_back(i); // No reallocation
}
```

### Container Selection

| Container | Random Access | Insert/Delete | Search | Memory |
|-----------|---------------|---------------|--------|--------|
| vector | O(1) | O(n) | O(n) | Contiguous |
| deque | O(1) | O(1) ends | O(n) | Segmented |
| list | O(n) | O(1) | O(n) | Node-based |
| set/map | - | O(log n) | O(log n) | Tree |
| unordered_set/map | - | O(1) avg | O(1) avg | Hash |

### Move Semantics

```cpp
// Before: Copy overhead
std::vector<BigObject> vec;
BigObject obj = createObject();
vec.push_back(obj); // Copies obj

// After: Move semantics
std::vector<BigObject> vec;
vec.push_back(createObject()); // Move, no copy
// Or explicitly
BigObject obj = createObject();
vec.push_back(std::move(obj));
```

### String Handling

```cpp
// Before: Multiple allocations
std::string result;
for (const auto& item : items) {
    result += item; // May reallocate
}

// After: Reserve or use string_view (C++17)
std::string result;
result.reserve(total_size);
for (const auto& item : items) {
    result += item;
}

// Or for read-only access (no allocation)
std::string_view view = large_string.substr(0, 100);
```

### Algorithm Selection

```cpp
#include <algorithm>

// Linear search: O(n)
auto it = std::find(vec.begin(), vec.end(), target);

// Binary search (sorted): O(log n)
bool found = std::binary_search(sorted_vec.begin(), sorted_vec.end(), target);

// Lower bound: O(log n)
auto it = std::lower_bound(sorted_vec.begin(), sorted_vec.end(), target);

// Sort + binary search is better for multiple searches
// O(n log n) + k * O(log n) vs k * O(n)
```

### Cache-Friendly Patterns

```cpp
// Before: Poor cache locality
struct Particle {
    float x, y, z;
    float vx, vy, vz;
};
std::vector<Particle> particles;

// After: Better cache locality (SoA)
struct ParticleSystem {
    std::vector<float> x, y, z;
    std::vector<float> vx, vy, vz;
};
// When only processing positions, cache loads only what's needed
```
