# OpenCode Skill Writing Best Practices

> Research findings and guidelines for writing high-quality OpenCode skills.

---

## Official Requirements Summary

### File Structure

```
.opencode/skills/
└── <skill-name>/
    └── SKILL.md              # Required: exact filename
```

### Frontmatter Requirements

| Field | Required | Rules |
|-------|----------|-------|
| `name` | ✅ Yes | 1-64 chars, lowercase alphanumeric + single hyphens, no leading/trailing/consecutive `--`, must match directory name |
| `description` | ✅ Yes | 1-1024 characters, specific enough for agent to choose correctly |
| `license` | ❌ Optional | SPDX identifier (e.g., MIT, Apache-2.0) |
| `compatibility` | ❌ Optional | Target platform (e.g., opencode) |
| `metadata` | ❌ Optional | String-to-string map for custom data |

### Name Validation Regex

```
^[a-z0-9]+(-[a-z0-9]+)*$
```

**Valid examples:**
- `test-driven-debugging`
- `code-review-guardian`
- `git-release`

**Invalid examples:**
- `Test-Debugging` (uppercase)
- `test_debugging` (underscore)
- `-test-debugging` (leading hyphen)
- `test--debugging` (consecutive hyphens)

---

## Best Practices from Research

### 1. Clear Trigger Conditions

**Bad:**
```markdown
This skill helps with debugging.
```

**Good:**
```markdown
## When to Use Me
- Any test is failing
- CI/CD pipeline is red
- "Works on my machine" issues
- Flaky test detection
```

**Why:** Agents need explicit conditions to know when to load a skill.

### 2. Structured Sections

Recommended structure (in order):

```markdown
---
name: skill-name
description: Clear, specific description (1-1024 chars)
---

# Skill Title

[Core principle or "elevator pitch"]

## When to Activate
[Explicit trigger conditions]

## Core Principle / The Iron Law
[Most important rule]

## Step-by-Step Process
[Numbered phases or steps]

## Quick Reference
[Condensed checklist for quick lookup]

## Anti-Patterns / Red Flags
[What NOT to do]

## Integration
[How this skill works with others]
```

### 3. Keep Prompts Focused

**Bad:**
```markdown
You are an expert developer who knows everything about code quality,
security, performance, and can help with any programming task...
```

**Good:**
```markdown
You are a code reviewer focused on security vulnerabilities.

Review code for:
1. SQL injection risks
2. XSS vulnerabilities
3. Hardcoded secrets
4. Authentication flaws
```

**Why:** Focused prompts produce more consistent, predictable behavior.

### 4. Include Examples in Prompts

**Without example:**
```markdown
Report any issues found.
```

**With example:**
```markdown
Report issues in this format:

| Severity | File | Line | Issue | Fix |
|----------|------|------|-------|-----|
| Critical | auth.ts | 42 | SQL injection | Use parameterized query |

Example:
| Critical | db.ts | 15 | Hardcoded password | Use process.env.DB_PASSWORD |
```

**Why:** Examples establish expected output format and quality level.

### 5. Use Templates and Checklists

Templates make skills more actionable:

```markdown
## Error Analysis Template

### Full Error Message
[Copy COMPLETE error, not summary]

### Stack Trace Analysis
- Top of stack: [Where error manifested]
- Bottom of stack: [Where error originated]

### Classification
[ ] TypeError
[ ] ReferenceError
[ ] AssertionError
```

### 6. Provide Quick Reference Cards

Agents need quick access to key information:

```markdown
## Quick Reference

Phase 1: ROOT CAUSE
□ Read FULL error message
□ Reproduce consistently
□ Check recent changes

Phase 2: PATTERN
□ Find working examples
□ Compare vs failing

Phase 3: HYPOTHESIS
□ Form ONE hypothesis
□ Test minimally

Phase 4: IMPLEMENT
□ Create failing test
□ Minimal fix
□ Verify all tests
```

### 7. Include Anti-Patterns

Tell agents what NOT to do:

```markdown
## 🛑 Red Flags - Stop Immediately

| Thought | Reality | Action |
|---------|---------|--------|
| "Let me just try this fix" | Guessing | STOP → Do Phase 1 |
| "Maybe increase timeout" | Masking symptom | Find root cause |
```

### 8. Use Visual Hierarchy

