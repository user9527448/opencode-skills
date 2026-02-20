---
name: code-review-guardian
description: Comprehensive code review checklist - security, performance, maintainability, and correctness
license: MIT
compatibility: opencode
---

# Code Review Guardian

Review code like a senior engineer, not a spell checker.

## When to Use

- Reviewing pull requests
- After completing a feature
- Before merging to main branch
- When asked to review code changes

---

## The Problem with Surface-Level Reviews

```
❌ Bad: "LGTM" or only commenting on formatting
✅ Good: Systematic review across all dimensions
```

Surface reviews miss bugs, security issues, and design problems.

---

## Review Dimensions

Review in this order - from most critical to least:

### 1. 🔒 Security (CRITICAL - Review First)

**Check for:**

| Vulnerability | What to Look For |
|---------------|------------------|
| SQL Injection | String concatenation in queries |
| XSS | Unescaped user input in HTML |
| CSRF | Missing tokens on state changes |
| Secrets in Code | API keys, passwords in source |
| Path Traversal | User input in file paths |
| Command Injection | User input in shell commands |

**Red flags:**

```javascript
// ❌ Dangerous patterns
query = "SELECT * FROM users WHERE id = " + userId
exec(userInput)
fs.readFile(path + userInput)
innerHTML = userInput
```

```javascript
// ✅ Safe patterns
query = db.query("SELECT * FROM users WHERE id = ?", [userId])
// Use parameterized queries, escaping, allowlists
```

**Security checklist:**

- [ ] All user inputs are validated
- [ ] No hardcoded secrets/credentials
- [ ] Authentication/authorization present
- [ ] Sensitive data encrypted
- [ ] Rate limiting on public endpoints

---

### 2. 🎯 Correctness (CRITICAL)

**Verify:**

| Aspect | Questions to Ask |
|--------|------------------|
| Logic | Does this do what it's supposed to do? |
| Edge Cases | What happens with null/empty/boundary values? |
| Error Handling | Are errors caught and handled properly? |
| Race Conditions | What if this runs concurrently? |
| Data Integrity | Can this corrupt data? |

**Correctness checklist:**

- [ ] Happy path works correctly
- [ ] Error cases are handled
- [ ] Null/undefined inputs handled
- [ ] Boundary conditions considered
- [ ] No off-by-one errors

---

### 3. ⚡ Performance (IMPORTANT)

**Watch for:**

| Issue | Pattern | Fix |
|-------|---------|-----|
| N+1 Queries | Query in loop | Batch query |
| Memory Leak | Unclosed resources | Use cleanup/finally |
| Unnecessary Work | Redundant calculations | Cache/memoize |
| Large Payloads | Returning too much data | Pagination/projection |
| Blocking I/O | Sync operations | Async patterns |

**Performance red flags:**

```javascript
// ❌ N+1 query pattern
for (const user of users) {
  const posts = await db.query(`SELECT * FROM posts WHERE user_id = ?`, [user.id])
}

// ✅ Batch query
const posts = await db.query(`SELECT * FROM posts WHERE user_id IN (?)`, [userIds])
```

**Performance checklist:**

- [ ] No N+1 queries
- [ ] No unnecessary loops/iterations
- [ ] Resources properly released
- [ ] Caching considered for hot paths
- [ ] Database queries optimized

---

### 4. 🧹 Maintainability (IMPORTANT)

**Evaluate:**

| Aspect | Good | Bad |
|--------|------|-----|
| Naming | `getUserById` | `get` or `func1` |
| Function Length | <30 lines | >100 lines |
| Complexity | Single responsibility | Does multiple things |
| DRY | Reused logic extracted | Copy-pasted code |
| Comments | Explain "why" | Explain "what" code does |

**Maintainability checklist:**

- [ ] Names are self-documenting
- [ ] Functions do one thing
- [ ] No deep nesting (>3 levels)
- [ ] Magic numbers are constants
- [ ] Complex logic has comments

---

### 5. 🧪 Testing (IMPORTANT)

**Check:**

| Question | Expectation |
|----------|-------------|
| Are new tests added? | Yes, for new code |
| Do tests cover edge cases? | Yes, not just happy path |
| Are tests readable? | Clear intent, not cryptic |
| Do tests pass? | All green |
| Are mocks appropriate? | Not over-mocked |

**Testing checklist:**

- [ ] New code has tests
- [ ] Tests cover edge cases
- [ ] Tests are readable
- [ ] No skipped tests without reason
- [ ] Mocks don't mask real issues

---

### 6. 📚 Documentation (NICE TO HAVE)

**Review:**

- [ ] Public APIs documented
- [ ] Complex logic explained
- [ ] README updated if needed
- [ ] Breaking changes noted

---

## Review Workflow

### Step 1: Understand Context

```markdown
## Context Checklist

- [ ] Read PR description
- [ ] Understand the problem being solved
- [ ] Check linked issues/tickets
- [ ] Note any design decisions mentioned
```

### Step 2: Quick Scan

First pass - get the big picture:

1. What files changed?
2. How many lines added/removed?
3. What's the general approach?

### Step 3: Deep Review

Second pass - use the dimensions above:

1. Security first
2. Then correctness
3. Then performance
4. Then maintainability
5. Then tests

### Step 4: Provide Feedback

**Good feedback format:**

```markdown
## Review Summary

### 🔴 Must Fix (blocking)
- [Issue 1]: [Description] (file:line)

### 🟡 Should Consider (non-blocking)
- [Issue 2]: [Suggestion]

### 🟢 Nice to Have
- [Minor improvement]

### ✅ What's Good
- [Positive observations]
```

---

## Feedback Principles

### ❌ Bad Feedback

```
"This is wrong"
"LGTM"
"Why did you do it this way?"
```

### ✅ Good Feedback

```
"This could cause SQL injection. Use parameterized queries instead:
cursor.query('SELECT * FROM users WHERE id = ?', [userId])"

"LGTM after addressing the security concern above. The refactoring of
the auth module is clean and well-tested."

"I'm curious about this approach - did you consider using X instead?
It might be simpler because Y."
```

**Good feedback is:**
- Specific (file:line)
- Constructive (suggests solution)
- Explained (why it matters)
- Kind (tone matters)

---

## Quick Reference Card

```
🔒 Security    → First, always
🎯 Correctness → Does it work?
⚡ Performance  → Any N+1? Memory leaks?
🧹 Maintainability → Readable? DRY?
🧪 Testing     → Covered? Edge cases?
📚 Documentation → Updated?
```

---

## Anti-Patterns

### ❌ "LGTM" without reading
Result: Bugs slip through

### ❌ Nitpicking formatting in first pass
Result: Miss critical issues

### ❌ Being vague ("this is bad")
Result: Developer doesn't know how to fix

### ❌ Only looking for problems
Result: Discouraging, misses good work

---

## Integration with AGENTS.md

```markdown
## Code Review Protocol

When reviewing code, load the code-review-guardian skill.
Always review security first, then correctness, then other dimensions.
Provide specific, constructive feedback with examples.
```
