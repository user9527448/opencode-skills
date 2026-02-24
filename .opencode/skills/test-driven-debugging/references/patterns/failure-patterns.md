# Failure Patterns Library

Comprehensive collection of common test failure patterns with root causes and debugging strategies.

## Type Errors

### TypeError: Cannot read property 'x' of undefined

**Likely Causes:**
- Accessing property before checking if object exists
- Async data not loaded yet
- Wrong variable in scope

**Debugging Steps:**
1. Find where variable is defined
2. Trace all paths that could lead to undefined
3. Add null checks or early returns
4. Verify with test case

---

### TypeError: 'x' is not a function

**Likely Causes:**
- Wrong object method binding
- Import/export mismatch
- Method name typo

**Debugging Steps:**
1. Check if method exists on object
2. Verify import is correct
3. Check `this` binding in method

---

### TypeError: Expected 'x' to be 'y'

**Likely Causes:**
- Wrong assertion
- Data transformation issue
- Type coercion problem

**Debugging Steps:**
1. Print actual value
2. Trace data flow
3. Check type coercion

---

## Async Errors

### TimeoutError: Async operation exceeded

**Likely Causes:**
- Promise never resolves
- Infinite loop
- Deadlock
- Network issue

**Debugging Steps:**
1. Add logging inside async operation
2. Check if promise ever resolves
3. Look for unhandled rejections
4. Verify timeout is reasonable

---

### Error: Mock 'x' was not called

**Likely Causes:**
- Different parameters than expected
- Wrong mock setup
- Code path not executed
- Async timing issue

**Debugging Steps:**
1. Log actual mock calls
2. Verify parameters match
3. Check if async/await missing

---

## Environment Errors

### "Works locally, fails in CI"

**Likely Causes:**
- Node version difference
- OS-specific behavior
- Environment variables
- Timing differences

**Debugging Steps:**
1. Compare Node versions
2. Check environment variables
3. Look for race conditions
4. Compare OS behavior

---

## Test Structure Errors

### Error: Cannot find module 'x'

**Likely Causes:**
- Missing dependency
- Wrong import path
- Case sensitivity (Linux)

**Debugging Steps:**
1. Check package.json
2. Verify file path
3. Check case sensitivity

---

### Error: Test timed out

**Likely Causes:**
- Infinite loop
- Never-resolving promise
- Too much work in test
- Resource contention

**Debugging Steps:**
1. Run test in isolation
2. Add debug logging
3. Check for infinite loops
4. Reduce test scope

---

## Flaky Test Patterns

### "Sometimes passes, sometimes fails"

**Likely Causes:**
- Race condition
- Shared state between tests
- Random data not seeded
- Timing dependency
- Network flakiness

**Debugging Steps:**
1. Run 10+ times
2. Check for shared state
3. Add delays
4. Seed random values

---

## Performance Errors

### Memory Leak

**Likely Causes:**
- Event listeners not removed
- Closures holding references
- Cached data growing unbounded

**Debugging Steps:**
1. Take heap snapshots
2. Compare snapshots
3. Look for growing objects

---

### Stack Overflow

**Likely Causes:**
- Infinite recursion
- Too deep call stack

**Debugging Steps:**
1. Check recursive base case
2. Reduce recursion depth
3. Convert to iteration

---

## Integration Errors

### Database Error

**Likely Causes:**
- Connection issue
- Query syntax error
- Migration not run
- Schema mismatch

**Debugging Steps:**
1. Check connection string
2. Run query manually
3. Verify migrations

---

### Network Error

**Likely Causes:**
- Service down
- Wrong URL
- CORS issue
- Auth expired

**Debugging Steps:**
1. Test endpoint manually
2. Check auth tokens
3. Look at CORS headers

---

## Pattern: Finding Root Cause

When you see an error, work backward:

```
1. What is the immediate failure? (symptom)
2. What code executed last? (point of failure)  
3. What should have been true? (assumption)
4. Why wasn't it true? (root cause)
```
