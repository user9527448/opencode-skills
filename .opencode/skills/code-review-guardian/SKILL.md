---
name: code-review-guardian
description: OWASP-aligned comprehensive code review - security, correctness, performance, maintainability, testing, documentation, architecture, concurrency
license: MIT
compatibility: opencode
metadata:
  references:
    dimensions: references/dimensions/
    examples: examples/
    templates: templates/
    scripts: scripts/
---

# Code Review Guardian

Review code like a senior engineer. Security first, always. Output standardized reports.

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

## 📋 Execution Workflow

### Step 1: Scope Definition
```
1. Identify files changed (git diff, PR files)
2. Determine review depth (quick/full/security-only)
3. Note language/framework for context
```

### Step 2: Automated Scans (Use Tools)
```
1. LSP Diagnostics → Type errors, linting issues
2. AST-grep → Pattern-based security/quality checks
3. Grep → Find TODOs, FIXMEs, hardcoded values
4. Run auto-scan.py → Quick security scan
```

### Step 3: Manual Review (By Dimension)
```
Review in order: Security → Correctness → Architecture → Performance 
                 → Maintainability → Concurrency → Testing → Documentation
                 
Use references/dimensions/ for detailed guidance on each dimension
```

### Step 4: Generate Report
```
Use templates/report-template.md for standardized output
```

---

## Review Dimensions (Critical → Nice-to-have)

```
1. 🔒 Security      → ALWAYS FIRST
2. 🎯 Correctness   → Does it work?
3. 🏗️ Architecture  → Design patterns, SOLID
4. ⚡ Performance    → Any bottlenecks?
5. 🧹 Maintainability → Readable? DRY?
6. 🔄 Concurrency   → Thread/process safe?
7. ♿ Accessibility → Frontend a11y
8. 🧪 Testing       → Covered?
9. 📚 Documentation → Updated?
```

---

## Quick Reference Card

```
📋 EXECUTION ORDER
1. Scope → 2. Auto-scan → 3. Manual review → 4. Report

🔒 SECURITY    → First, always
   □ Injection risks (SQL, CMD, XSS)
   □ Auth/authz gaps
   □ Secrets in code
   □ Input validation

🎯 CORRECTNESS → Works as expected?
   □ Edge cases (null, empty, boundary)
   □ Error handling
   □ Type safety

🏗️ ARCHITECTURE → Well designed?
   □ SOLID principles
   □ No circular deps
   □ Separation of concerns

⚡ PERFORMANCE  → Scalable?
   □ N+1 queries
   □ Memory leaks
   □ Blocking I/O

🧹 MAINTAINABILITY → Readable?
   □ Naming clarity
   □ Complexity < 10
   □ DRY principle

🔄 CONCURRENCY → Thread safe?
   □ Race conditions
   □ Proper locking

♿ ACCESSIBILITY → A11y compliant?
   □ Alt text
   □ Keyboard nav
   □ Color contrast

🧪 TESTING     → Covered?
   □ New tests for new code
   □ Edge cases tested
   □ All tests pass

📚 DOCS        → Updated?
   □ API documentation
   □ README updates
   □ Breaking changes noted

📊 OUTPUT → Use templates/report-template.md
```

---

## 📁 Directory Structure

```
code-review-guardian/
├── SKILL.md
├── references/
│   └── dimensions/
│       ├── security.md        # OWASP Top 10, vulnerability patterns
│       ├── correctness.md     # Logic verification, error handling
│       ├── architecture.md    # SOLID principles, design patterns
│       ├── performance.md     # N+1, memory, algorithms
│       ├── maintainability.md # Naming, complexity, code smells
│       ├── concurrency.md     # Thread safety, race conditions
│       ├── accessibility.md   # WCAG 2.1, ARIA
│       ├── testing.md         # Test quality, patterns
│       └── documentation.md   # JSDoc, comments
├── examples/
│   └── scenarios/
│       ├── rest-api-review.md    # API review scenario
│       └── frontend-component.md  # React component scenario
├── templates/
│   ├── report-template.md     # Standard review report format
│   └── checklist-all.md       # Complete review checklist
└── scripts/
    └── auto-scan.py          # Automated security scanner
```

---

## 📖 Reference Files

| Category | Location | Contents |
|----------|----------|----------|
| **Dimensions** | `references/dimensions/` | 9 detailed review dimension guides |
| **Scenarios** | `examples/scenarios/` | Real-world review examples |
| **Templates** | `templates/` | Report template, complete checklist |
| **Scripts** | `scripts/` | Automated scan tool |

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
"[CRIT-001] SQL injection vulnerability at auth.ts:45
Use parameterized queries instead of string concatenation:
cursor.query('SELECT * FROM users WHERE id = ?', [userId])
Reference: OWASP A03:2021"
```

**Good feedback is:**
- Specific (file:line)
- Constructive (suggests solution)
- Explained (why it matters)
- Categorized (severity + category)
- Actionable (clear next step)

---

## Integration Notes

- Use `scripts/auto-scan.py` for quick automated checks
- Follow dimension order (Security first!)
- Always use report template for consistent output
- Review `examples/scenarios/` for real-world patterns

---

## Limitations

- Automated scans are heuristics only - manual review still required
- Cannot detect business logic errors
- Cannot verify security controls effectiveness
- Accessibility review limited to frontend code
- Performance benchmarks require actual load testing
