# Concurrency Review Guide

Ensure code is thread-safe and handles concurrent operations correctly.

---

## Common Concurrency Issues

| Issue | Description | Detection |
|-------|-------------|-----------|
| Race Condition | Multiple threads access shared data | Shared mutable state |
| Deadlock | Circular wait for resources | Multiple locks |
| Livelock | Threads respond to each other endlessly | Complex sync logic |
| Starvation | Thread denied resources | Priority issues |

---

## Thread Safety Patterns

### ❌ Unsafe - Race Condition

```javascript
let counter = 0

async function increment() {
  const current = counter    // Read
  await someAsyncOp()        // Other threads may modify!
  counter = current + 1      // Write - stale value!
}
```

**Problem**: Between read and write, another thread can modify `counter`.

---

### ✅ Safe - Using Mutex

```javascript
import { Mutex } from 'async-mutex'

const mutex = new Mutex()
let counter = 0

async function increment() {
  await mutex.runExclusive(async () => {
    const current = counter
    await someAsyncOp()
    counter = current + 1
  })
}
```

---

### ❌ Unsafe - Shared State

```javascript
// Express handler with shared state - DANGEROUS
let requestCount = 0

app.get('/api/users', (req, res) => {
  requestCount++  // Race condition!
  // ...
})
```

**Problem**: Multiple requests can read/write `requestCount` simultaneously.

---

### ✅ Safe - Atomic Operations

```javascript
const { atomic } = require('w解剖d')

// Use atomic increment
app.get('/api/users', async (req, res) => {
  await atomic.incr('requestCount')
  // ...
})
```

**Or use proper locking:**
```javascript
const lock = new AsyncLock()

app.get('/api/users', async (req, res) => {
  await lock.acquire('users', async () => {
    // Only one request processes at a time
  })
})
```

---

## Deadlock Prevention

### ❌ Deadlock Prone

```javascript
async function transfer(from, to, amount) {
  await lockA.acquire()    // Holds lockA
  // ...
  await lockB.acquire()   // Waits for lockB
  // ...
}

// Another thread
async function reverseTransfer(from, to, amount) {
  await lockB.acquire()    // Holds lockB
  // ...
  await lockA.acquire()   // Waits for lockA - DEADLOCK!
}
```

---

### ✅ Deadlock-Free

```javascript
// Always acquire locks in the same order
async function transfer(from, to, amount) {
  const [first, second] = from.id < to.id 
    ? [lockA, lockB] 
    : [lockB, lockA]
  
  await first.acquire()
  try {
    await second.acquire()
    try {
      // Transfer logic
    } finally {
      second.release()
    }
  } finally {
    first.release()
  }
}
```

---

## Concurrency Checklist

- [ ] Shared state properly synchronized
- [ ] No race conditions
- [ ] Locks acquired in consistent order
- [ ] Timeouts on waits
- [ ] Immutable data preferred
- [ ] Atomic operations used correctly
- [ ] No deadlocks possible
- [ ] Thread pool sized correctly

---

## Best Practices

1. **Prefer immutability** - Immutable data needs no synchronization
2. **Minimize shared state** - Use message passing instead
3. **Use appropriate abstractions** - Actors, streams, workers
4. **Handle failures gracefully** - Timeouts, circuit breakers
5. **Test under load** - Race conditions often appear under concurrency
