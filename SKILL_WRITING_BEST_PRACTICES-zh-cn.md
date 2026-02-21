# OpenCode 技能编写最佳实践

> 编写高质量 OpenCode 技能的研究发现和指南。

---

## 官方要求摘要

### 文件结构

```
.opencode/skills/
└── <skill-name>/
    └── SKILL.md              # 必需：精确的文件名
```

### Frontmatter 要求

| 字段 | 必需 | 规则 |
|------|------|------|
| `name` | ✅ 是 | 1-64 字符，小写字母数字 + 单连字符，无前导/尾随/连续 `--`，必须与目录名匹配 |
| `description` | ✅ 是 | 1-1024 字符，足够具体以便代理正确选择 |
| `license` | ❌ 可选 | SPDX 标识符（如 MIT, Apache-2.0） |
| `compatibility` | ❌ 可选 | 目标平台（如 opencode） |
| `metadata` | ❌ 可选 | 字符到字符串的映射，用于自定义数据 |

### 名称验证正则

```
^[a-z0-9]+(-[a-z0-9]+)*$
```

**有效示例：**
- `test-driven-debugging`
- `code-review-guardian`
- `git-release`

**无效示例：**
- `Test-Debugging`（大写）
- `test_debugging`（下划线）
- `-test-debugging`（前导连字符）
- `test--debugging`（连续连字符）

---

## 研究得出的最佳实践

### 1. 清晰的触发条件

**差的写法：**
```markdown
This skill helps with debugging.
```

**好的写法：**
```markdown
## When to Use Me
- Any test is failing
- CI/CD pipeline is red
- "Works on my machine" issues
- Flaky test detection
```

**原因：** 代理需要明确的条件来知道何时加载技能。

### 2. 结构化的章节

推荐的顺序结构：

```markdown
---
name: skill-name
description: 清晰、具体的描述（1-1024 字符）
---

# 技能标题

[核心原则或"电梯演讲"]

## When to Activate（何时激活）
[明确的触发条件]

## Core Principle / The Iron Law（核心原则/铁律）
[最重要的规则]

## Step-by-Step Process（分步流程）
[编号的阶段或步骤]

## Quick Reference（快速参考）
[简洁的检查清单]

## Anti-Patterns / Red Flags（反模式/警示信号）
[不应该做什么]

## Integration（集成）
[此技能如何与其他技能配合]
```

### 3. 保持提示聚焦

**差的写法：**
```markdown
You are an expert developer who knows everything about code quality,
security, performance, and can help with any programming task...
```

**好的写法：**
```markdown
You are a code reviewer focused on security vulnerabilities.

Review code for:
1. SQL injection risks
2. XSS vulnerabilities
3. Hardcoded secrets
4. Authentication flaws
```

**原因：** 聚焦的提示产生更一致、可预测的行为。

### 4. 在提示中包含示例

**无示例：**
```markdown
Report any issues found.
```

**有示例：**
```markdown
Report issues in this format:

| Severity | File | Line | Issue | Fix |
|----------|------|------|-------|-----|
| Critical | auth.ts | 42 | SQL injection | Use parameterized query |

Example:
| Critical | db.ts | 15 | Hardcoded password | Use process.env.DB_PASSWORD |
```

**原因：** 示例建立预期的输出格式和质量水平。

### 5. 使用模板和检查清单

模板使技能更具可操作性：

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

### 6. 提供快速参考卡

代理需要快速访问关键信息：

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

### 7. 包含反模式

告诉代理不应该做什么：

```markdown
## 🛑 Red Flags - Stop Immediately

| Thought | Reality | Action |
|---------|---------|--------|
| "Let me just try this fix" | Guessing | STOP → Do Phase 1 |
| "Maybe increase timeout" | Masking symptom | Find root cause |
```

### 8. 使用视觉层次

```markdown
# Main Title (H1)
## Section (H2)
### Subsection (H3)

- Bullet points for lists
1. Numbered for sequences

| Tables | For | Comparisons |
|--------|-----|-------------|

```code blocks for examples```

**提示：** 谨慎使用表情符号进行强调：
- 🚨 严重警告
- ✅ 好的模式
- ❌ 坏的模式
- ⚠️ 重要说明
```

---

## 内容长度指南

| 组件 | 推荐长度 |
|------|----------|
| 描述 | 20-160 字符 |
| 核心原则 | 1-2 句话 |
| 触发条件 | 3-6 项 |
| 每个阶段/步骤 | 50-200 词 |
| 快速参考 | 5-15 行 |
| 技能总行数 | 200-400 行 |

