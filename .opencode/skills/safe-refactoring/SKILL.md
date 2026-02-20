---
name: safe-refactoring
description: Systematic refactoring protocol - small steps, verified changes, always reversible
license: MIT
compatibility: opencode
---

# Safe Refactoring

Refactor without fear. Small steps, verified at each stage.

## When to Use

- Improving code structure without changing behavior
- Reducing technical debt
- Preparing code for new features
- Simplifying complex code

---

## The Problem with Big Bang Refactoring

```
❌ Bad: Rewrite everything → Tests fail → Can't find what broke → Give up
✅ Good: Small change → Verify → Commit → Repeat
```

Large refactorings fail because they're hard to verify and hard to rollback.

---

## Core Principles

### 1. 🟢 Green Before You Start

**Never refactor red tests.**

```bash
# Before any refactoring
npm test  # Must pass completely
```

If tests are failing, fix bugs first. Refactoring is for working code.

---

### 2. 📏 Small Steps

**Each refactoring step should be:**

- Completable in <15 minutes
- Independently verifiable
- Easy to rollback

```
❌ Bad: "Refactor entire authentication module"
✅ Good: "Extract password validation into separate function"
```

---

### 3. ✅ Verify After Each Step

**After every change:**

```bash
# 1. Run tests
npm test

# 2. Type check (if TypeScript)
npm run typecheck

# 3. Lint
npm run lint
```

**If anything fails:** Stop and fix before continuing.

---

### 4. 💾 Commit Frequently

**After each successful verification:**

```bash
git add .
git commit -m "refactor: [describe single change]"
```

This creates rollback points. You can always `git revert` if needed.

---

## Refactoring Catalog

### Extract Function

**When:** Code block has a clear purpose

**Before:**
```javascript
function processOrder(order) {
  // validate order
  if (!order.items || order.items.length === 0) {
    throw new Error('Empty order');
  }
  if (!order.customer) {
    throw new Error('No customer');
  }
  
  // ... rest of function
}
```

**After:**
```javascript
function processOrder(order) {
  validateOrder(order);
  // ... rest of function
}

function validateOrder(order) {
  if (!order.items || order.items.length === 0) {
    throw new Error('Empty order');
  }
  if (!order.customer) {
    throw new Error('No customer');
  }
}
```

**Verification:** Tests still pass (behavior unchanged)

---

### Rename Variable/Function

**When:** Name doesn't communicate intent

**Before:**
```javascript
const d = new Date();
const temp = users.filter(u => u.active);
```

**After:**
```javascript
const currentDate = new Date();
const activeUsers = users.filter(user => user.isActive);
```

**Verification:** Tests + type check (rename should not break types)

---

### Extract Constant/Magic Number

**When:** Numbers/strings appear without explanation

**Before:**
```javascript
if (user.age >= 18) { /* ... */ }
setTimeout(callback, 30000);
```

**After:**
```javascript
const LEGAL_AGE = 18;
const SESSION_TIMEOUT_MS = 30000;

if (user.age >= LEGAL_AGE) { /* ... */ }
setTimeout(callback, SESSION_TIMEOUT_MS);
```

**Verification:** Tests pass

---

### Simplify Conditional

**When:** Complex boolean logic

**Before:**
```javascript
if (user && user.isActive && !user.isBanned && user.hasPermission('write')) {
  // ...
}
```

**After:**
```javascript
function canWrite(user) {
  return user?.isActive 
    && !user.isBanned 
    && user.hasPermission('write');
}

if (canWrite(user)) {
  // ...
}
```

**Verification:** Tests for the conditional path pass

---

### Remove Dead Code

**When:** Code is unused

**Steps:**
1. Search for all usages
2. If none found, delete
3. Verify tests pass

**Warning:** Be careful with:
- Public APIs (might be used externally)
- Reflection/dynamic calls
- Event handlers

**Verification:** Full test suite + manual check for edge cases

---

## Refactoring Workflow

### Phase 1: Prepare

```markdown
## Pre-Refactor Checklist

- [ ] All tests pass (green)
- [ ] No uncommitted changes
- [ ] Branch is up to date
- [ ] I understand what the code does
- [ ] I have tests covering this area
```

### Phase 2: Plan

```markdown
## Refactoring Plan

### Goal
[What I want to improve]

### Steps
1. [Step 1 - small, verifiable]
2. [Step 2 - small, verifiable]
3. [Step 3 - small, verifiable]

### Verification
- [Which tests to run]
- [Any manual checks needed]
```

### Phase 3: Execute

```
For each step:
  1. Make change
  2. Run tests
  3. If pass → commit
  4. If fail → fix or rollback
```

### Phase 4: Verify

```bash
# Full verification
npm test
npm run lint
npm run typecheck

# If CI exists
git push  # Let CI verify
```

---

## Verification Checklist

After refactoring:

- [ ] All tests pass
- [ ] No type errors (TypeScript)
- [ ] No lint errors
- [ ] Behavior unchanged (same outputs for same inputs)
- [ ] No dead code introduced
- [ ] Documentation updated if public API changed

---

## Common Pitfalls

### ❌ "I'll just quickly refactor this while I'm here"

**Problem:** Scope creep, mixing refactoring with feature changes

**Fix:** Separate commits for refactoring vs features

---

### ❌ "Tests slow me down, I'll run them at the end"

**Problem:** Hard to isolate which change broke things

**Fix:** Run tests after every change

---

### ❌ "This is simple, I don't need to commit yet"

**Problem:** Lose rollback point if something goes wrong

**Fix:** Commit after every verified change

---

### ❌ "I'll clean up tests later"

**Problem:** Refactoring without test coverage is dangerous

**Fix:** Add tests before refactoring if coverage is low

---

## Rollback Strategy

If something goes wrong:

### Immediate Rollback (uncommitted changes)
```bash
git checkout -- .
git clean -fd
```

### Last Commit Rollback
```bash
git revert HEAD
```

### Find When It Broke
```bash
git bisect start
git bisect bad HEAD
git bisect good <last-known-good-commit>
# Git will binary search to find the breaking commit
```

---

## Quick Reference

```
🟢 GREEN    → Tests must pass before starting
📏 SMALL    → One tiny change at a time
✅ VERIFY   → Run tests after each change
💾 COMMIT   → Checkpoint frequently
🔄 REPEAT   → Continue until done
```

---

## Integration with AGENTS.md

```markdown
## Refactoring Protocol

When refactoring code:
1. Load the safe-refactoring skill
2. Ensure tests are green before starting
3. Make small, verifiable changes
4. Run tests after each change
5. Commit frequently
```
