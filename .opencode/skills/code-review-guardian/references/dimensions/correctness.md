# Correctness Review Guide

Verify that the code works correctly - logic matches requirements, handles edge cases, and has proper error handling.

---

## Logic Verification

### Happy Path

| Check | Questions |
|-------|-----------|
| Main flow | Does the primary use case work end-to-end? |
| Input processing | Are valid inputs processed correctly? |
| Output format | Does the output match expected format? |
| State changes | Are all expected state changes applied? |

---

### Edge Cases

| Edge Case | What to Check |
|-----------|--------------|
| null | How does code handle null values? |
| undefined | What happens with undefined? |
| empty string | Empty vs null handling |
| empty array | Iteration over empty array |
| empty object | Property access on empty object |
| zero / negative | Boundary values for numbers |
| maximum values | Integer overflow, buffer limits |
| very long strings | Truncation, performance |
| special characters | Unicode, escape sequences |

---

### Error Handling

| Check | Questions |
|-------|-----------|
| Caught exceptions | Are all expected exceptions caught? |
| Error messages | Are errors descriptive and actionable? |
| Error propagation | Do errors bubble up correctly? |
| Recovery | Can the system recover from errors? |
| Logging | Are errors logged appropriately? |

---

## Error Handling Patterns

### ❌ Silent Failure

```javascript
// BAD: Swallows error, no indication of failure
try {
  await doSomething()
} catch (e) {
  // Do nothing
}

// BAD: Generic error message
if (error) {
  throw new Error("Error occurred")
}
```

**Why it's bad**: Silent failures are impossible to debug. Users don't know something went wrong.

---

### ✅ Proper Error Handling

```javascript
// GOOD: Descriptive error with context
try {
  await processUserData(userId)
} catch (error) {
  logger.error('Failed to process user data', {
    userId,
    error: error.message,
    stack: error.stack
  })
  
  throw new UserProcessingError(
    `Failed to process user ${userId}: ${error.message}`,
    { cause: error, userId }
  )
}

// GOOD: Custom error classes
class ValidationError extends Error {
  constructor(message, { field, value, ...options }) {
    super(message)
    this.name = 'ValidationError'
    this.field = field
    this.value = value
  }
}

class NotFoundError extends Error {
  constructor(resource, id) {
    super(`${resource} not found: ${id}`)
    this.name = 'NotFoundError'
    this.resource = resource
    this.id = id
  }
}
```

---

### Error Recovery Patterns

```javascript
// Retry with exponential backoff
async function withRetry(fn, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn()
    } catch (error) {
      if (i === maxRetries - 1) throw error
      const delay = Math.pow(2, i) * 1000
      await sleep(delay)
    }
  }
}

// Circuit breaker
class CircuitBreaker {
  constructor(threshold, timeout) {
    this.threshold = threshold
    this.timeout = timeout
    this.failures = 0
    this.state = 'CLOSED'
  }
  
  async call(fn) {
    if (this.state === 'OPEN') {
      throw new Error('Circuit open')
    }
    try {
      const result = await fn()
      this.state = 'CLOSED'
      this.failures = 0
      return result
    } catch (error) {
      this.failures++
      if (this.failures >= this.threshold) {
        this.state = 'OPEN'
        setTimeout(() => this.state = 'HALF', this.timeout)
      }
      throw error
    }
  }
}
```

---

## Correctness Checklist

- [ ] Logic matches requirements
- [ ] All branches reachable and tested
- [ ] Null/undefined handled
- [ ] Empty arrays/objects handled
- [ ] Boundary conditions checked
- [ ] Error messages helpful and specific
- [ ] No silent failures
- [ ] Type assertions avoid `as any`
- [ ] Async operations handle rejections
- [ ] Floating point comparisons account for precision
- [ ] Unicode handled correctly
- [ ] Time zones handled correctly

---

## Common Correctness Issues

| Issue | Detection | Fix |
|-------|-----------|-----|
| Off-by-one errors | Boundary testing | Use inclusive/exclusive clearly |
| Race conditions | Shared mutable state | Use locks/atomic operations |
| Integer overflow | Large number operations | Use BigInt or validate range |
| Null pointer | Null access | Optional chaining, null checks |
| Infinite loops | No exit condition | Verify loop terminates |

---

## Testing for Correctness

```python
# Example: Exhaustive edge case testing
def test_user_creation():
    # Valid input
    assert create_user("john", "john@example.com").name == "john"
    
    # Edge cases
    assert create_user("", "test@example.com") raises ValidationError
    assert create_user("john", "") raises ValidationError
    assert create_user(None, "test@example.com") raises ValidationError
    assert create_user("a" * 300, "test@example.com") raises ValidationError
    
    # Unicode
    assert create_user("约翰", "john@example.com").name == "约翰"
```
