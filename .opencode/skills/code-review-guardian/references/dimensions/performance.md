# Performance Review Guide

Identify and resolve performance bottlenecks - database queries, memory usage, algorithmic efficiency.

---

## Common Performance Issues

| Issue | Pattern | Detection |
|-------|---------|-----------|
| N+1 Queries | Query in loop | Look for `for...await` |
| Memory Leak | Unclosed resources | Missing `finally` or cleanup |
| Unnecessary Work | Redundant calculations | Duplicate function calls |
| Large Payloads | Too much data | Check response size |
| Blocking I/O | Sync operations | `readFileSync`, `execSync` |
| Unoptimized Loops | O(n²) in hot paths | Nested loops |

---

## Database Performance

### N+1 Query Problem

**❌ N+1 Query:**
```javascript
// For 100 users, this executes 101 queries!
for (const user of users) {
  const posts = await db.query(
    `SELECT * FROM posts WHERE user_id = ?`, 
    [user.id]
  )
  user.posts = posts
}
```

**✅ Batch Query:**
```javascript
// Only 2 queries total
const userIds = users.map(u => u.id)
const posts = await db.query(
  `SELECT * FROM posts WHERE user_id IN (?)`, 
  [userIds]
)

// Group posts by user
const postsByUser = posts.reduce((acc, post) => {
  (acc[post.user_id] ||= []).push(post)
  return acc
}, {})

users.forEach(user => {
  user.posts = postsByUser[user.id] || []
})
```

---

### Missing Index

**❌ Slow Query:**
```sql
SELECT * FROM orders WHERE created_at > '2024-01-01'
```

**✅ With Index:**
```sql
CREATE INDEX idx_orders_created_at ON orders(created_at);
```

---

## Memory Performance

### Memory Leaks

**❌ Common Leak Patterns:**
```javascript
// 1. Event listeners not removed
component.on('data', handler)
// Never removed!

// 2. Closures holding references
const cache = {}
function process(data) {
  const key = computeKey(data)
  cache[key] = { data, timestamp: Date.now() }
  // cache grows unbounded!
}

// 3. Global variables
window.someCache = hugeData
```

**✅ Proper Cleanup:**
```javascript
// 1. Cleanup in useEffect
useEffect(() => {
  component.on('data', handler)
  return () => component.off('data', handler) // Clean up!
}, [])

// 2. Bounded cache
const cache = new LRUCache(100)
function process(data) {
  cache.set(computeKey(data), data)
}

// 3. Weak references
const cache = new WeakMap()
```

---

### Large Data Handling

**❌ Load Everything:**
```javascript
const allUsers = await db.query('SELECT * FROM users')
// Memory explodes with millions of rows
```

**✅ Streaming/Pagination:**
```javascript
// Use cursor-based pagination
async function* streamUsers(batchSize = 1000) {
  let cursor = null
  while (true) {
    const { users, nextCursor } = await db.query(
      'SELECT * FROM users LIMIT ? OFFSET ?',
      [batchSize, cursor]
    )
    yield users
    if (!nextCursor) break
    cursor = nextCursor
  }
}

// Or streaming
for await (const chunk of streamUsers()) {
  processChunk(chunk)
}
```

---

## Algorithmic Performance

### Time Complexity

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2^n) | Exponential | Recursive Fibonacci |

**Optimization Examples:**

| Original | Optimized | Complexity |
|----------|-----------|------------|
| Nested loops for search | Hash map lookup | O(n²) → O(n) |
| Linear search | Binary search | O(n) → O(log n) |
| Recalculate in loop | Memoization | O(n) → O(1) |

---

## Async Performance

### Blocking Operations

**❌ Blocking:**
```javascript
const data = fs.readFileSync('file.txt')  // Blocks event loop
const result = execSync('npm build')       // Blocks event loop
```

**✅ Non-blocking:**
```javascript
const data = await fs.promises.readFile('file.txt')
const result = await exec('npm build')    // With timeout!
```

---

## Performance Checklist

- [ ] No N+1 queries
- [ ] No unnecessary loops
- [ ] Resources properly released
- [ ] Caching considered for hot paths
- [ ] Database queries use indexes
- [ ] Pagination for large lists
- [ ] Lazy loading where appropriate
- [ ] Async/await not blocking
- [ ] No memory leaks
- [ ] Appropriate data structures used
- [ ] Compression for large responses
- [ ] CDN for static assets
