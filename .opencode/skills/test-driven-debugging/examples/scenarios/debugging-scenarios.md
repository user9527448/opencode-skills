# Debugging Scenarios

Real-world debugging examples demonstrating the systematic approach.

---

## Scenario 1: Async Race Condition

### The Problem
Tests sometimes pass, sometimes fail. Error: "Cannot read property 'id' of null"

### Investigation

**Phase 1: Root Cause**
- Error occurs randomly, not always
- Always on line where `user.id` is accessed
- Timing varies between runs

**Hypothesis:**
- Data fetching not complete when accessed

**Discovery:**
```javascript
// Code under test
async function getUserData() {
  const user = await fetchUser(); // Sometimes not awaited
  return user.id; // Fails when user is undefined
}
```

### The Fix
```javascript
async function getUserData() {
  const user = await fetchUser(); // Added await
  return user?.id ?? null; // Added optional chaining
}
```

### Verification
- Run 20 times → all pass
- Add delay test → still passes
- Coverage > 85%

---

## Scenario 2: Regression from Recent Change

### The Problem
Feature X worked yesterday, now broken. Error: "TypeError: Cannot read property 'map' of undefined"

### Investigation

**Phase 1: Git Archaeology**
```bash
git log --oneline -5 -- features/user-list.ts
# Find recent commits

git diff HEAD~3 features/user-list.ts
# Check what changed
```

**Discovery:**
- Commit "refactor: simplify data fetching" changed data structure
- Was: `data.items`
- Now: `data.results`

### The Fix
```javascript
// Updated to match new structure
const items = data.results || [];
```

### Verification
- Run related tests
- Check other places using same data
- Full suite passes

---

## Scenario 3: Environment-Specific Failure

### The Problem
Tests pass locally, fail in CI. Error: "ENOENT: no such file or directory"

### Investigation

**Phase 1: Compare Environments**
```bash
# Local
node --version  # v18.17.0
ls -la /path/  # exists

# CI  
node --version  # v16.20.0
ls -la /path/  # doesn't exist
```

**Discovery:**
- CI uses different Node version
- Path handling differs between versions
- File path constructed differently

### The Fix
```javascript
const path = require('path');
const basePath = process.cwd();
const configPath = path.resolve(basePath, 'config.json');
```

### Verification
- Test in Docker container matching CI
- Run in CI environment

---

## Scenario 4: Memory Leak in Long-Running Process

### The Problem
Process starts fine, slows down over hours. Eventually crashes.

### Investigation

**Phase 1: Heap Snapshots**
```javascript
// Add to code
const heapUsed = process.memoryUsage().heapUsed;
console.log(`Heap: ${Math.round(heapUsed / 1024 / 1024)}MB`);
```

**Observation:**
- Memory grows 10MB per 1000 requests
- Never decreases

**Discovery:**
- Event listeners accumulating
- Cache growing unbounded

### The Fix
```javascript
// Add cleanup
function cleanup() {
  emitter.removeAllListeners();
  cache.clear();
}
```

### Verification
- Run load test overnight
- Monitor heap over time
- Verify stable memory

---

## Scenario 5: Flaky Database Test

### The Problem
Database integration tests fail randomly. Error: "Unique constraint violation"

### Investigation

**Phase 1: Isolate**
- Run only DB tests → still flaky
- Run single test → passes sometimes

**Discovery:**
- Previous test doesn't clean up
- Database state persists
- ID sequence collides

### The Fix
```javascript
// Add cleanup
afterEach(async () => {
  await db.users.deleteMany({});
});
```

### Verification
- Run 10 times → all pass
- Run in parallel → all pass

---

## Scenario 6: Third-Party API Change

### The Problem
External API integration failing. Error: "Cannot read property 'data' of undefined"

### Investigation

**Phase 1: Check API**
```bash
curl https://api.example.com/v1/users
# Check response format
```

**Discovery:**
- API version changed
- Response structure different
- Breaking change without notice

### The Fix
```javascript
// Handle both formats
function parseResponse(response) {
  if (response.data) {
    return response.data;
  }
  // Handle legacy format
  return response;
}
```

### Verification
- Mock both responses
- Test in staging
- Add monitoring for API changes

---

## Key Takeaways

1. **Reproduce first** - Can't fix what you can't reproduce
2. **Isolate the case** - Smallest possible test case
3. **Check recent changes** - Git history is invaluable
4. **Compare environments** - CI vs local differences
5. **Think systematically** - Hypothesis → Test → Evidence
