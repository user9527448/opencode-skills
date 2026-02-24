# Test-Driven Debugging

> Systematic debugging methodology with causal debugging principles for AI coding agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/MIT)
[![OpenCode Compatible](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://opencode.ai)

## Overview

A four-phase systematic debugging methodology that emphasizes root cause investigation before any fixes. Enhanced with modern debugging principles including causal debugging, deterministic replay, and verification gates.

**Triggers:** "test failed", "debug this", "fix bug", "regression", "flaky test", "CI red"

## Features

- 🔬 **Root Cause First** - Never fix without understanding the problem
- 🧪 **Scientific Method** - Hypothesis testing, not guessing
- 🛡️ **Verification Gates** - Coverage >80%, mutation >90%
- 📊 **Pattern Library** - 20+ common failure patterns
- 🎯 **Causal Debugging** - Deterministic replay, dynamic slicing
- 📝 **Templates** - Hypothesis testing, error analysis
- 🔧 **Automation** - Git bisect automation script

## Directory Structure

```
test-driven-debugging/
├── SKILL.md                           # Main skill (460 lines)
├── SKILL-zh-cn.md                     # Chinese version
├── references/
│   └── patterns/
│       └── failure-patterns.md        # 20+ failure patterns
├── examples/
│   └── scenarios/
│       └── debugging-scenarios.md    # Real-world examples
├── templates/
│   ├── hypothesis-template.md         # Hypothesis testing form
│   └── error-analysis.md             # Error analysis worksheet
└── scripts/
    └── bisect-automate.sh             # Git bisect automation
```

## Core Principles

| Principle | Description |
|-----------|-------------|
| 🟢 **Deterministic First** | Make failures reproducible |
| 🔬 **Scientific Method** | Hypothesis → Test → Evidence |
| 📏 **Minimal Reproduction** | Smallest possible case |
| 🛡️ **Verification Gates** | Never ship without proof |

## The Four Phases

```
Phase 1: ROOT CAUSE
  □ Read FULL error message
  □ Reproduce deterministically
  □ Check recent changes (git)
  □ Gather evidence

Phase 2: PATTERN
  □ Find working examples
  □ Compare vs failing
  □ Match pattern library

Phase 3: HYPOTHESIS
  □ Form ONE hypothesis
  □ Test minimally
  □ Document result

Phase 4: IMPLEMENT
  □ Create failing test
  □ Minimal fix
  □ Run verification gates
```

## Verification Gates

Before shipping any fix:

| Gate | Threshold | Tool |
|------|-----------|------|
| Unit tests | 100% pass | jest, pytest |
| Coverage | >80% changed | coverage report |
| Mutation | >90% killed | stryker, mutmut |
| Type check | 0 errors | tsc --noEmit |

## Quick Start

```bash
# Load the skill
skill({ name: "test-driven-debugging" })

# Run automated bisect (if regression)
bash scripts/bisect-automate.sh

# Use templates for systematic debugging
# templates/hypothesis-template.md
# templates/error-analysis.md
```

## Advanced: Causal Debugging

For complex bugs:

1. **Deterministic Replay** - Freeze environment, capture exact inputs
2. **Dynamic Slicing** - Find minimal code path causing bug
3. **Counterfactual Reasoning** - "If X, does failure disappear?"
4. **Property-Based Testing** - Verify no regressions

## Integration

Works well with other OpenCode skills:

- `code-review-guardian` - Post-fix quality check
- `safe-refactoring` - If refactoring needed after fix
- `code-complexity-optimizer` - For performance-related bugs

## License

MIT

## Author

user9527448
