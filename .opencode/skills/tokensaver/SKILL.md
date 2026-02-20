---
name: tokensaver
description: Runtime context optimization strategies to reduce token consumption during OpenCode sessions
license: MIT
compatibility: opencode
---

# TokenSaver

Optimize context to reduce token costs. Active strategies, not passive advice.

## ⚠️ Critical Warning

**This skill does NOT automatically reduce tokens.** You must actively apply these strategies.

```
Reading this skill = +1500 tokens
Applying this skill = -50000 tokens (net savings)
Ignoring this skill = wasted tokens
```

---

## Core Principle: Tokens-Per-Task

**Wrong:** Minimize tokens per request
**Right:** Minimize total tokens to complete the task

Aggressive compression that loses information causes re-fetching → MORE tokens wasted.

---

## When to Activate

| Trigger | Action |
|---------|--------|
| Context > 50% limit | Start monitoring |
| Context > 70% limit | Proactively compress |
| After subtask complete | Summarize and prune |
| Before expensive ops | Clean up context |

---

## Strategy 1: Structured Summarization

Replace old messages with this summary format:

```markdown
## Session Summary

### User Intent
[1-2 sentences]

### Files Modified
- `path/file.ts`: [what changed]

### Key Decisions
- [decision + rationale]

### Current State
[status and next steps]

### Must Preserve
[file paths, error messages, critical context]
```

**When:** 20+ tool calls, repeated reads, or phase complete

---

## Strategy 2: Tool Output Pruning

### Remove Redundant Reads
```
❌ Keep 5 read results for same file
✅ Keep only latest read
```

### Compress After Write
```
❌ Keep write + later read
✅ Prune write, keep read result
```

### Clean Old Errors
After 4+ turns, keep error message but prune failed input:
```
❌ 500 lines of failed input + error
✅ "[Pruned] - Error: cannot read property 'x'"
```

---

## Strategy 3: Avoid Re-Exploration

Don't grep the same pattern twice. Remember findings:

```
❌ grep "auth" → results → later grep "auth" again
✅ Remember: "Auth patterns in src/middleware/auth.ts"
```

---

## Strategy 4: Priority-Based Retention

| Priority | Keep | Prune |
|----------|------|-------|
| P1 | File paths, errors, user intent | Never |
| P2 | Decisions, file changes | Summarize |
| P3 | Exploration logs | Compress |
| P4 | Duplicate reads | Prune entirely |

---

## Quick Checklist

Before major actions:

- [ ] Context > 70%? → Compress
- [ ] Read same file 3x? → Prune old
- [ ] Phase done? → Summarize
- [ ] 10+ errors? → Clean old ones

---

## Token Estimation

| Content | Ratio |
|---------|-------|
| English | ~4 chars/token |
| Code | ~3 chars/token |
| Chinese | ~1.5 chars/token |

---

## Anti-Patterns

| ❌ Don't | Result |
|----------|--------|
| Keep everything | Bloat, high cost |
| Compress aggressively | Lost info, re-fetch |
| Ignore this skill | Wasted tokens |

---

## Integration

Combine with [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning) for automatic + manual optimization.

---

## Quick Reference

```
1. SUMMARIZE old context → structured format
2. PRUNE duplicates and errors
3. PRESERVE file paths and decisions
4. CHECK before expensive operations
```
