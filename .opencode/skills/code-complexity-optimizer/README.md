# Code Complexity Optimizer

> OpenCode skill for systematic algorithm optimization through complexity analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/MIT)
[![OpenCode Compatible](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://opencode.ai)

## Overview

Analyze time/space complexity (O(n), O(log n), O(n²), etc.), guide optimization through interactive Q&A, and provide clear tradeoff recommendations.

**Trigger:** "代码优化", "code optimization", "complexity optimization", "性能优化"

## Features

- 📊 **Complexity Analysis** - Automatic detection of time/space complexity patterns
- 💬 **Interactive Q&A** - Clarify optimization goals (time/space/balanced)
- 🔄 **Auto Decision** - Smart optimization selection based on constraints
- 🛠️ **Tool Integration** - Scripts for benchmarking and verification
- 🌍 **Multi-language** - Python, JavaScript, Java, C/C++, Go guides
- 🎯 **Multi-paradigm** - OOP, FP, Reactive, Concurrent patterns

## Directory Structure

```
code-complexity-optimizer/
├── SKILL.md                    # Core instructions (357 lines)
├── SKILL-zh-cn.md              # Chinese version
├── README.md                   # This file
│
├── references/
│   ├── languages/              # Language-specific guides
│   │   ├── python.md
│   │   ├── javascript.md
│   │   ├── java.md
│   │   ├── cpp.md
│   │   └── go.md
│   └── paradigms/              # Paradigm-specific patterns
│       ├── oop.md
│       ├── functional.md
│       ├── reactive.md
│       └── concurrent.md
│
├── examples/                   # Optimization patterns
│   ├── time-optimization.md    # O(n²)→O(n), O(n)→O(log n)
│   ├── space-optimization.md   # O(n)→O(1) patterns
│   └── anti-patterns.md        # Common mistakes
│
├── templates/
│   └── verification.py         # Correctness verification template
│
└── scripts/
    ├── analyze.py              # Multi-language complexity analyzer
    └── benchmark.py            # Performance benchmarking tool
```

## Quick Start

### Installation

```bash
# Clone or copy to your OpenCode skills directory
cp -r code-complexity-optimizer ~/.config/opencode/skills/

# Or project-level
cp -r code-complexity-optimizer your-project/.opencode/skills/
```

### Usage

In OpenCode, mention any optimization-related task:

```
User: 优化这段代码的代码优化
User: This code is too slow, help optimize
User: 这段代码的时间复杂度是多少？
```

### Helper Scripts

```bash
# Install dependencies
pip install lizard radon

# Analyze complexity
python scripts/analyze.py src/utils.py
python scripts/analyze.py ./src --format json --output report.json

# Benchmark performance
python scripts/benchmark.py my_module.py process_data --runs 100
python scripts/benchmark.py original.py func --compare optimized.py func
```

## Optimization Workflow

```
Phase 1: ANALYZE
├── Identify target code
├── Calculate current complexity (time/space)
└── Find bottlenecks

Phase 2: CLARIFY
├── Ask optimization goal (time/space/balanced)
└── Understand constraints

Phase 3: STRATEGIZE
├── Select optimization approach
└── Propose changes with tradeoff analysis

Phase 4: EXECUTE
├── Apply minimal changes
└── Preserve behavior

Phase 5: VERIFY
├── Run tests
├── Compare outputs
└── Generate report
```

## Quick Reference

```
┌─────────────────────────────────────────────┐
│        COMPLEXITY OPTIMIZATION              │
├─────────────────────────────────────────────┤
│ TIME ↓                                      │
│   Nested loops    → Hash map / Set         │
│   Repeated calc   → Memoization            │
│   Linear search   → Binary search (sorted) │
│   Full scan       → Early exit             │
├─────────────────────────────────────────────┤
│ SPACE ↓                                     │
│   New arrays      → In-place modify        │
│   Full list       → Generator/Iterator     │
│   Deep recursion  → Iterative              │
│   Object copies   → References             │
├─────────────────────────────────────────────┤
│ BALANCED                                    │
│   Wrong data struct → Right data struct    │
│   Naive algorithm  → Optimal algorithm     │
└─────────────────────────────────────────────┘
```

## Example

**Input:**
```python
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates
```

**Agent Analysis:**
```
分析结果:
- 时间复杂度: O(n³) - 双重循环 O(n²) × not in 检查 O(n)
- 空间复杂度: O(n) - duplicates 数组
- 瓶颈: 嵌套循环 + 线性查找

优化方案建议:
1. 【优先时间】使用集合去重
   - 时间: O(n²) → O(n)
   - 空间: O(n) (增加一个集合)
   
2. 【平衡优化】使用 Counter
   - 时间: O(n)
   - 空间: O(n)
```

## References

| Category | Files | Description |
|----------|-------|-------------|
| **Languages** | 5 | Python, JS, Java, C++, Go specific patterns |
| **Paradigms** | 4 | OOP, FP, Reactive, Concurrent patterns |
| **Examples** | 3 | Time/Space optimizations, Anti-patterns |

## Integration

Works well with other OpenCode skills:

- `test-driven-debugging` - Verify optimization correctness
- `safe-refactoring` - Complex restructuring
- `code-review-guardian` - Post-optimization quality check

## Limitations

- Cannot modify compiled code or binaries
- Some optimizations require runtime profiling
- Hardware-specific optimizations need target testing

## License

MIT License - See [LICENSE](../../LICENSE)

## Author

user9527448

## Links

- [OpenCode Documentation](https://opencode.ai/docs/skills/)
- [Main Skills Repository](https://github.com/user9527448/opencode-skills)
