---
name: skill-structure-organizer
description: 当技能超过500行时，指导将OpenCode技能重组为模块化结构。分析、提取并重组内容到references/、examples/、templates/、scripts/。
license: MIT
compatibility: opencode
metadata:
  author: user9527448
  tags:
    - skill-writing
    - refactoring
    - organization
  triggers:
    - "restructure skill"
    - "skill too long"
    - "organize skill"
    - "模块化skill"
---

# 技能结构组织器

## 概述

当OpenCode技能超过复杂度阈值时，指导从单文件格式重组为模块化目录结构。

## 触发条件

**当以下情况使用此技能：**
- 技能的 SKILL.md 超过 500 行
- 多种语言/范式指南嵌入在单个文件中
- 辅助脚本需要组织
- 用户提及"restructure skill"、"skill too long"、"organize skill"

---

## 核心原则

> **核心工作流保留在 SKILL.md。** 详细参考放入子目录。永远不要混合它们。

---

## 阶段 1: 分析

### 步骤 1.1: 评估当前结构

```bash
# 统计行数
wc -l .opencode/skills/<skill-name>/SKILL.md

# 列出当前文件
find .opencode/skills/<skill-name> -type f
```

### 步骤 1.2: 识别提取候选

| 内容类型 | 是否提取 | 目标目录 |
|----------|----------|----------|
| 语言特定指南 | 是，如果 > 1 种语言 | `references/languages/` |
| 范式特定指南 | 是，如果 > 1 种范式 | `references/paradigms/` |
| 代码示例（> 50 行） | 是 | `examples/` |
| 模板/样板 | 是 | `templates/` |
| 辅助脚本 | 是 | `scripts/` |
| 核心工作流（阶段 1-N） | 否 | 保留在 SKILL.md |
| 快速参考 | 否 | 保留在 SKILL.md |
| 触发条件 | 否 | 保留在 SKILL.md |

### 步骤 1.3: 决策矩阵

```
IF SKILL.md < 400 行:
    → 保持简单结构
    
ELIF SKILL.md < 600 行:
    → 考虑重组，如果：
        - 多种语言指南
        - 多种范式指南
        - 有辅助脚本
        
ELSE (SKILL.md >= 600 行):
    → 必须重组
```

---

## 阶段 2: 创建目录结构

### 步骤 2.1: 创建标准目录

```bash
cd .opencode/skills/<skill-name>

# 创建所有可能的目录
mkdir -p references/languages
mkdir -p references/paradigms
mkdir -p examples
mkdir -p templates
mkdir -p scripts
```

### 步骤 2.2: 目录用途

| 目录 | 内容 | 文件格式 |
|------|------|----------|
| `references/languages/` | 语言特定指南 | `{lang}.md` |
| `references/paradigms/` | 范式特定模式 | `{paradigm}.md` |
| `examples/` | 代码示例、模式 | `{type}-{pattern}.md` |
| `templates/` | 可复用模板 | `{name}.py` 或 `.md` |
| `scripts/` | 可执行助手 | `{name}.py` 或 `.sh` |

---

## 阶段 3: 提取内容

### 步骤 3.1: 提取语言指南

对于 SKILL.md 中的每种语言部分：

1. 创建 `references/languages/{lang}.md`
2. 复制语言特定内容
3. 添加语言名称头部
4. 从 SKILL.md 中删除

### 步骤 3.2: 提取范式指南

同样流程 → `references/paradigms/{paradigm}.md`

### 步骤 3.3: 提取示例

超过 50 行的代码示例 → `examples/{type}.md`

### 步骤 3.4: 移动脚本

```bash
mv *.py scripts/
mv *.sh scripts/
```

---

## 阶段 4: 更新 SKILL.md

### 步骤 4.1: 目标结构

保留在 SKILL.md（~300-400 行）：
- Frontmatter（带 metadata.references）
- 概述
- 触发条件
- 核心原则
- 核心工作流（阶段 1-N）
- 快速参考卡
- 工具集成（简略）
- 参考文件表
- 集成说明
- 警示信号
- 限制

### 步骤 4.2: 添加参考元数据

```yaml
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
```

### 步骤 4.3: 添加参考表

```markdown
## 参考文件

| 类别 | 位置 | 内容 |
|------|------|------|
| **语言指南** | `references/languages/` | Python, JavaScript, Java, C++, Go 指南 |
| **范式指南** | `references/paradigms/` | OOP, FP, 响应式, 并发模式 |
| **示例** | `examples/` | 优化模式前后对比 |
| **模板** | `templates/` | 验证和基准测试模板 |
| **脚本** | `scripts/` | 辅助工具 |
```

---

## 阶段 5: 创建 README.md

### 必需部分

```markdown
# 技能名称

> 简短描述

## 概述
## 功能特性
## 目录结构
## 快速开始
## 安装
## 使用方法
## 快速参考
## 示例
## 参考资料（表格）
## 集成
## 限制
## 许可证
## 作者
## 链接
```

---

## 阶段 6: 验证

### 验证清单

- [ ] SKILL.md 减少到 < 400 行
- [ ] 所有提取内容在正确目录
- [ ] SKILL.md 有参考表
- [ ] metadata.references 添加到 frontmatter
- [ ] README.md 已创建
- [ ] 所有内部链接已更新
- [ ] 脚本移动到 scripts/
- [ ] 全局安装已更新

---

## 快速参考卡

```
┌─────────────────────────────────────────────┐
│        技能重组工作流                        │
├─────────────────────────────────────────────┤
│ 1. 分析                                     │
│    统计行数，识别提取目标                    │
│                                             │
│ 2. 创建                                     │
│    mkdir references/ examples/ scripts/     │
│                                             │
│ 3. 提取                                     │
│    语言 → references/languages/             │
│    范式 → references/paradigms/             │
│    示例 → examples/                         │
│    脚本 → scripts/                          │
│                                             │
│ 4. 更新                                     │
│    添加 metadata.references                 │
│    添加参考表                               │
│    将 SKILL.md 减少到 < 400 行              │
│                                             │
│ 5. 文档                                     │
│    创建 README.md                           │
│                                             │
│ 6. 验证                                     │
│    检查所有清单项                           │
└─────────────────────────────────────────────┘
```

---

## 反模式

| 反模式 | 问题 | 修复 |
|--------|------|------|
| 提取过多 | 核心工作流分散 | 阶段保留在 SKILL.md |
| 没有参考表 | 智能体找不到指南 | 添加表格到 SKILL.md |
| 跳过 README.md | 可发现性差 | 总是创建 README.md |
| 脚本保留在根目录 | 无组织 | 总是使用 scripts/ |

---

## 集成说明

- 在 `SKILL_WRITING_BEST_PRACTICES` 技能之后使用以获取指导
- 与 `safe-refactoring` 配合进行安全重组
- 重组后使用 `code-review-guardian` 进行质量检查

---

## 案例研究：code-complexity-optimizer

### 重组前
```
SKILL.md: 721 行（太长）
脚本：混合在根目录
```

### 重组后
```
SKILL.md: 357 行（-50%）
+ 5 个语言指南在 references/languages/
+ 4 个范式指南在 references/paradigms/
+ 3 个示例文件在 examples/
+ 1 个模板在 templates/
+ 2 个脚本在 scripts/
+ README.md
```

### 关键变更
1. 提取语言特定优化
2. 提取范式特定模式
3. 分离代码示例
4. 添加参考元数据到 frontmatter
5. 创建全面的 README.md
