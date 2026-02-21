# OpenCode 开发者技能集

> 一套用于系统化软件开发的 OpenCode 技能集合。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 包含技能

| 技能 | 用途 | 行数 |
|------|------|------|
| 🧪 [test-driven-debugging](.opencode/skills/test-driven-debugging/SKILL.md) | 系统化修复失败测试 | 232 |
| 🔒 [code-review-guardian](.opencode/skills/code-review-guardian/SKILL.md) | 全面代码审查 | 307 |
| 🔧 [safe-refactoring](.opencode/skills/safe-refactoring/SKILL.md) | 零风险代码重构 | 376 |
| 🚀 [code-complexity-optimizer](.opencode/skills/code-complexity-optimizer/SKILL.md) | 算法复杂度优化 | 357 |
| 📁 [skill-structure-organizer](.opencode/skills/skill-structure-organizer/SKILL.md) | 重构技能为模块化格式 | 220 |
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

### 技能如何工作

技能是加载到 OpenCode 上下文中的**指导文档**。它们告诉 AI 代理如何处理特定任务。

```
┌─────────────────────────────────────────────────────────┐
│  用户: "我的测试失败了，帮我修一下"                        │
│                                                         │
│  OpenCode: 加载 test-driven-debugging 技能              │
│            → 现在知道系统化的调试流程                      │
│            → 遵循: READ → RUN → LOG → FIX → VERIFY       │
└─────────────────────────────────────────────────────────┘
```

### 加载技能

在 OpenCode 中，通过调用以下方式加载技能：

```
skill({ name: "test-driven-debugging" })
skill({ name: "code-review-guardian" })
skill({ name: "safe-refactoring" })
skill({ name: "code-complexity-optimizer" })
skill({ name: "skill-structure-organizer" })
skill({ name: "tokensaver" })
```

**自动加载的触发条件：**
- 你提到相关任务（如"测试失败了"）
- OpenCode 检测到需要某个技能
- 你明确要求加载某个技能

### 何时使用每个技能

| 场景 | 加载技能 |
|------|----------|
| "测试X失败了" | test-driven-debugging |
| "审查这个PR" | code-review-guardian |
| "重构模块Y" | safe-refactoring |
| "代码优化" | code-complexity-optimizer |
| "技能太长" / "重组技能" | skill-structure-organizer |
| "上下文太大了" | tokensaver |

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

### 🚀 code-complexity-optimizer（代码复杂度优化）

```
流程：
1. ANALYZE 分析 → 确定当前时间/空间复杂度
2. CLARIFY 明确 → 询问优化目标（时间、空间或平衡）
3. STRATEGIZE 策略 → 选择优化方法
4. EXECUTE 执行 → 应用最小改动
5. VERIFY 验证 → 确认正确性和复杂度改进

优化策略：
- 时间优化：哈希表、记忆化、二分查找、提前退出
- 空间优化：原地操作、迭代器、流式处理
- 平衡优化：最优数据结构、算法替换
```

**何时使用：** 基于复杂度优化算法

### 📁 skill-structure-organizer（技能结构组织）

```
流程：
1. ANALYZE 分析 → 统计行数，识别提取目标
2. CREATE 创建 → mkdir references/ examples/ scripts/
3. EXTRACT 提取 → 语言、范式、示例到子目录
4. UPDATE 更新 → 添加 metadata.references，精简 SKILL.md
5. DOCUMENT 文档 → 创建 README.md
6. VERIFY 验证 → 检查所有清单项

何时重组：
- SKILL.md > 500 行
- 多种语言/范式指南
- 有辅助脚本
```

**何时使用：** 将技能重组为模块化格式

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
