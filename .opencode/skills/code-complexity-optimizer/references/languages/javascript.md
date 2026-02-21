# JavaScript/TypeScript Optimization Guide

## Anti-Patterns

| Anti-Pattern | Complexity | Solution |
|--------------|------------|----------|
| `array.push(...spread)` | O(n²) | `array.concat()` |
| `array.filter().map()` | 2× O(n) | Single `reduce()` |
| `for...in` on arrays | O(n) + prototype chain | `for...of` |
| Property access in hot loop | O(1) but slow | Cache in local variable |
| `JSON.parse(JSON.stringify())` | O(n) + GC | Structured clone or manual |
| `delete` on array | O(n) shift | Use `splice` or object |

## Optimization Patterns

### Array Method Chaining

```javascript
// Before: 2 passes over array
const result = arr.filter(x => x > 0).map(x => x * 2);

// After: 1 pass (if performance critical)
const result = arr.reduce((acc, x) => 
  x > 0 ? [...acc, x * 2] : acc, []);

// Or: Direct loop (fastest for large arrays)
const result = [];
for (const x of arr) {
  if (x > 0) result.push(x * 2);
}
```

### Object Lookups

```javascript
// Before: O(n) search
const found = users.find(u => u.id === targetId);

// After: O(1) with Map
const userMap = new Map(users.map(u => [u.id, u]));
const found = userMap.get(targetId);
```

### Spread Operator

```javascript
// Before: Creates new array each time
const newArr = [...arr, newItem]; // O(n)

// After: For building large arrays
const newArr = arr.slice();
newArr.push(newItem);

// Or use push directly if original can be modified
arr.push(newItem); // O(1) amortized
```

### Object Spread vs Object.assign

```javascript
// Both are O(n) for properties
const merged = { ...obj1, ...obj2 };
const merged = Object.assign({}, obj1, obj2);

// For hot paths, direct assignment is faster
const merged = {};
for (const key in obj1) merged[key] = obj1[key];
for (const key in obj2) merged[key] = obj2[key];
```

### Set for Unique Values

```javascript
// Before: O(n²)
const unique = arr.filter((x, i) => arr.indexOf(x) === i);

// After: O(n)
const unique = [...new Set(arr)];
```

### Avoid Re-renders (React)

```javascript
// Before: New function on every render
<button onClick={() => handleClick(id)}>

// After: Stable reference
const handleClick = useCallback((id) => {...}, [deps]);
<button onClick={() => handleClick(id)}>

// Best: Pass id directly
const handleClick = useCallback((e) => {
  const id = e.currentTarget.dataset.id;
}, []);
<button data-id={id} onClick={handleClick}>
```

## TypeScript-Specific

| Issue | Impact | Solution |
|-------|--------|----------|
| `any` type | No compile-time optimization | Use specific types |
| Runtime type checks | O(n) for complex types | Use type guards |
| Enum to const | Extra runtime code | Use `const` objects |
