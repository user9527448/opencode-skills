---
name: test-driven-debugging
description: Four-phase systematic debugging methodology - root cause investigation, pattern analysis, hypothesis testing, minimal fix implementation
license: MIT
compatibility: opencode
---

# Test-Driven Debugging

**Core Principle: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.**

Never apply symptom-focused patches. Understand WHY something fails before attempting to fix it.

---

## 🚨 When to Activate This Skill

| Trigger | Priority |
|---------|----------|
| Any test failure | HIGH |
| CI/CD pipeline red | HIGH |
| "Works on my machine" issues | MEDIUM |
| Flaky test detection | MEDIUM |
| Regression after changes | HIGH |

---

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST

If you haven't completed Phase 1, you cannot propose fixes.
Violating this is violating the spirit of debugging.
```

---

## Phase 1: Root Cause Investigation

**Before touching any code:**

### Step 1.1: Read Error Messages Thoroughly

Every word in an error message matters. Do not skip.

```markdown
## Error Analysis Template

### Full Error Message
[Copy the COMPLETE error message, not a summary]

### Stack Trace Analysis
- Top of stack: [Where error manifested]
- Bottom of stack: [Where error originated]
- Key frames: [Important intermediate calls]

### Error Type Classification
[ ] TypeError - Wrong type/null/undefined
[ ] ReferenceError - Variable not found
[ ] SyntaxError - Code won't parse
[ ] AssertionError - Test expectation failed
[ ] TimeoutError - Operation took too long
```

### Step 1.2: Reproduce Consistently

```bash
# Run the specific failing test
npm test -- --grep "exact test name"

# Run with verbose output
npm test -- --verbose --grep "test name"

# Run in isolation
npm test -- --runInBand --grep "test name"
```

**Reproduction Checklist:**
- [ ] Can I trigger it reliably?
- [ ] What are the exact steps?
- [ ] Does it fail locally AND in CI?
- [ ] Does it fail in isolation or only in full suite?

### Step 1.3: Examine Recent Changes

```bash
# What changed recently?
git log --oneline -20

# What changed in the failing file?
git log -p -- path/to/failing.test.ts

# Git bisect to find the breaking commit
git bisect start
git bisect bad HEAD
git bisect good <last-known-good-commit>
```

### Step 1.4: Gather Diagnostic Evidence

| Evidence Type | How to Collect |
|---------------|----------------|
| Screenshots | CI artifacts, local capture |
| Console logs | `console.log` or debugger |
| Network requests | DevTools Network tab |
| Database state | Query before/after test |

---

## Phase 2: Pattern Analysis

### Step 2.1: Locate Working Examples

| Aspect | Working Code | Failing Code | Difference |
|--------|--------------|--------------|------------|
| Input | [value] | [value] | [diff] |
| State | [value] | [value] | [diff] |
| Timing | [value] | [value] | [diff] |

### Step 2.2: Test Failure Pattern Library

| Pattern | Likely Cause | Quick Check |
|---------|--------------|-------------|
| `Expected X but got Y` | Off-by-one, wrong return | Print actual value |
| `Cannot read property 'x' of undefined` | Missing null check, async timing | Trace undefined source |
| `Timeout exceeded` | Async not completing, infinite loop | Log each async step |
| `Mock not called` | Wrong module, different params | Log actual mock calls |
| `Element not found` | UI changed, selector outdated | Check screenshot |
| `Works locally, fails CI` | Environment difference | Compare environments |

---

## Phase 3: Hypothesis Testing

### Hypothesis Template

```markdown
### Hypothesis #1
**Statement:** "The error occurs because [specific reason]"
**Test:** [How to verify - minimal test]
**Expected if true:** [What we'd see]
**Result:** [CONFIRMED / DISPROVEN]
**New information:** [What we learned]
```

### Rules for Hypothesis Testing

1. Test ONE hypothesis at a time
2. Make minimal changes to test
3. Document results before moving on
4. If hypothesis fails, update understanding

### Debugging Log

| # | Hypothesis | Test Method | Result | Conclusion |
|---|------------|-------------|--------|------------|
| 1 | [guess] | [how] | ✓/✗ | [learned] |
| 2 | [guess] | [how] | ✓/✗ | [learned] |

---

## Phase 4: Implementation

### Step 4.1: Create Failing Test Case

```javascript
// Before fixing, capture the bug behavior
it('should handle null input correctly', () => {
  const result = processInput(null);
  expect(result).toBeDefined(); // Currently throws
});
```

### Step 4.2: Implement Minimal Fix

- Change only what's necessary
- Preserve all existing behavior
- No refactoring during fix

### Step 4.3: Verify

```bash
npm test -- --grep "fixed test"  # Specific
npm test -- path/to/module/      # Related
npm test                          # Full suite
```

---

## 🛑 Red Flags - Stop Immediately

| Thought | Reality | Action |
|---------|---------|--------|
| "Let me just try this fix" | Guessing | STOP → Do Phase 1 |
| "Maybe if I increase timeout" | Masking symptom | Find root cause |
| "It's probably just flaky" | Assumption | Investigate why |
| "I'll fix it and test later" | Risky | Test after EVERY change |

---

## Three-Strike Rule

```
If THREE consecutive fixes fail:

STOP. This signals:
- Wrong hypothesis
- Architectural problem
- Missing information

Action:
1. Revert all changes
2. Gather more evidence
3. Consult another engineer
```

---

## Quick Reference

```
PHASE 1: ROOT CAUSE
□ Read FULL error message
□ Reproduce consistently
□ Check recent changes
□ Gather evidence

PHASE 2: PATTERN
□ Find working examples
□ Compare vs failing
□ Match pattern library

PHASE 3: HYPOTHESIS
□ Form ONE hypothesis
□ Test minimally
□ Document result

PHASE 4: IMPLEMENT
□ Create failing test
□ Minimal fix
□ Verify all tests
```
