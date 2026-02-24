# Error Analysis Worksheet

Systematic error analysis template for root cause investigation.

---

## Error Details

### Full Error Message

```
[Paste complete error - no truncation]
```

### Stack Trace

```
[Paste full stack trace]
```

### Error Classification

| Category | Type | Checked |
|----------|------|---------|
| **Type Errors** | | |
| | TypeError | [ ] |
| | ReferenceError | [ ] |
| | SyntaxError | [ ] |
| | RangeError | [ ] |
| **Async Errors** | | |
| | TimeoutError | [ ] |
| | Promise never resolved | [ ] |
| | Unhandled rejection | [ ] |
| **Test Errors** | | |
| | AssertionError | [ ] |
| | Expect mismatch | [ ] |
| **Environment** | | |
| | Module not found | [ ] |
| | Permission denied | [ ] |
| **Network** | | |
| | Connection refused | [ ] |
| | Timeout | [ ] |

---

## Reproduction

### Can reproduce?

- [ ] Yes, 100% reliable
- [ ] Sometimes (~50%)
- [ ] Rarely (<10%)
- [ ] Never reproduced

### Reproduction Steps

1. 
2. 
3. 

### Environment

| Variable | Value |
|----------|-------|
| Node version | |
| npm version | |
| OS | |
| Memory | |
| CPU | |

---

## Code Context

### File(s) Involved

- 
- 

### Recent Changes (git)

```bash
git log --oneline -5 -- [file]
```

### Variables at Failure Point

| Variable | Value | Expected |
|----------|-------|----------|
| | | |
| | | |
| | | |

---

## Analysis

### What happened? (Symptom)

```
[Describe what you observed]
```

### What should have happened?

```
[Describe expected behavior]
```

### Root Cause Hypothesis

```
[Your best guess]
```

### Evidence supporting

- 
- 

---

## Investigation Plan

### Step 1: [ ]

**Action:** 
**Expected:**
**Result:**

### Step 2: [ ]

**Action:** 
**Expected:**
**Result:**

### Step 3: [ ]

**Action:** 
**Expected:**
**Result:**

---

## Resolution

### Root Cause Found

```
[Actual root cause]
```

### Fix Applied

```javascript
[Code change]
```

### Verification

| Test | Result |
|------|--------|
| Unit tests | ✓ / ✗ |
| Coverage | ✓ / ✗ |
| Full suite | ✓ / ✗ |

### Lessons Learned

- 
- 
