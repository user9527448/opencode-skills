---
name: safe-refactoring
description: 系统化重构协议 - 小步前进、验证变更、始终可回退
license: MIT
compatibility: opencode
---

# 安全重构

无惧重构。小步前进，每步验证。

## 何时使用

- 改进代码结构但不改变行为
- 减少技术债务
- 为新功能准备代码
- 简化复杂代码

---

## 大爆炸重构的问题

```
❌ 错误：重写一切 → 测试失败 → 找不到哪里坏了 → 放弃
✅ 正确：小改动 → 验证 → 提交 → 重复
```

大型重构会失败，因为难以验证且难以回滚。

---

## 核心原则

### 1. 🟢 开始前必须全绿

**永远不要重构红色测试。**

```bash
# 任何重构之前
npm test  # 必须完全通过
```

如果测试失败，先修bug。重构是针对工作代码的。

---

### 2. 📏 小步前进

**每个重构步骤应该：**

- <15分钟内可完成
- 可独立验证
- 易于回滚

```
❌ 错误："重构整个认证模块"
✅ 正确："将密码验证提取为独立函数"
```

---

### 3. ✅ 每步验证

**每次修改后：**

```bash
# 1. 运行测试
npm test

# 2. 类型检查（如果是TypeScript）
npm run typecheck

# 3. Lint
npm run lint
```

**如果有任何失败：** 停止并在继续前修复。

---

### 4. 💾 频繁提交

**每次成功验证后：**

```bash
git add .
git commit -m "refactor: [描述单一改动]"
```

这创建回滚点。如果需要，随时可以 `git revert`。

---

## 重构目录

### 提取函数

**何时：** 代码块有明确目的

**之前：**
```javascript
function processOrder(order) {
  // 验证订单
  if (!order.items || order.items.length === 0) {
    throw new Error('空订单');
  }
  if (!order.customer) {
    throw new Error('无客户');
  }
  
  // ... 函数其余部分
}
```

**之后：**
```javascript
function processOrder(order) {
  validateOrder(order);
  // ... 函数其余部分
}

function validateOrder(order) {
  if (!order.items || order.items.length === 0) {
    throw new Error('空订单');
  }
  if (!order.customer) {
    throw new Error('无客户');
  }
}
```

**验证：** 测试仍然通过（行为不变）

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

**验证：** 测试 + 类型检查（重命名不应破坏类型）

---

### 提取常量/魔法数字

**何时：** 数字/字符串出现但没有解释

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

**验证：** 条件路径的测试通过

---

### 移除死代码

**何时：** 代码未使用

**步骤：**
1. 搜索所有使用位置
2. 如果没有，删除
3. 验证测试通过

**警告：** 注意：
- 公共API（可能被外部使用）
- 反射/动态调用
- 事件处理器

**验证：** 完整测试套件 + 手动检查边界情况

---

## 重构工作流

### 阶段1: 准备

```markdown
## 重构前检查清单

- [ ] 所有测试通过（全绿）
- [ ] 无未提交的改动
- [ ] 分支是最新的
- [ ] 我理解代码做什么
- [ ] 我有覆盖此区域的测试
```

### 阶段2: 计划

```markdown
## 重构计划

### 目标
[我想改进什么]

### 步骤
1. [步骤1 - 小，可验证]
2. [步骤2 - 小，可验证]
3. [步骤3 - 小，可验证]

### 验证
- [运行哪些测试]
- [需要什么手动检查]
```

### 阶段3: 执行

```
对于每个步骤：
  1. 做改动
  2. 运行测试
  3. 如果通过 → 提交
  4. 如果失败 → 修复或回滚
```

### 阶段4: 验证

```bash
# 完整验证
npm test
npm run lint
npm run typecheck

# 如果有CI
git push  # 让CI验证
```

---

## 验证检查清单

重构后：

- [ ] 所有测试通过
- [ ] 无类型错误（TypeScript）
- [ ] 无lint错误
- [ ] 行为不变（相同输入相同输出）
- [ ] 无引入死代码
- [ ] 公共API变更时文档已更新

---

## 常见陷阱

### ❌ "顺手重构一下"

**问题：** 范围蔓延，混合重构和功能变更

**修复：** 重构和功能分开提交

---

### ❌ "测试太慢，最后再跑"

**问题：** 难以隔离哪个改动破坏了什么

**修复：** 每次改动后运行测试

---

### ❌ "这很简单，不用提交"

**问题：** 出问题时失去回滚点

**修复：** 每次验证后提交

---

### ❌ "测试稍后补"

**问题：** 没有测试覆盖的重构很危险

**修复：** 如果覆盖率低，重构前先加测试

---

## 回滚策略

如果出问题：

### 立即回滚（未提交改动）
```bash
git checkout -- .
git clean -fd
```

### 上一提交回滚
```bash
git revert HEAD
```

### 找出何时坏的
```bash
git bisect start
git bisect bad HEAD
git bisect good <最后已知的好提交>
# Git会二分搜索找出破坏的提交
```

---

## 快速参考

```
🟢 全绿    → 开始前测试必须通过
📏 小步    → 每次一个微小改动
✅ 验证    → 每次改动后运行测试
💾 提交    → 频繁检查点
🔄 重复    → 继续直到完成
```
