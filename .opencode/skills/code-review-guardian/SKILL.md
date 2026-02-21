---
name: code-review-guardian
description: OWASP-aligned comprehensive code review - security, correctness, performance, maintainability, testing, documentation
license: MIT
compatibility: opencode
---

# Code Review Guardian

Review code like a senior engineer. Security first, always.

---

## 🚨 When to Activate This Skill

| Trigger | Priority |
|---------|----------|
| Pull request review | HIGH |
| Pre-merge check | HIGH |
| Security audit | CRITICAL |
| Post-implementation review | MEDIUM |
| Code quality check | MEDIUM |

---

## Review Order (Critical → Nice-to-have)

```
1. 🔒 Security     → ALWAYS FIRST
2. 🎯 Correctness  → Does it work?
3. ⚡ Performance   → Any bottlenecks?
4. 🧹 Maintainability → Readable? DRY?
5. 🧪 Testing      → Covered?
6. 📚 Documentation → Updated?
```

---

## 1. 🔒 Security Review (ALWAYS FIRST)

### OWASP Top 10 Quick Check

| # | Risk | What to Look For | Severity |
|---|------|------------------|----------|
| A01 | Broken Access Control | Missing auth checks, IDOR | 🔴 Critical |
| A02 | Crypto Failures | Weak algorithms, hardcoded keys | 🔴 Critical |
| A03 | Injection | String concat in SQL/commands | 🔴 Critical |
| A04 | Insecure Design | Missing security controls | 🟡 High |
| A05 | Misconfiguration | Default creds, verbose errors | 🟡 High |
| A06 | Vulnerable Components | Outdated packages | 🟡 High |
| A07 | Auth Failures | Weak passwords, missing MFA | 🔴 Critical |
| A08 | Data Integrity | Unvalidated inputs | 🟡 High |
| A09 | Logging Failures | Missing audit trails | 🟡 High |
| A10 | SSRF | User input in URLs | 🟡 High |

### Security Code Patterns

**❌ Dangerous Patterns:**
```javascript
// SQL Injection
query = "SELECT * FROM users WHERE id = " + userId

// Command Injection
exec(userInput)

// Path Traversal
fs.readFile(path + userInput)

// XSS
innerHTML = userInput

// Hardcoded secrets
const apiKey = "sk-abc123..."
```

**✅ Safe Patterns:**
```javascript
// Parameterized query
db.query("SELECT * FROM users WHERE id = ?", [userId])

// Allowlist validation
const allowed = ['option1', 'option2'];
if (!allowed.includes(input)) throw new Error();

// Environment variables
const apiKey = process.env.API_KEY

// Output encoding
textContent = escapeHtml(userInput)
```

### Security Checklist

- [ ] All user inputs validated and sanitized
- [ ] No hardcoded credentials or secrets
- [ ] Authentication present on protected routes
- [ ] Authorization checked before operations
- [ ] Sensitive data encrypted at rest and in transit
- [ ] Rate limiting on public endpoints
- [ ] CORS configured properly
- [ ] Security headers present (CSP, HSTS, X-Frame-Options)
- [ ] Dependencies checked for vulnerabilities

---

## 2. 🎯 Correctness Review

### Logic Verification

| Check | Questions |
|-------|-----------|
| Happy path | Does the main flow work? |
| Edge cases | null, empty, boundary values? |
| Error handling | All errors caught and handled? |
| Race conditions | Concurrent access safe? |
| Data integrity | Can this corrupt data? |

### Correctness Checklist

- [ ] Logic matches requirements
- [ ] All branches reachable and tested
- [ ] Null/undefined handled
- [ ] Empty arrays/objects handled
- [ ] Boundary conditions checked
- [ ] Error messages helpful
- [ ] No silent failures

---

## 3. ⚡ Performance Review

### Common Performance Issues

