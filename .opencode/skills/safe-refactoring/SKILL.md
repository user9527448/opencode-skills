---
name: safe-refactoring
description: Systematic refactoring protocol - small steps, verified changes, always reversible, behavior-preserving
license: MIT
compatibility: opencode
---

# Safe Refactoring

Refactor without fear. Small steps, each verified.

---

## 🚨 When to Activate This Skill

| Trigger | Priority |
|---------|----------|
| Improving code structure | HIGH |
| Reducing technical debt | HIGH |
| Preparing for new feature | MEDIUM |
| Simplifying complex code | MEDIUM |
| After understanding legacy code | HIGH |

---

## The Iron Law

```
REFACTORING = Behavior-Preserving Transformation

If behavior changes, it's NOT refactoring - it's rewriting.
```

---

## Core Principles

### 1. 🟢 GREEN Before You Start

```bash
# BEFORE any refactoring
npm test  # MUST pass completely

# If tests fail, FIX BUGS FIRST
# Refactoring is for WORKING code
```

### 2. 📏 Small Steps Only

**Each step should be:**
- Completable in <15 minutes
- Independently verifiable
- Easy to rollback

```
❌ "Refactor entire authentication module"
✅ "Extract password validation into separate function"
```

### 3. ✅ Verify After Each Step

```bash
# After EVERY change
npm test        # Tests pass?
npm run lint    # No new warnings?
npm run build   # Compiles?
```

### 4. 💾 Commit Frequently

```bash
# After each successful verification
git add .
git commit -m "refactor: [describe single change]"

# Creates rollback points
```

---

## Refactoring Workflow

### Phase 1: Prepare

```markdown
## Pre-Refactor Checklist

- [ ] All tests pass (GREEN)
- [ ] No uncommitted changes
- [ ] Branch is clean
- [ ] I understand what the code does
- [ ] Tests exist for this area
```

### Phase 2: Plan

```markdown
## Refactoring Plan

### Goal
[What I want to improve - ONE thing]

### Steps
1. [Step 1 - <15 min, verifiable]
2. [Step 2 - <15 min, verifiable]
3. [Step 3 - <15 min, verifiable]

### Verification
- [Which tests to run]
- [Any manual checks needed]
```

### Phase 3: Execute (Loop)

```
For each step:
  1. Make ONE small change
  2. Run tests
  3. If GREEN → Commit
  4. If RED → Fix or ROLLBACK immediately
  5. Repeat until step complete
```

### Phase 4: Verify

```bash
# Full verification
npm test
npm run lint
npm run build
npm run typecheck  # TypeScript

# Let CI verify
git push
```

---

## Refactoring Catalog

### Extract Function

**When:** Code block has clear purpose

**Before:**
```javascript
function processOrder(order) {
  // 20 lines of validation
  if (!order.items || order.items.length === 0) {
    throw new Error('Empty order');
  }
  // ... more validation ...
  
  // Actual processing
}
```

**After:**
```javascript
function processOrder(order) {
  validateOrder(order);
  // Actual processing
}

function validateOrder(order) {
  if (!order.items || order.items.length === 0) {
    throw new Error('Empty order');
  }
  // ... validation logic ...
}
```

**Verify:** Tests still pass

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

**Verify:** Tests + type check

---

### Extract Constant

**When:** Magic numbers appear

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

**Verify:** Tests pass

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

**Verify:** Tests for conditional path

---

### Remove Dead Code

**When:** Code is unused

**Steps:**
1. Search for all usages
2. If truly none, delete
3. Verify tests pass

**Warning:** Be careful with:
- Public APIs (may be external)
- Event handlers
- Reflection/dynamic calls

---

## Local Refactorings (Safest)

These affect only ONE file:

| Refactoring | Risk | Time |
|-------------|------|------|
| Rename variable | Low | 1 min |
| Extract function | Low | 5 min |
| Remove unused import | Low | 30 sec |
| Format code | None | 1 min |
| Extract constant | Low | 2 min |
| Simplify if | Low | 3 min |

---

## Red Flags - Stop Immediately

| Thought | Reality | Action |
|---------|---------|--------|
| "I'll just quickly refactor this too" | Scope creep | STOP → One change only |
| "Tests slow me down" | Risky | Run tests after EVERY change |
| "This is simple, no commit needed" | No rollback | Commit after each step |
| "I'll clean up tests later" | Dangerous | Tests MUST pass first |

---

## Rollback Strategy

### Uncommitted Changes
```bash
git checkout -- .
git clean -fd
```

### Last Commit
```bash
git revert HEAD
```

### Find Breaking Commit
```bash
git bisect start
git bisect bad HEAD
git bisect good <last-good-commit>
# Git binary searches to find the problem
```

---

## Baby Steps Example

**Goal:** Extract user validation

```
Step 1: Create empty validateUser() function
        → Run tests → GREEN → Commit

Step 2: Copy validation logic to new function
        → Run tests → GREEN → Commit

Step 3: Call new function, keep old code
        → Run tests → GREEN → Commit

Step 4: Remove old validation code
        → Run tests → GREEN → Commit

Step 5: Remove temporary duplication
        → Run tests → GREEN → Commit
```

Each step: <5 minutes, easily rollbackable.

---

## Quick Reference

```
🟢 GREEN    → Tests MUST pass before starting
📏 SMALL    → One tiny change at a time
✅ VERIFY   → Run tests after each change
💾 COMMIT   → Checkpoint frequently
🔄 REPEAT   → Continue until done

NEVER:
- Skip running tests
- Make multiple changes at once
- Refactor without commits
- Continue after RED test
```
