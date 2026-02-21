# OpenCode 开发者技能集

> 一套用于系统化软件开发的 OpenCode 技能集合。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 包含技能

| 技能 | 用途 | 行数 |
|------|------|------|
| 🧪 [test-driven-debugging](.opencode/skills/test-driven-debugging/SKILL.md) | 系统化修复失败测试 | 232 |
| 🔒 [code-review-guardian](.opencode/skills/code-review-guardian/SKILL.md) | 全面代码审查 | 307 |
| 🔧 [safe-refactoring](.opencode/skills/safe-refactoring/SKILL.md) | 零风险代码重构 | 376 |
| 💰 [tokensaver](.opencode/skills/tokensaver/SKILL.md) | 上下文优化策略 | 160 |

## 快速开始

### 方式1: 项目级安装（推荐）

克隆或复制到你的项目：

```bash
# 克隆
git clone https://github.com/user9527448/opencode-skills.git
cp -r opencode-skills/.opencode/skills/* your-project/.opencode/skills/

# 或直接复制
cp -r .opencode/skills/* /path/to/your/project/.opencode/skills/
```

### 方式2: 全局安装

为所有项目安装：

```bash
cp -r .opencode/skills/* ~/.config/opencode/skills/
```

## 使用方法

按需加载技能：

```
skill({ name: "test-driven-debugging" })
skill({ name: "code-review-guardian" })
skill({ name: "safe-refactoring" })
skill({ name: "tokensaver" })
```

## 技能概要

### 🧪 test-driven-debugging（测试驱动调试）

```
流程：
1. READ 测试 → 理解测试的目的
2. RUN 测试 → 隔离失败原因
3. LOG 假设 → 系统化排查
4. FIX 最小化 → 最小的修复改动
5. VERIFY 全部 → 确保无回归
```

**何时使用：** 任何测试失败时

### 🔒 code-review-guardian（代码审查守护）

```
维度（按顺序）：
1. 安全性 → SQL注入、XSS、敏感信息
2. 正确性 → 逻辑、边界情况、错误处理
3. 性能 → N+1查询、内存泄漏、阻塞
4. 可维护性 → 命名、复杂度、DRY
5. 测试 → 覆盖率、边界情况
6. 文档 → API、复杂逻辑
```

**何时使用：** 审查PR或代码时

### 🔧 safe-refactoring（安全重构）

```
原则：
1. GREEN → 开始前测试必须通过
2. SMALL → 每次只做一个小改动
3. VERIFY → 每次改动后运行测试
4. COMMIT → 频繁提交检查点
```

**何时使用：** 改进代码结构时

### 💰 tokensaver（Token节省）

```
策略：
1. 结构化摘要 → 用摘要替换旧消息
2. 工具输出修剪 → 移除重复读取、旧错误
3. 上下文卫生 → 不重复探索相同模式
4. 优先级保留 → 保留P1，压缩P3-P4
```

**何时使用：** 接近Token限制时

## 相关项目

- [opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning) - 自动上下文优化（插件）
- [OpenCode 文档](https://opencode.ai/docs/skills/) - 官方技能文档

## 贡献

欢迎贡献！每个技能遵循此结构：

```yaml
---
name: skill-name
description: 简短描述
license: MIT
compatibility: opencode
---

# 技能内容...
```

## 许可证

MIT
