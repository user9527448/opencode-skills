# OpenCode Developer Skills

> A collection of OpenCode skills for systematic software development.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What's Included

| Skill | Purpose | Lines |
|-------|---------|-------|
| 🧪 [test-driven-debugging](.opencode/skills/test-driven-debugging/SKILL.md) | Fix failing tests systematically | 463 |
| 🔒 [code-review-guardian](.opencode/skills/code-review-guardian/SKILL.md) | Comprehensive code review | 217 |
| 🔧 [safe-refactoring](.opencode/skills/safe-refactoring/SKILL.md) | Risk-free code refactoring | 274 |
| 🚀 [code-complexity-optimizer](.opencode/skills/code-complexity-optimizer/SKILL.md) | Algorithm complexity optimization | 357 |
| 📁 [skill-structure-organizer](.opencode/skills/skill-structure-organizer/SKILL.md) | Restructure skills to modular format | 417 |
| 💰 [tokensaver](.opencode/skills/tokensaver/SKILL.md) | Context optimization strategies | 253 |

## Quick Start

### Option 1: Project-level (Recommended)

Clone or copy to your project:

```bash
# Clone
git clone https://github.com/user9527448/opencode-skills.git
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

### How Skills Work

Skills are **guidance documents** loaded into OpenCode's context. They tell the AI agent HOW to approach specific tasks.

```
┌─────────────────────────────────────────────────────────┐
│  User: "My test is failing, help me fix it"             │
│                                                         │
│  OpenCode: Loads test-driven-debugging skill           │
│            → Now knows the systematic debugging process │
│            → Follows: ROOT CAUSE → PATTERN → HYPOTHESIS│
└─────────────────────────────────────────────────────────┘
```

### Loading a Skill

In OpenCode, skills are loaded by calling:

```
skill({ name: "test-driven-debugging" })
skill({ name: "code-review-guardian" })
skill({ name: "safe-refactoring" })
skill({ name: "code-complexity-optimizer" })
skill({ name: "skill-structure-organizer" })
skill({ name: "tokensaver" })
```

**This happens automatically when:**
- You mention a related task (e.g., "test is failing")
- OpenCode detects the need for a skill
- You explicitly ask to load a skill

### When to Use Each Skill

| Scenario | Skill to Load |
|----------|---------------|
| "Test X is failing" | test-driven-debugging |
| "Review this PR" | code-review-guardian |
| "Refactor module Y" | safe-refactoring |
| "代码优化" / "Optimize this code" | code-complexity-optimizer |
| "Skill too long" / "Restructure skill" | skill-structure-organizer |
| "Context is too large" | tokensaver |

## Skill Summaries

### 🧪 test-driven-debugging

```
Four Phases:
1. ROOT CAUSE → Read error, reproduce, check git, gather evidence
2. PATTERN → Find working examples, match pattern library
3. HYPOTHESIS → Form one hypothesis, test minimally
4. IMPLEMENT → Create failing test, minimal fix, verification gates

Key Features:
- Causal debugging principles
- Verification gates (coverage >80%, mutation >90%)
- Deterministic replay
- Dynamic slicing
```

**When to use:** Any test is failing

### 🔒 code-review-guardian

```
9 Review Dimensions (in order):
1. 🔒 Security → OWASP Top 10, vulnerabilities
2. 🎯 Correctness → Logic, edge cases, errors
3. 🏗️ Architecture → SOLID, design patterns
4. ⚡ Performance → N+1, memory, algorithms
5. 🧹 Maintainability → Naming, complexity, DRY
6. 🔄 Concurrency → Thread safety, race conditions
7. ♿ Accessibility → WCAG 2.1, ARIA
8. 🧪 Testing → Coverage, test quality
9. 📚 Documentation → JSDoc, comments
```

**When to use:** Reviewing PRs or code

### 🔧 safe-refactoring

```
Five Phases:
1. ASSESS → Understand code, measure metrics
2. PREPARE → Checklist, define scope
3. PLAN → Choose refactoring type
4. EXECUTE → Loop: change → test → commit
5. VERIFY → Full test suite, push to CI

Principles:
- GREEN → Tests must pass before starting
- SMALL → One tiny change at a time
- VERIFY → Run tests after each change
- COMMIT → Checkpoint frequently
```

**When to use:** Improving code structure

### 🚀 code-complexity-optimizer

```
Process:
1. ANALYZE → Determine current time/space complexity
2. CLARIFY → Ask optimization goal (time, space, or balanced)
3. STRATEGIZE → Select optimization approach
4. EXECUTE → Apply minimal changes
5. VERIFY → Confirm correctness and complexity improvement

Optimization strategies:
- Time: Hash maps, memoization, binary search, early exit
- Space: In-place, iterators, streaming
- Balanced: Optimal data structures, algorithm replacement
```

**When to use:** Optimizing algorithms based on complexity

### 📁 skill-structure-organizer

```
Seven Phases:
1. ANALYZE → Count lines, identify extraction targets
2. CREATE → mkdir references/ examples/ scripts/
3. EXTRACT → Languages, paradigms, examples to subdirs
4. UPDATE → Add metadata.references, reduce SKILL.md
5. DOCUMENT → Create README.md
6. VERIFY → Check all checklists
7. LOCALIZATION → Add bilingual support (optional)

When to restructure:
- SKILL.md > 500 lines
- Multiple language/paradigm guides
- Helper scripts present
```

**When to use:** Restructuring skills to modular format

### 💰 tokensaver

```
Strategies:
1. Structured Summarization → Replace old messages with summary
2. Tool Output Pruning → Remove redundant reads, old errors
3. Context Hygiene → Don't re-explore same patterns
4. Importance Retention → Keep P1, compress P3-P4
```

**When to use:** Approaching token limits

## Modular Structure

Several skills have been restructured to modular format:

```
.opencode/skills/
├── test-driven-debugging/
│   ├── SKILL.md
│   ├── references/patterns/
│   ├── examples/scenarios/
│   ├── templates/
│   └── scripts/
├── code-review-guardian/
│   ├── SKILL.md
│   ├── references/dimensions/
│   ├── examples/scenarios/
│   ├── templates/
│   └── scripts/
├── safe-refactoring/
│   ├── SKILL.md
│   ├── references/catalog/
│   ├── references/smells/
│   ├── examples/scenarios/
│   └── templates/
└── code-complexity-optimizer/
    ├── SKILL.md
    ├── references/languages/
    ├── references/paradigms/
    ├── examples/
    ├── templates/
    └── scripts/
```

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