| Issue | Pattern | Detection |
|-------|---------|-----------|
| N+1 Queries | Query in loop | Look for `for...await` |
| Memory Leak | Unclosed resources | Missing `finally` or cleanup |
| Unnecessary Work | Redundant calculations | Duplicate function calls |
| Large Payloads | Too much data | Check response size |
| Blocking I/O | Sync operations | `readFileSync`, `execSync` |

### Performance Patterns

**❌ N+1 Query:**
```javascript
for (const user of users) {
  const posts = await db.query(`SELECT * FROM posts WHERE user_id = ?`, [user.id])
}
```

**✅ Batch Query:**
```javascript
const userIds = users.map(u => u.id)
const posts = await db.query(`SELECT * FROM posts WHERE user_id IN (?)`, [userIds])
```

### Performance Checklist

- [ ] No N+1 queries
- [ ] No unnecessary loops
- [ ] Resources properly released
- [ ] Caching considered for hot paths
- [ ] Database queries use indexes
- [ ] Pagination for large lists
- [ ] Lazy loading where appropriate

---

## 4. 🧹 Maintainability Review

### Code Quality Metrics

| Aspect | Good | Bad |
|--------|------|-----|
| Naming | `getUserById` | `get`, `func1` |
| Length | <30 lines | >100 lines |
| Complexity | Single responsibility | Multiple concerns |
| DRY | Extracted utilities | Copy-paste code |
| Comments | Explain "why" | Explain "what" |

### Maintainability Checklist

- [ ] Names are self-documenting
- [ ] Functions do one thing
- [ ] Nesting ≤3 levels
- [ ] Magic numbers are constants
- [ ] Complex logic has comments
- [ ] No dead code
- [ ] Consistent style with codebase

---

## 5. 🧪 Testing Review

### Test Quality Checks

| Question | Expectation |
|----------|-------------|
| New tests added? | Yes, for new code |
| Edge cases covered? | Not just happy path |
| Tests readable? | Clear intent |
| All tests pass? | Green |
| Mocks appropriate? | Not over-mocked |

### Testing Checklist

- [ ] New code has tests
- [ ] Edge cases tested
- [ ] Tests are readable
- [ ] No skipped tests without reason
- [ ] Test names describe behavior
- [ ] Assertions are specific

---

## 6. 📚 Documentation Review

- [ ] Public APIs documented
- [ ] Complex logic explained
- [ ] README updated if needed
- [ ] Breaking changes noted
- [ ] Examples provided

---

## Review Output Template

```markdown
## Code Review Summary

### 🔴 Must Fix (Blocking)
- [Security] [file:line] - SQL injection vulnerability
- [Logic] [file:line] - Null check missing

### 🟡 Should Consider (Non-blocking)
- [Performance] Consider batching queries in loop
- [Style] Variable name could be more descriptive

### 🟢 Done Well
- Clean separation of concerns
- Good test coverage on new feature
- Clear commit messages

### ✅ Overall
[Approve / Request Changes / Comment]
```

---

## Feedback Principles

### ❌ Bad Feedback
```
"This is wrong"
"LGTM"
"Why did you do this?"
```

### ✅ Good Feedback
```
"This could cause SQL injection. Use parameterized queries:
cursor.query('SELECT * FROM users WHERE id = ?', [userId])"

"LGTM after addressing the security concern. 
The refactoring is clean and well-tested."
```

**Good feedback is:**
- Specific (file:line)
- Constructive (suggests solution)
- Explained (why it matters)
- Kind (tone matters)

---

## Quick Reference Card

```
🔒 SECURITY    → First, always
   □ Injection risks
   □ Auth/authz
   □ Secrets in code
   
🎯 CORRECTNESS → Works as expected?
   □ Edge cases
   □ Error handling
   
⚡ PERFORMANCE  → Scalable?
   □ N+1 queries
   □ Memory leaks
   
🧹 MAINTAINABILITY → Readable?
   □ Naming
   □ Complexity
   
🧪 TESTING     → Covered?
   □ New tests
   □ Edge cases
   
📚 DOCS        → Updated?
   □ API docs
   □ README
```
