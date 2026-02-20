---
name: test-driven-debugging
description: Systematic debugging workflow for failing tests - understand intent, isolate cause, minimal fix
license: MIT
compatibility: opencode
---

# Test-Driven Debugging

Fix failing tests systematically, not randomly.

## When to Use

- Any test is failing
- CI/CD pipeline is red
- After making changes that broke existing tests

---

## The Problem with Random Debugging

```
❌ Bad: See error → Guess cause → Random fix → Hope it works
✅ Good: See error → Understand test → Isolate cause → Minimal fix
```

Random debugging wastes time and often introduces new bugs.

---

## Debugging Protocol

### Phase 1: Understand the Test (READ FIRST)

**Before touching any code, answer these questions:**

```markdown
## Test Analysis

### What is this test testing?
[Describe the feature/behavior being tested in 1 sentence]

### What is the expected behavior?
[What should happen according to the test]

### What is the actual behavior?
[What's actually happening - from error message]

### What assertion failed?
[The specific line/assertion that failed]
```

**Action:** Read the test file completely. Do not skip this step.

---

### Phase 2: Reproduce and Isolate

**Run the test in isolation:**

```bash
# Run only the failing test
npm test -- --grep "test name pattern"

# Or for specific file
npm test -- path/to/failing.test.ts
```

**Isolation checklist:**

- [ ] Does it fail in isolation (not just in full suite)?
- [ ] Does it fail consistently (not flaky)?
- [ ] What's the exact error message and stack trace?

---

### Phase 3: Form Hypotheses

**Create a debugging log:**

```markdown
## Debugging Log

| # | Hypothesis | How to Verify | Result | Conclusion |
|---|------------|---------------|--------|------------|
| 1 | [guess 1] | [test approach] | ✓/✗ | [what you learned] |
| 2 | [guess 2] | [test approach] | ✓/✗ | [what you learned] |
| 3 | [guess 3] | [test approach] | ✓/✗ | [what you learned] |
```

**Hypothesis sources:**
- Error message/stack trace
- Recent code changes (git diff)
- Similar bugs you've seen before
- Dependencies that changed

---

### Phase 4: Binary Search (When Stuck)

If the cause isn't obvious, use binary search:

1. **Comment out half the test** - Does it still fail?
2. **If yes** - Problem is in the remaining half
3. **If no** - Problem is in the commented half
4. **Repeat** until you isolate the failing line

---

### Phase 5: Minimal Fix

**Fix principles:**

1. **Minimal change** - Fix only what's broken
2. **Preserve intent** - Don't change test expectations
3. **No refactoring** - Save that for a separate commit

**Before committing:**

```bash
# Run the specific test
npm test -- --grep "fixed test"

# Run related tests (same file or module)
npm test -- path/to/module/

# Run all tests (ensure no regression)
npm test
```

---

## Common Failure Patterns

### Pattern: "Expected X but got Y"

```
AssertionError: expected 5 to equal 3
```

**Likely causes:**
- Off-by-one error
- Wrong return value
- State not reset between tests

**Debug approach:** Print/log the actual value before assertion

---

### Pattern: "Cannot read property X of undefined"

```
TypeError: Cannot read property 'id' of undefined
```

**Likely causes:**
- Missing null check
- Async timing issue
- Mock not set up correctly

**Debug approach:** Trace back where the undefined value came from

---

### Pattern: "Timeout exceeded"

```
Error: Timeout of 5000ms exceeded
```

**Likely causes:**
- Async operation not completing
- Missing await
- Infinite loop

**Debug approach:** Add logging at each async step

---

### Pattern: "Mock not called"

```
Expected mock function to have been called, but it was not called
```

**Likely causes:**
- Mock not applied to correct module
- Function called with different parameters
- Import mocking issues

**Debug approach:** Log the actual calls made to the mock

---

## Anti-Patterns

### ❌ "I'll just comment out the test"
Result: Technical debt accumulates, real bugs hide

### ❌ "I'll fix it by changing the test expectation"
Result: Test passes but doesn't verify correct behavior

### ❌ "Let me refactor while I'm here"
Result: Introduces new bugs, obscures the real fix

### ❌ "The test is flaky, I'll skip it"
Result: Real issue never addressed

---

## Quick Reference

```
1. READ test → Understand what it's testing
2. RUN test → Isolate the failure
3. LOG hypotheses → Systematic investigation
4. FIX minimal → Smallest possible change
5. VERIFY all → No regressions
```

---

## Integration with AGENTS.md

Add to your project's AGENTS.md:

```markdown
## Debugging Workflow

When tests fail, load the test-driven-debugging skill and follow its protocol.
Never skip understanding the test before attempting fixes.
```