```markdown
# Main Title (H1)
## Section (H2)
### Subsection (H3)

- Bullet points for lists
1. Numbered for sequences

| Tables | For | Comparisons |
|--------|-----|-------------|

```code blocks for examples```

**Tip:** Use emoji sparingly for emphasis:
- 🚨 Critical warnings
- ✅ Good patterns
- ❌ Bad patterns
- ⚠️ Important notes
```

---

## Content Length Guidelines

| Component | Recommended Length |
|-----------|-------------------|
| Description | 20-160 characters |
| Core principle | 1-2 sentences |
| Trigger conditions | 3-6 items |
| Each phase/step | 50-200 words |
| Quick reference | 5-15 lines |
| Total skill | 200-400 lines |

**Why length matters:**
- Too short: Insufficient guidance
- Too long: Agent won't follow all instructions
- Sweet spot: Enough detail, scannable structure

---

## Validation Checklist

Before publishing a skill, verify:

### Frontmatter
- [ ] `name` matches directory name exactly
- [ ] `name` follows naming convention (lowercase, hyphens only)
- [ ] `description` is 20-1024 characters
- [ ] `description` is specific enough for selection
- [ ] Optional fields have valid values

### Content
- [ ] Clear trigger conditions defined
- [ ] Step-by-step process provided
- [ ] Examples included for key concepts
- [ ] Quick reference/summary available
- [ ] Anti-patterns documented
- [ ] Template(s) provided where applicable

### Structure
- [ ] Logical flow (when → what → how)
- [ ] Headings create clear hierarchy
- [ ] Tables used for comparisons
- [ ] Code blocks used for examples
- [ ] List items are concise

---

## Common Mistakes to Avoid

### 1. Name/Directory Mismatch

```
❌ Directory: code-review/
   Frontmatter: name: code-review-guardian

✅ Directory: code-review-guardian/
   Frontmatter: name: code-review-guardian
```

### 2. Vague Description

```
❌ description: Helps with code review

✅ description: OWASP-aligned code review for security, 
   performance, and maintainability issues
```

### 3. Missing Trigger Conditions

```
❌ # Code Review
   This skill helps review code.

✅ # Code Review Guardian
   ## When to Activate
   - Pull request review
   - Pre-merge security check
   - Code quality audit
```

### 4. No Examples

```
❌ Fix any issues you find.

✅ ## Example Fix
   Before: const apiKey = "sk-abc123"
   After: const apiKey = process.env.API_KEY
```

### 5. Missing Quick Reference

```
❌ (Only verbose explanations)

✅ ## Quick Reference
   🔒 Security → First, always
   🎯 Correctness → Does it work?
   ⚡ Performance → Any N+1?
```

---

## Examples from Our Skills

### test-driven-debugging

**Strengths:**
- Clear "Iron Law" principle
- Four-phase framework
- Pattern library for common failures
- Three-strike rule for failed fixes
- Red flags table

**Structure:**
```
Trigger Conditions → Iron Law → Phase 1-4 → Red Flags → Quick Reference
```

### code-review-guardian

**Strengths:**
- Priority-ordered dimensions (Security First)
- OWASP Top 10 reference table
- Safe/Dangerous code patterns
- Review output template
- Feedback principles

**Structure:**
```
Review Order → Security (OWASP) → Correctness → Performance → 
Maintainability → Testing → Output Template
```

### safe-refactoring

**Strengths:**
- Core principles (GREEN, SMALL, VERIFY, COMMIT)
- Refactoring catalog with before/after
- Local refactorings list (safest operations)
- Rollback strategies
- Baby steps example

**Structure:**
```
Iron Law → Core Principles → Workflow → Catalog → 
Red Flags → Rollback → Quick Reference
```

### tokensaver

**Strengths:**
- Priority-based retention table (P1-P4)
- Before/after example with token counts
- Token estimation reference
- Integration with plugin mention

**Structure:**
```
When to Activate → Core Principle → Strategies 1-4 → 
Practical Application → Anti-Patterns → Quick Reference
```

---

## References

### Official Documentation
- [OpenCode Agent Skills](https://opencode.ai/docs/skills/)
- [malhashemi/opencode-skills](https://github.com/malhashemi/opencode-skills)

### Community Resources
- [AI Skill Market - SKILL.md Format Guide](https://aiskill.market/blog/claude-code-skill-md-format)
- [Context Engineering Guide](https://promptbuilder.cc/blog/context-engineering-agents-guide-2025)

### Related Skills for Reference
- [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)
- [systematic-debugging (Claudetory)](https://claudetory.com/skills/systematic-debugging)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-21 | Initial research compilation |
