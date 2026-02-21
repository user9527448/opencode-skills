---
name: safe-refactoring
description: 系统化重构协议 - 小步前进、验证变更、始终可回退、行为保持
license: MIT
compatibility: opencode
---

# 安全重构

无惧重构。小步前进，每步验证。

---

## 🚨 何时激活此技能

| 触发条件 | 优先级 |
|----------|--------|
| 改进代码结构 | 高 |
| 减少技术债务 | 高 |
| 为新功能准备 | 中 |
| 简化复杂代码 | 中 |
| 理解遗留代码后 | 高 |

---

## 铁律

```
重构 = 行为保持的转换

如果行为变了，那不是重构 - 那是重写。
```

---

## 核心原则

### 1. 🟢 开始前必须全绿

```bash
# 任何重构之前
npm test  # 必须完全通过

# 如果测试失败，先修BUG
# 重构是针对工作代码的
```

### 2. 📏 只做小步

**每步应该：**
- <15分钟内可完成
- 可独立验证
- 易于回滚

```
❌ "重构整个认证模块"
✅ "将密码验证提取为独立函数"
```

### 3. ✅ 每步验证

```bash
# 每次改动后
npm test        # 测试通过？
npm run lint    # 无新警告？
npm run build   # 能编译？
```

### 4. 💾 频繁提交

```bash
# 每次成功验证后
git add .
git commit -m "refactor: [描述单一改动]"

# 创建回滚点
```

---

## 重构工作流

### 阶段1：准备

```markdown
## 重构前检查清单

- [ ] 所有测试通过（全绿）
- [ ] 无未提交的改动
- [ ] 分支干净
- [ ] 我理解代码做什么
- [ ] 此区域有测试
```

### 阶段2：计划

```markdown
## 重构计划

### 目标
[我想改进什么 - 一件事]

### 步骤
1. [步骤1 - <15分钟，可验证]
2. [步骤2 - <15分钟，可验证]
3. [步骤3 - <15分钟，可验证]

### 验证
- [运行哪些测试]
- [需要什么手动检查]
```

### 阶段3：执行（循环）

```
对于每个步骤：
  1. 做一个小的改动
  2. 运行测试
  3. 如果全绿 → 提交
  4. 如果变红 → 立即修复或回滚
  5. 重复直到步骤完成
```

### 阶段4：验证

```bash
# 完整验证
npm test
npm run lint
npm run build
npm run typecheck  # TypeScript

# 让CI验证
git push
```

---

## 重构目录

### 提取函数

**何时：** 代码块有明确目的

**之前：**
```javascript
function processOrder(order) {
  // 20行验证
  if (!order.items || order.items.length === 0) {
    throw new Error('空订单');
  }
  // ...更多验证...
  
  // 实际处理
}
```

**之后：**
```javascript
function processOrder(order) {
  validateOrder(order);
  // 实际处理
}

function validateOrder(order) {
  if (!order.items || order.items.length === 0) {
    throw new Error('空订单');
  }
  // ...验证逻辑...
}
```

**验证：** 测试仍然通过

---

### 重命名变量/函数

**何时：** 名称不能传达意图

**之前：**
```javascript
const d = new Date();
const temp = users.filter(u => u.active);
```

**之后：**
```javascript
const currentDate = new Date();
const activeUsers = users.filter(user => user.isActive);
```

**验证：** 测试 + 类型检查

---

### 提取常量

**何时：** 出现魔法数字

**之前：**
```javascript
if (user.age >= 18) { /* ... */ }
setTimeout(callback, 30000);
```

**之后：**
```javascript
const LEGAL_AGE = 18;
const SESSION_TIMEOUT_MS = 30000;

if (user.age >= LEGAL_AGE) { /* ... */ }
setTimeout(callback, SESSION_TIMEOUT_MS);
```

**验证：** 测试通过

---

### 简化条件

**何时：** 复杂的布尔逻辑

**之前：**
```javascript
if (user && user.isActive && !user.isBanned && user.hasPermission('write')) {
  // ...
}
```

**之后：**
```javascript
function canWrite(user) {
  return user?.isActive 
    && !user.isBanned 
    && user.hasPermission('write');
}

if (canWrite(user)) {
  // ...
}
```

**验证：** 条件路径测试

---

## 红旗 - 立即停止

| 想法 | 现实 | 行动 |
|------|------|------|
| "顺便重构一下这个" | 范围蔓延 | 停止 → 只做一个改动 |
| "测试太慢了" | 危险 | 每次改动后运行测试 |
| "这很简单，不用提交" | 无回滚 | 每步后提交 |
| "测试稍后补" | 危险 | 测试必须先通过 |

---

## 回滚策略

### 未提交的改动
```bash
git checkout -- .
git clean -fd
```

### 上一提交
```bash
git revert HEAD
```

### 找破坏提交
```bash
git bisect start
git bisect bad HEAD
git bisect good <最后好的提交>
```

---

## 小步示例

**目标：** 提取用户验证

```
步骤1：创建空的validateUser()函数
       → 运行测试 → 全绿 → 提交

步骤2：复制验证逻辑到新函数
       → 运行测试 → 全绿 → 提交

步骤3：调用新函数，保留旧代码
       → 运行测试 → 全绿 → 提交

步骤4：删除旧验证代码
       → 运行测试 → 全绿 → 提交

步骤5：删除临时重复
       → 运行测试 → 全绿 → 提交
```

每步：<5分钟，易于回滚。

---

## 快速参考

```
🟢 全绿    → 开始前测试必须通过
📏 小步    → 每次一个微小改动
✅ 验证    → 每次改动后运行测试
💾 提交    → 频繁检查点
🔄 重复    → 继续直到完成

绝不要：
- 跳过运行测试
- 一次做多个改动
- 不提交就重构
- 测试变红后继续
```