**为什么长度很重要：**
- 太短：指导不足
- 太长：代理不会遵循所有指令
- 最佳：足够详细，可扫描的结构

---

## 验证检查清单

发布技能前，验证：

### Frontmatter
- [ ] `name` 与目录名完全匹配
- [ ] `name` 遵循命名约定（小写，仅连字符）
- [ ] `description` 为 20-1024 字符
- [ ] `description` 足够具体以便选择
- [ ] 可选字段有有效值

### 内容
- [ ] 定义了明确的触发条件
- [ ] 提供了分步流程
- [ ] 关键概念包含示例
- [ ] 有快速参考/摘要
- [ ] 记录了反模式
- [ ] 适用时提供了模板

### 结构
- [ ] 逻辑流程（何时 → 什么 → 如何）
- [ ] 标题创建清晰的层次结构
- [ ] 表格用于比较
- [ ] 代码块用于示例
- [ ] 列表项简洁

---

## 常见错误避免

### 1. 名称/目录不匹配

```
❌ Directory: code-review/
   Frontmatter: name: code-review-guardian

✅ Directory: code-review-guardian/
   Frontmatter: name: code-review-guardian
```

### 2. 模糊的描述

```
❌ description: Helps with code review

✅ description: OWASP-aligned code review for security, 
   performance, and maintainability issues
```

### 3. 缺少触发条件

```
❌ # Code Review
   This skill helps review code.

✅ # Code Review Guardian
   ## When to Activate
   - Pull request review
   - Pre-merge security check
   - Code quality audit
```

### 4. 没有示例

```
❌ Fix any issues you find.

✅ ## Example Fix
   Before: const apiKey = "sk-abc123"
   After: const apiKey = process.env.API_KEY
```

### 5. 缺少快速参考

```
❌ (Only verbose explanations)

✅ ## Quick Reference
   🔒 Security → First, always
   🎯 Correctness → Does it work?
   ⚡ Performance → Any N+1?
```

---

## 我们技能的示例

### test-driven-debugging

**优势：**
- 清晰的"铁律"原则
- 四阶段框架
- 常见失败的模式库
- 失败修复的三次规则
- 警示信号表

**结构：**
```
Trigger Conditions → Iron Law → Phase 1-4 → Red Flags → Quick Reference
```

### code-review-guardian

**优势：**
- 优先级排序的维度（安全第一）
- OWASP Top 10 参考表
- 安全/危险的代码模式
- 审查输出模板
- 反馈原则

**结构：**
```
Review Order → Security (OWASP) → Correctness → Performance → 
Maintainability → Testing → Output Template
```

### safe-refactoring

**优势：**
- 核心原则（GREEN, SMALL, VERIFY, COMMIT）
- 带前后对比的重构目录
- 本地重构列表（最安全的操作）
- 回滚策略
- 小步骤示例

**结构：**
```
Iron Law → Core Principles → Workflow → Catalog → 
Red Flags → Rollback → Quick Reference
```

### tokensaver

**优势：**
- 基于优先级的保留表（P1-P4）
- 带 token 计数的前后示例
- Token 估算参考
- 与插件的集成说明

**结构：**
```
When to Activate → Core Principle → Strategies 1-4 → 
Practical Application → Anti-Patterns → Quick Reference
```

---

## 进阶文件结构（复杂技能推荐）

当技能超过 500-800 行或需要模板/脚本/参考时，使用此模块化结构：

### 目录模板

```
.opencode/skills/<skill-name>/
├── SKILL.md                    # 核心指令（~300-400 行）
│                               # 包含：触发条件、核心原则、工作流、快速参考
│
├── references/                 # 详细参考指南
│   ├── languages/              # 语言特定指南
│   │   ├── python.md
│   │   ├── javascript.md
│   │   └── ...
│   └── paradigms/              # 范式特定模式
│       ├── oop.md
│       ├── functional.md
│       └── ...
│
├── examples/                   # 优化/示例模式
│   ├── time-optimization.md
│   ├── space-optimization.md
│   └── anti-patterns.md
│
├── templates/                  # 可复用模板
│   └── verification.py
│
├── scripts/                    # 可执行辅助脚本
│   ├── analyze.py
│   └── benchmark.py
│
└── README.md                   # 技能文档
```

### 何时使用进阶结构

