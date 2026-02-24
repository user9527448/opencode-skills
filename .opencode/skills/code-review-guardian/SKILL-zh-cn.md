---
name: code-review-guardian
description: OWASP对齐的全面代码审查 - 安全性、正确性、性能、可维护性、测试、文档、架构、并发
license: MIT
compatibility: opencode
metadata:
  references:
    dimensions: references/dimensions/
    examples: examples/
    templates: templates/
    scripts: scripts/
---

# Code Review Guardian

像资深工程师一样审查代码。安全第一，永远如此。输出标准化报告。

---

## 🚨 何时激活此技能

| 触发条件 | 优先级 |
|---------|----------|
| Pull Request 审查 | 高 |
| 合并前检查 | 高 |
| 安全审计 | 关键 |
| 实现后审查 | 中 |
| 代码质量检查 | 中 |

---

## 📋 执行工作流

### 步骤 1: 确定范围
```
1. 识别变更文件 (git diff, PR文件列表)
2. 确定审查深度 (quick/full/security-only)
3. 记录语言/框架上下文
```

### 步骤 2: 自动化扫描 (使用工具)
```
1. LSP诊断 → 类型错误、lint问题
2. AST-grep → 基于模式的安全/质量检查
3. Grep → 查找TODOs、FIXMEs、硬编码值
4. 运行 auto-scan.py → 快速安全扫描
```

### 步骤 3: 人工审查 (按维度)
```
审查顺序: 安全性 → 正确性 → 架构 → 性能 
         → 可维护性 → 并发 → 测试 → 文档
         
使用 references/dimensions/ 获取每个维度的详细指导
```

### 步骤 4: 生成报告
```
使用 templates/report-template.md 生成标准化输出
```

---

## 审查维度 (关键 → 锦上添花)

```
1. 🔒 安全性      → 始终第一
2. 🎯 正确性       → 能工作吗?
3. 🏗️ 架构  → 设计模式、SOLID
4. ⚡ 性能    → 有瓶颈吗?
5. 🧹 可维护性 → 可读? DRY?
6. 🔄 并发   → 线程/进程安全?
7. ♿ 无障碍 → 前端无障碍
8. 🧪 测试       → 覆盖了吗?
9. 📚 文档 → 更新了吗?
```

---

## 快速参考卡

```
📋 执行顺序
1. 范围 → 2. 自动化扫描 → 3. 人工审查 → 4. 报告

🔒 安全性    → 始终第一
   □ 注入风险 (SQL, CMD, XSS)
   □ 认证/授权缺口
   □ 代码中的密钥
   □ 输入验证

🎯 正确性 → 按预期工作?
   □ 边界情况 (null, empty, boundary)
   □ 错误处理
   □ 类型安全

🏗️ 架构 → 设计良好?
   □ SOLID原则
   □ 无循环依赖
   □ 关注点分离

⚡ 性能  → 可扩展?
   □ N+1 查询
   □ 内存泄漏
   □ 阻塞I/O

🧹 可维护性 → 可读?
   □ 命名清晰度
   □ 复杂度 < 10
   □ DRY原则

🔄 并发 → 线程安全?
   □ 竞态条件
   □ 正确的锁

♿ 无障碍 → A11y合规?
   □ Alt文本
   □ 键盘导航
   □ 颜色对比

🧪 测试     → 覆盖?
   □ 新代码的新测试
   □ 边界情况已测试
   □ 所有测试通过

📚 文档        → 更新?
   □ API文档
   □ README更新
   □ 重大变更已记录

📊 输出 → 使用 templates/report-template.md
```

---

## 📁 目录结构

```
code-review-guardian/
├── SKILL.md
├── references/
│   └── dimensions/
│       ├── security.md        # OWASP Top 10, 漏洞模式
│       ├── correctness.md     # 逻辑验证, 错误处理
│       ├── architecture.md    # SOLID原则, 设计模式
│       ├── performance.md     # N+1, 内存, 算法
│       ├── maintainability.md # 命名, 复杂度, 代码异味
│       ├── concurrency.md     # 线程安全, 竞态条件
│       ├── accessibility.md   # WCAG 2.1, ARIA
│       ├── testing.md         # 测试质量, 模式
│       └── documentation.md   # JSDoc, 注释
├── examples/
│   └── scenarios/
│       ├── rest-api-review.md    # API审查场景
│       └── frontend-component.md  # React组件场景
├── templates/
│   ├── report-template.md     # 标准审查报告格式
│   └── checklist-all.md       # 完整审查检查清单
└── scripts/
    └── auto-scan.py          # 自动化安全扫描器
```

---

## 📖 参考文件

| 类别 | 位置 | 内容 |
|----------|----------|----------|
| **维度** | `references/dimensions/` | 9个详细审查维度指南 |
| **场景** | `examples/scenarios/` | 真实世界审查示例 |
| **模板** | `templates/` | 报告模板, 完整检查清单 |
| **脚本** | `scripts/` | 自动化扫描工具 |

---

## 反馈原则

### ❌ 糟糕的反馈
```
"这是错的"
"LGTM"
"你为什么这样做?"
```

### ✅ 好的反馈
```
"[CRIT-001] auth.ts:45 存在SQL注入漏洞
使用参数化查询代替字符串拼接:
cursor.query('SELECT * FROM users WHERE id = ?', [userId])
参考: OWASP A03:2021"
```

**好的反馈是:**
- 具体的 (文件:行号)
- 建设性的 (提出解决方案)
- 有解释的 (为什么重要)
- 有分类的 (严重程度 + 类别)
- 可执行的 (明确的下一步)

---

## 集成说明

- 使用 `scripts/auto-scan.py` 进行快速自动化检查
- 遵循维度顺序 (安全性第一!)
- 始终使用报告模板保持一致输出
- 查看 `examples/scenarios/` 了解真实模式

---

## 限制

- 自动化扫描只是启发式 - 仍需人工审查
- 无法检测业务逻辑错误
- 无法验证安全控制有效性
- 无障碍审查仅限前端代码
- 性能基准测试需要实际负载测试
