# OpenCode Developer Skills

> A collection of OpenCode skills for systematic software development.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What's Included

| Skill | Purpose | Lines |
|-------|---------|-------|
| 🧪 [test-driven-debugging](.opencode/skills/test-driven-debugging/SKILL.md) | Fix failing tests systematically | 232 |
| 🔒 [code-review-guardian](.opencode/skills/code-review-guardian/SKILL.md) | Comprehensive code review | 307 |
| 🔧 [safe-refactoring](.opencode/skills/safe-refactoring/SKILL.md) | Risk-free code refactoring | 376 |
| 💰 [tokensaver](.opencode/skills/tokensaver/SKILL.md) | Context optimization strategies | 160 |

## Quick Start

### Option 1: Project-level (Recommended)

Clone or copy to your project:

```bash
# Clone
git clone https://github.com/yourusername/opencode-skills.git
cp -r opencode-skills/.opencode/skills/* your-project/.opencode/skills/

# Or copy directly
cp -r .opencode/skills/* /path/to/your/project/.opencode/skills/
```

### Option 2: Global Installation

Install for all projects:

```bash
cp -r .opencode/skills/* ~/.config/opencode/skills/
```

## Usage

Load a skill when needed:

```
skill({ name: "test-driven-debugging" })
skill({ name: "code-review-guardian" })
skill({ name: "safe-refactoring" })
skill({ name: "tokensaver" })
```

## Skill Summaries

### 🧪 test-driven-debugging

```
Protocol:
1. READ test → Understand what it's testing
2. RUN test → Isolate the failure
3. LOG hypotheses → Systematic investigation
4. FIX minimal → Smallest possible change
5. VERIFY all → No regressions
```

**When to use:** Any test is failing

### 🔒 code-review-guardian

```
Dimensions (in order):
1. Security → SQL injection, XSS, secrets
2. Correctness → Logic, edge cases, errors
3. Performance → N+1, memory, blocking
4. Maintainability → Names, complexity, DRY
5. Testing → Coverage, edge cases
6. Documentation → APIs, complex logic
```

**When to use:** Reviewing PRs or code

### 🔧 safe-refactoring

```
Principles:
1. GREEN → Tests must pass before starting
2. SMALL → One tiny change at a time
3. VERIFY → Run tests after each change
4. COMMIT → Checkpoint frequently
```

**When to use:** Improving code structure

### 💰 tokensaver

```
Strategies:
1. Structured Summarization → Replace old messages with summary
2. Tool Output Pruning → Remove redundant reads, old errors
3. Context Hygiene → Don't re-explore same patterns
4. Importance Retention → Keep P1, compress P3-P4
```

**When to use:** Approaching token limits

## Related Projects

- [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning) - Automatic context optimization (plugin)
- [OpenCode Documentation](https://opencode.ai/docs/skills/) - Official skill docs

## Contributing

Contributions welcome! Each skill follows this structure:

```yaml
---
name: skill-name
description: Brief description
license: MIT
compatibility: opencode
---

# Skill content...
```

## License

MIT
