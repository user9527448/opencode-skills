# Code Review Guardian

> 面向 AI 编码代理人的 OWASP 对齐全面代码审查技能。

## 概述

Code Review Guardian 提供了一个系统化的代码审查框架，涵盖 9 个关键维度。它以安全为首要原则，并生成标准化的 Markdown 报告。

## 功能特性

- **9 大审查维度**：安全、正确性、架构、性能、可维护性、并发、无障碍、测试、文档
- **标准化报告**：统一的 Markdown 格式，包含严重级别
- **自动化扫描**：内置脚本用于快速安全检查
- **真实案例**：包含实用的审查场景示例
- **全面检查清单**：每个维度的详细检查清单

## 目录结构

```
code-review-guardian/
├── SKILL.md                           # 主技能文件 (217 行)
├── references/
│   └── dimensions/                     # 详细维度指南
│       ├── security.md                 # OWASP Top 10，漏洞模式
│       ├── correctness.md             # 逻辑验证，错误处理
│       ├── architecture.md            # SOLID 原则，设计模式
│       ├── performance.md             # N+1 问题，内存，算法
│       ├── maintainability.md         # 命名，复杂度，代码异味
│       ├── concurrency.md             # 线程安全，竞争条件
│       ├── accessibility.md           # WCAG 2.1，ARIA
│       ├── testing.md                 # 测试质量，模式
│       └── documentation.md           # JSDoc，注释
├── examples/
│   └── scenarios/
│       ├── rest-api-review.md         # REST API 审查示例
│       └── frontend-component.md       # React 组件示例
├── templates/
│   ├── report-template.md             # 标准审查报告格式
│   └── checklist-all.md               # 完整审查检查清单
└── scripts/
    └── auto-scan.py                   # 自动化安全扫描器
```

## 快速开始

### 加载技能

```javascript
skill({ name: "code-review-guardian" })
```

### 审查工作流

1. **范围定义**：识别文件并确定审查深度
2. **自动化扫描**：运行 LSP 诊断、AST-grep、auto-scan.py
3. **人工审查**：按顺序遵循 9 个维度（安全优先！）
4. **生成报告**：使用 templates/report-template.md

### 使用示例

```bash
# 运行自动化扫描
python scripts/auto-scan.py /path/to/code --format=markdown

# 审查特定文件
# 加载技能并审查 PR 变更
```

## 审查维度

| 维度 | 优先级 | 描述 |
|-----------|----------|-------------|
| 🔒 安全 | 关键 | OWASP Top 10，漏洞 |
| 🎯 正确性 | 高 | 逻辑，边界情况，错误 |
| 🏗️ 架构 | 高 | SOLID，设计模式 |
| ⚡ 性能 | 中 | N+1，内存，算法 |
| 🧹 可维护性 | 中 | 命名，复杂度，DRY |
| 🔄 并发 | 中 | 线程安全，竞争条件 |
| ♿ 无障碍 | 中 | WCAG 2.1，ARIA |
| 🧪 测试 | 低 | 覆盖率，测试质量 |
| 📚 文档 | 低 | JSDoc，注释 |

## 报告格式

使用标准报告模板：

```markdown
# 代码审查报告

## 执行摘要
| 指标 | 数量 |
|--------|-------|
| 🔴 严重 | {n} |
| 🟠 高 | {n} |
| 🟡 中 | {n} |
| 🟢 低 | {n} |

## 🔴 严重问题
## 🟠 高优先级问题
## 🟡 中优先级问题
## 🟢 低优先级 / 挑剔
## ✅ 做得好的方面
## 📋 检查清单摘要
## 🔧 建议行动
```

## 集成

- 与 `safe-refactoring` 配合用于审查后的改进
- 与 `test-driven-debugging` 配合验证修复
- 与 `code-complexity-optimizer` 配合进行性能审查

## 许可证

MIT

## 作者

user9527448
