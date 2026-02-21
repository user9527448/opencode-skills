# Java Optimization Guide

## Anti-Patterns

| Anti-Pattern | Complexity | Solution |
|--------------|------------|----------|
| `String +=` in loop | O(n²) | `StringBuilder` |
| `ArrayList.contains()` | O(n) | `HashSet.contains()` → O(1) |
| Boxing primitives | O(1) + GC | Use primitive collections |
| `LinkedList` random access | O(n) | `ArrayList` → O(1) |
| Unnecessary synchronization | Lock overhead | Use concurrent collections |
| Creating objects in loops | GC pressure | Reuse or pool objects |

## Optimization Patterns

### String Building

```java
// Before: O(n²) - creates new String each time
String result = "";
for (String item : items) {
    result += item;
}

// After: O(n) with StringBuilder
StringBuilder sb = new StringBuilder();
for (String item : items) {
    sb.append(item);
}
String result = sb.toString();
```

### Collection Selection

| Operation | ArrayList | LinkedList | HashSet | TreeSet |
|-----------|-----------|------------|---------|---------|
| Get by index | O(1) | O(n) | - | - |
| Add at end | O(1)* | O(1) | O(1) | O(log n) |
| Contains | O(n) | O(n) | O(1) | O(log n) |
| Remove | O(n) | O(n) | O(1) | O(log n) |
| Iteration | O(n) | O(n) | O(n) | O(n) |

### Map Selection

| Map Type | Get | Put | Remove | Ordered |
|----------|-----|-----|--------|---------|
| HashMap | O(1) | O(1) | O(1) | No |
| LinkedHashMap | O(1) | O(1) | O(1) | Insertion |
| TreeMap | O(log n) | O(log n) | O(log n) | Sorted |
| ConcurrentHashMap | O(1) | O(1) | O(1) | No (thread-safe) |

### Primitive Collections

```java
// Before: Boxing overhead
List<Integer> list = new ArrayList<>();
for (int i = 0; i < 1000000; i++) {
    list.add(i); // Boxes int to Integer
}

// After: Use primitive collections (Trove, Eclipse Collections, etc.)
IntArrayList list = new IntArrayList();
for (int i = 0; i < 1000000; i++) {
    list.add(i); // No boxing
}
```

### Stream vs Loop

```java
// Stream (readable but slightly slower)
long count = list.stream()
    .filter(x -> x > 0)
    .count();

// Traditional loop (faster for hot paths)
int count = 0;
for (int x : list) {
    if (x > 0) count++;
}
```

### Object Pooling

```java
// For expensive objects (connections, threads, etc.)
ObjectPool<ExpensiveObject> pool = new GenericObjectPool<>(
    new ExpensiveObjectFactory()
);

ExpensiveObject obj = pool.borrowObject();
try {
    obj.doWork();
} finally {
    pool.returnObject(obj);
}
```
