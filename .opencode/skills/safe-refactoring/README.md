# Safe Refactoring

> Comprehensive refactoring protocol for AI coding agents.

## Overview

Safe Refactoring provides a systematic approach to code refactoring that prioritizes safety through small steps, continuous verification, and behavior preservation.

## Features

- **5-Phase Workflow**: Assess → Prepare → Plan → Execute → Verify
- **Code Smells Guide**: 14 common smells with fixes
- **Refactoring Catalog**: 15 refactoring techniques
- **Real-world Scenarios**: Step-by-step examples
- **Templates**: Pre-refactor checklist, execution plan

## Directory Structure

```
safe-refactoring/
├── SKILL.md                      # Main skill (274 lines)
├── references/
│   ├── catalog/
│   │   └── refactoring-types.md   # 15 refactoring types
│   └── smells/
│       └── code-smells.md           # 14 code smells
├── examples/
│   └── scenarios/
│       └── refactoring-scenarios.md # Real-world examples
└── templates/
    ├── pre-refactor-checklist.md
    └── execution-plan.md
```

## Quick Start

### Load the Skill

```javascript
skill({ name: "safe-refactoring" })
```

### Basic Workflow

```
1. ASSESS    → Understand code, measure metrics
2. PREPARE   → Use checklist template
3. PLAN      → Choose refactoring type
4. EXECUTE   → Loop: change → test → commit
5. VERIFY    → Full test suite, push
```

## Key Principles

| Principle | Description |
|-----------|-------------|
| 🟢 GREEN | Tests MUST pass before starting |
| 📏 SMALL | One tiny change at a time |
| ✅ VERIFY | Run tests after each change |
| 💾 COMMIT | Checkpoint frequently |

## Refactoring Types

| Type | When to Use |
|------|-------------|
| Extract Method | Long method with clear purpose |
| Rename | Name doesn't communicate intent |
| Move Method | Feature envy - uses other class more |
| Extract Class | Multiple responsibilities |
| Replace Conditional | Complex if-else chains |

## Code Smells

| Smell | Fix |
|--------|-----|
| Long Method | Extract Method |
| Large Class | Extract Class |
| Duplicate Code | Extract Function |
| Feature Envy | Move Method |
| Data Clumps | Parameter Object |

## Integration

- Works with `test-driven-debugging` for adding tests
- Works with `code-review-guardian` after refactoring
- Use `code-complexity-optimizer` for algorithm improvements

## License

MIT
