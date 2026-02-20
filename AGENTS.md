# AGENTS.md - Developer Skills Collection

> A collection of OpenCode skills for systematic software development.

## ⚠️ About This Project

This project provides **skills** (guidance documents) for OpenCode agents. Skills do not automatically execute - they guide agents on HOW to think and act.

**For automatic context optimization**, use [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning) plugin instead.

---

## Available Skills

| Skill | Purpose | When to Load |
|-------|---------|--------------|
| **test-driven-debugging** | Fix failing tests systematically | When any test fails |
| **code-review-guardian** | Comprehensive code review | When reviewing PRs or code |
| **safe-refactoring** | Risk-free code refactoring | When improving code structure |
| **tokensaver** | Context optimization strategies | When approaching token limits |

---

## Quick Reference

### Load a Skill

```
skill({ name: "test-driven-debugging" })
skill({ name: "code-review-guardian" })
skill({ name: "safe-refactoring" })
skill({ name: "tokensaver" })
```

### When to Use Each Skill

| Scenario | Load Skill |
|----------|------------|
| Test X is failing | test-driven-debugging |
| Review this PR | code-review-guardian |
| Refactor module Y | safe-refactoring |
| Context too large | tokensaver |

---

## Skill Summaries

### 🧪 test-driven-debugging

```
Protocol:
1. READ test → Understand what it's testing
2. RUN test → Isolate the failure
3. LOG hypotheses → Systematic investigation
4. FIX minimal → Smallest possible change
5. VERIFY all → No regressions

Key rule: Never skip understanding the test before fixing.
```

### 🔒 code-review-guardian

```
Dimensions (in order):
1. Security → SQL injection, XSS, secrets
2. Correctness → Logic, edge cases, errors
3. Performance → N+1, memory, blocking
4. Maintainability → Names, complexity, DRY
5. Testing → Coverage, edge cases
6. Documentation → APIs, complex logic

Key rule: Review security first, always.
```

### 🔧 safe-refactoring

```
Principles:
1. GREEN → Tests must pass before starting
2. SMALL → One tiny change at a time
3. VERIFY → Run tests after each change
4. COMMIT → Checkpoint frequently

Key rule: If tests fail, stop and fix before continuing.
```

### 💰 tokensaver

```
Strategies:
1. Structured Summarization → Replace old messages with summary
2. Tool Output Pruning → Remove redundant reads, old errors
3. Context Hygiene → Don't re-explore same patterns
4. Importance Retention → Keep P1, compress P3-P4

Key rule: Optimize for tokens-per-task, not tokens-per-request.
```

---

## Project Structure

```
.opencode/
└── skills/
    ├── test-driven-debugging/
    │   └── SKILL.md
    ├── code-review-guardian/
    │   └── SKILL.md
    ├── safe-refactoring/
    │   └── SKILL.md
    └── tokensaver/
        └── SKILL.md
```

---

## Installation

### As Global Skills

```bash
cp -r .opencode/skills/* ~/.config/opencode/skills/
```

### As Project Skills

Skills in `.opencode/skills/` are automatically discovered by OpenCode.

---

## Related Resources

- [OpenCode Skills Documentation](https://opencode.ai/docs/skills/)
- [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)
