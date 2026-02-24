# Code Review Guardian

> OWASP-aligned comprehensive code review skill for AI coding agents.

## Overview

Code Review Guardian provides a systematic framework for conducting thorough code reviews across 9 critical dimensions. It emphasizes security first and produces standardized markdown reports.

## Features

- **9 Review Dimensions**: Security, Correctness, Architecture, Performance, Maintainability, Concurrency, Accessibility, Testing, Documentation
- **Standardized Reports**: Consistent markdown format with severity levels
- **Automated Scanning**: Built-in script for quick security checks
- **Real-world Examples**: Practical review scenarios included
- **Comprehensive Checklists**: Detailed checklists for each dimension

## Directory Structure

```
code-review-guardian/
├── SKILL.md                           # Main skill file (217 lines)
├── references/
│   └── dimensions/                     # Detailed dimension guides
│       ├── security.md                 # OWASP Top 10, vulnerability patterns
│       ├── correctness.md             # Logic verification, error handling
│       ├── architecture.md            # SOLID principles, design patterns
│       ├── performance.md             # N+1, memory, algorithms
│       ├── maintainability.md         # Naming, complexity, code smells
│       ├── concurrency.md             # Thread safety, race conditions
│       ├── accessibility.md           # WCAG 2.1, ARIA
│       ├── testing.md                 # Test quality, patterns
│       └── documentation.md           # JSDoc, comments
├── examples/
│   └── scenarios/
│       ├── rest-api-review.md         # REST API review example
│       └── frontend-component.md       # React component example
├── templates/
│   ├── report-template.md             # Standard review report format
│   └── checklist-all.md               # Complete review checklist
└── scripts/
    └── auto-scan.py                   # Automated security scanner
```

## Quick Start

### Load the Skill

```javascript
skill({ name: "code-review-guardian" })
```

### Review Workflow

1. **Scope Definition**: Identify files and determine review depth
2. **Automated Scans**: Run LSP diagnostics, AST-grep, auto-scan.py
3. **Manual Review**: Follow 9 dimensions in order (Security first!)
4. **Generate Report**: Use templates/report-template.md

### Example Usage

```bash
# Run automated scan
python scripts/auto-scan.py /path/to/code --format=markdown

# Review specific files
# Load skill and review PR changes
```

## Review Dimensions

| Dimension | Priority | Description |
|-----------|----------|-------------|
| 🔒 Security | CRITICAL | OWASP Top 10, vulnerabilities |
| 🎯 Correctness | HIGH | Logic, edge cases, errors |
| 🏗️ Architecture | HIGH | SOLID, design patterns |
| ⚡ Performance | MEDIUM | N+1, memory, algorithms |
| 🧹 Maintainability | MEDIUM | Naming, complexity, DRY |
| 🔄 Concurrency | MEDIUM | Thread safety, race conditions |
| ♿ Accessibility | MEDIUM | WCAG 2.1, ARIA |
| 🧪 Testing | LOW | Coverage, test quality |
| 📚 Documentation | LOW | JSDoc, comments |

## Report Format

Use the standard report template:

```markdown
# Code Review Report

## Executive Summary
| Metric | Count |
|--------|-------|
| 🔴 Critical | {n} |
| 🟠 High | {n} |
| 🟡 Medium | {n} |
| 🟢 Low | {n} |

## 🔴 Critical Issues
## 🟠 High Priority Issues
## 🟡 Medium Priority Issues
## 🟢 Low Priority / Nitpicks
## ✅ What's Done Well
## 📋 Checklist Summary
## 🔧 Recommended Actions
```

## Integration

- Works with `safe-refactoring` for post-review improvements
- Use with `test-driven-debugging` to verify fixes
- Combine with `code-complexity-optimizer` for performance reviews

## License

MIT

## Author

user9527448
