# Go Optimization Guide

## Anti-Patterns

| Anti-Pattern | Complexity | Solution |
|--------------|------------|----------|
| `append` without capacity | O(n) reallocations | `make([]T, 0, cap)` |
| `interface{}` overhead | Type assertion | Generics (Go 1.18+) |
| `fmt.Sprintf` in hot path | Reflection | `strconv` functions |
| Map without size hint | Rehashing | `make(map[K]V, hint)` |
| String concat in loop | O(n²) | `strings.Builder` |
| Copying large structs | O(size) | Use pointers |

## Optimization Patterns

### Slice Pre-allocation

```go
// Before: Multiple reallocations
var result []int
for i := 0; i < 1000000; i++ {
    result = append(result, i)
}

// After: Single allocation
result := make([]int, 0, 1000000)
for i := 0; i < 1000000; i++ {
    result = append(result, i)
}
```

### Map Pre-allocation

```go
// Before: May rehash multiple times
m := make(map[string]int)
for i := 0; i < 1000000; i++ {
    m[fmt.Sprintf("key%d", i)] = i
}

// After: Pre-sized map
m := make(map[string]int, 1000000)
for i := 0; i < 1000000; i++ {
    m[fmt.Sprintf("key%d", i)] = i
}
```

### String Building

```go
import "strings"

// Before: O(n²) - creates new string each time
var result string
for _, s := range parts {
    result += s
}

// After: O(n) with strings.Builder
var sb strings.Builder
sb.Grow(totalSize) // Optional: pre-allocate
for _, s := range parts {
    sb.WriteString(s)
}
result := sb.String()
```

### strconv vs fmt

```go
// Before: Uses reflection
s := fmt.Sprintf("%d", n)

// After: Direct conversion (faster)
s := strconv.Itoa(n)

// For floats
s := strconv.FormatFloat(f, 'f', -1, 64)
```

### Avoid Interface Overhead

```go
// Before: Interface overhead
func process(items []interface{}) {
    for _, item := range items {
        if s, ok := item.(string); ok {
            // ...
        }
    }
}

// After: Use generics (Go 1.18+)
func process[T any](items []T) {
    for _, item := range items {
        // Direct access, no type assertion
    }
}
```

### Sync.Pool for Reuse

```go
var bufferPool = sync.Pool{
    New: func() interface{} {
        return new(bytes.Buffer)
    },
}

func process() {
    buf := bufferPool.Get().(*bytes.Buffer)
    defer func() {
        buf.Reset()
        bufferPool.Put(buf)
    }()
    
    // Use buffer...
}
```

### Slice Tricks

```go
// Filter in-place (O(n))
filtered := items[:0]
for _, item := range items {
    if keep(item) {
        filtered = append(filtered, item)
    }
}

// Clear but keep capacity
items = items[:0]

// Copy slice
newSlice := make([]T, len(old))
copy(newSlice, old)
```