| 条件 | 简单结构 | 进阶结构 |
|------|----------|----------|
| SKILL.md 行数 | < 400 | > 500 |
| 需要语言指南 | 否 | 是（多种） |
| 辅助脚本 | 否 | 是 |
| 代码示例 | 少量内联 | 多个独立文件 |
| 模板 | 无 | 可复用模板 |

### 进阶技能的 SKILL.md 结构

保持 SKILL.md 聚焦于核心工作流：

```markdown
---
name: skill-name
description: 简短描述
metadata:
  references:
    languages: references/languages/
    paradigms: references/paradigms/
    examples: examples/
    templates: templates/
    scripts: scripts/
---

# Skill Title

## Overview
## Trigger Conditions
## The Iron Law
## Phase 1: ...
## Phase 2: ...
## Phase 3: ...
## Quick Reference Card
## Tool Integration
## Reference Files (指向子目录的表格)
## Integration Notes
## Red Flags
## Limitations
```

### 进阶结构的好处

| 好处 | 描述 |
|------|------|
| **聚焦的 SKILL.md** | 代理更容易遵循核心工作流 |
| **按需加载** | 详细指南仅在需要时加载 |
| **可维护性** | 每个文件单一职责 |
| **可扩展性** | 容易添加新语言/范式 |
| **可复用性** | 脚本和模板可导入 |

---

## 案例研究：code-complexity-optimizer 重组

### 重组前（单文件）

```
code-complexity-optimizer/
├── SKILL.md          (721 行)
├── SKILL-zh-cn.md    (721 行)
├── analyze.py        (424 行)
└── benchmark.py      (301 行)
```

**问题：**
- SKILL.md 太长（721 行 > 400 行指南）
- 语言特定指南埋在单个文件中
- 核心工作流和参考之间没有分离

### 重组后（模块化结构）

```
code-complexity-optimizer/
├── SKILL.md                    (357 行) ← 减少 50%
├── SKILL-zh-cn.md              (357 行)
├── README.md                   (144 行)
│
├── references/
│   ├── languages/
│   │   ├── python.md           (76 行)
│   │   ├── javascript.md       (89 行)
│   │   ├── java.md             (72 行)
│   │   ├── cpp.md              (77 行)
│   │   └── go.md               (74 行)
│   └── paradigms/
│       ├── oop.md              (69 行)
│       ├── functional.md       (68 行)
│       ├── reactive.md         (73 行)
│       └── concurrent.md       (91 行)
│
├── examples/
│   ├── time-optimization.md    (95 行)
│   ├── space-optimization.md   (91 行)
│   └── anti-patterns.md        (123 行)
│
├── templates/
│   └── verification.py         (226 行)
│
└── scripts/
    ├── analyze.py              (424 行)
    └── benchmark.py            (301 行)
```

### 重组过程

**步骤 1：分析当前 SKILL.md**
- 识别可以提取的部分
- 按类别分组（语言、范式、示例）

**步骤 2：创建目录结构**
```bash
mkdir -p references/languages references/paradigms
mkdir -p examples templates scripts
```

**步骤 3：提取内容**
- 语言指南 → `references/languages/*.md`
- 范式指南 → `references/paradigms/*.md`
- 优化模式 → `examples/*.md`
- 移动脚本 → `scripts/`

**步骤 4：更新 SKILL.md**
- 保留核心工作流（阶段 1-5）
- 添加指向子目录的参考表
- 添加 `metadata references:` 以便自动发现

**步骤 5：创建 README.md**
- 概述和功能
- 安装说明
- 快速参考
- 详细指南链接

### 结果

| 指标 | 重组前 | 重组后 | 变化 |
|------|--------|--------|------|
| SKILL.md 行数 | 721 | 357 | **-50%** |
| 总文件数 | 4 | 18 | +14 |
| 模块化 | 低 | 高 | ✅ |
| 可维护性 | 低 | 高 | ✅ |

---

## 参考资料

### 官方文档
- [OpenCode Agent Skills](https://opencode.ai/docs/skills/)
- [malhashemi/opencode-skills](https://github.com/malhashemi/opencode-skills)

### 社区资源
- [AI Skill Market - SKILL.md Format Guide](https://aiskill.market/blog/claude-code-skill-md-format)
- [Context Engineering Guide](https://promptbuilder.cc/blog/context-engineering-agents-guide-2025)

### 相关技能参考
- [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)
- [systematic-debugging (Claudetory)](https://claudetory.com/skills/systematic-debugging)

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.1.0 | 2026-02-21 | 添加进阶文件结构模板和案例研究 |
| 1.0.0 | 2026-02-21 | 初始研究汇编 |
