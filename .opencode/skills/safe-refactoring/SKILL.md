---
name: safe-refactoring
description: Comprehensive refactoring protocol - small steps, verified changes, behavior-preserving, with code smells catalog
license: MIT
compatibility: opencode
metadata:
  references:
    catalog: references/catalog/
    smells: references/smells/
    examples: examples/
    templates: templates/
---

# Safe Refactoring

> Refactor without fear. Small steps, each verified. Always preserve behavior.

---

## 🚨 When to Activate This Skill

| Trigger | Priority | Notes |
|---------|----------|-------|
| Improving code structure | HIGH | When code is hard to understand |
| Reducing technical debt | HIGH | When code slows development |
| Preparing for new feature | MEDIUM | Before adding complex logic |
| Simplifying complex code | MEDIUM | Long methods, god classes |
| After understanding legacy code | HIGH | When legacy code is documented |

---

## The Iron Law

```
REFACTORING (n.): a change made to the internal structure of software
to make it easier to understand and cheaper to modify without
changing its observable behavior.

— Martin Fowler
```

**Core Principle:**
- ✅ Changing structure WITHOUT changing behavior → **Refactoring**
- ❌ Changing structure AND behavior → **Rewriting** (different process)

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
npm run lint        # 1. Linting passes
npm run typecheck  # 2. Types are valid
npm test           # 3. Tests pass
npm run build      # 4. Build succeeds
```

### 4. 💾 Commit Frequently

```bash
# After each successful verification
git commit -m "refactor: [describe single change]"
```

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────┐
│           REFACTORING WORKFLOW                       │
├─────────────────────────────────────────────────────┤
│ 1. ASSESS     → Understand code, measure metrics    │
│ 2. PREPARE    → Checklist, define scope            │
│ 3. PLAN       → Choose refactoring type             │
│ 4. EXECUTE    → Loop: change → test → commit       │
│ 5. VERIFY     → Full test suite, push to CI        │
└─────────────────────────────────────────────────────┘
```

---

## Phase 1: Assessment

### Code Understanding

Before refactoring, answer:

| Question | Why It Matters |
|----------|----------------|
| What does this code do? | Can't improve what you don't understand |
| How is it tested? | Tests define correct behavior |
| Who uses this code? | External dependencies may break |

### Code Metrics

| Metric | Threshold | Action |
|--------|-----------|--------|
| Function length | >50 lines | Extract method |
| Cyclomatic complexity | >10 | Simplify logic |
| Parameters | >4 | Parameter object |
| Nesting depth | >4 | Early returns |

---

## Phase 2: Preparation

Use `templates/pre-refactor-checklist.md` for structured preparation.

### Pre-Refactor Checklist

- [ ] Tests pass (GREEN)
- [ ] Coverage > 70%
- [ ] Branch is clean
- [ ] Goal is ONE improvement
- [ ] Steps broken into <15 min each

---

## Phase 3: Planning

### Choose Refactoring Type

Based on code smell:

| Code Smell | Refactoring | Priority |
|------------|-------------|----------|
| Long Method | Extract Method | P0 |
| Large Class | Extract Class | P0 |
| Duplicate Code | Extract Function | P1 |
| Feature Envy | Move Method | P1 |
| Data Clumps | Parameter Object | P1 |
| Switch Statements | Polymorphism | P2 |

**Full catalog:** See `references/catalog/refactoring-types.md`

### Plan Baby Steps

Use `templates/execution-plan.md` for structured planning.

---

## Phase 4: Execution

### The Safe Loop

```
1. Pick ONE small change
2. Make the change
3. RUN TESTS
   ├─ GREEN → Commit & Continue
   └─ RED   → Fix OR Rollback
4. Repeat until done
```

### When Tests Fail

| Step | Action |
|------|--------|
| 1 | Revert change → Tests pass? |
| 2 | If yes: Fix the bug introduced |
| 3 | If no: Pre-existing failure |

**⚠️ NEVER leave tests failing**

---

## Phase 5: Verification

```bash
# Full verification
npm test && npm run lint && npm run build

# Push to CI
git push
```

---

## 📁 Directory Structure

```
safe-refactoring/
├── SKILL.md
├── references/
│   ├── catalog/
│   │   └── refactoring-types.md    # 15 refactoring types
│   └── smells/
│       └── code-smells.md            # 14 code smells
├── examples/
│   └── scenarios/
│       └── refactoring-scenarios.md  # Real-world examples
└── templates/
    ├── pre-refactor-checklist.md
    └── execution-plan.md
```

---

## 📖 Reference Files

| Category | Location | Contents |
|----------|----------|----------|
| **Catalog** | `references/catalog/` | 15 refactoring techniques |
| **Smells** | `references/smells/` | 14 code smells with fixes |
| **Scenarios** | `examples/scenarios/` | Real-world refactoring |
| **Templates** | `templates/` | Checklist and planning |

---

## Quick Reference

```
🟢 GREEN    → Tests MUST pass before starting
📏 SMALL    → One tiny change at a time
✅ VERIFY   → Run tests after each change
💾 COMMIT   → Checkpoint frequently

NEVER:
- Skip running tests
- Make multiple changes at once
- Continue after RED test
```

---

## Red Flags - STOP Immediately

| Thought | Reality | Action |
|---------|---------|--------|
| "Tests slow me down" | Without tests, you're blind | Run tests ALWAYS |
| "I'll refactor this too" | Scope creep | Stick to ONE goal |
| "This is simple, no tests needed" | Assumptions dangerous | Add tests first |
| "Let me just try this" | Guessing | Analyze first |

---

## Integration Notes

- Works with `test-driven-debugging` for adding tests first
- Works with `code-review-guardian` after refactoring
- Use `code-complexity-optimizer` for algorithmic improvements

---

## Limitations

- Cannot refactor compiled binaries
- Cannot refactor code without understanding
- Large-scale refactoring requires team coordination
