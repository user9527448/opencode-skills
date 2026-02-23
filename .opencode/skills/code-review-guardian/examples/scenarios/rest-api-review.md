# Review Scenario: REST API Endpoint

## Context
Reviewing a new REST API endpoint for user data access.

## Code Under Review

```javascript
// routes/user.js
const express = require('express')
const router = express.Router()
const db = require('../db')

// Get user by ID
router.get('/users/:id', async (req, res) => {
  const user = await db.query(
    'SELECT * FROM users WHERE id = ' + req.params.id
  )
  res.json(user)
})

// Update user
router.put('/users/:id', async (req, res) => {
  await db.query(
    'UPDATE users SET name = ?, email = ? WHERE id = ?',
    [req.body.name, req.body.email, req.params.id]
  )
  res.json({ success: true })
})

// Get user's orders
router.get('/users/:id/orders', async (req, res) => {
  const orders = []
  const user = await db.query('SELECT * FROM users WHERE id = ?', [req.params.id])
  
  const orderIds = await db.query('SELECT order_id FROM user_orders WHERE user_id = ?', [req.params.id])
  for (const o of orderIds) {
    const order = await db.query('SELECT * FROM orders WHERE id = ?', [o.order_id])
    orders.push(order)
  }
  
  res.json(orders)
})

module.exports = router
```

---

## Findings

### 🔴 Critical Issues

#### CRIT-001: SQL Injection
- **Category**: Security
- **File**: `routes/user.js:12`
- **Issue**: Direct string concatenation in SQL query
- **Impact**: Attacker can inject malicious SQL
- **Code**:
  ```javascript
  'SELECT * FROM users WHERE id = ' + req.params.id
  ```
- **Fix**: Use parameterized queries
  ```javascript
  db.query('SELECT * FROM users WHERE id = ?', [req.params.id])
  ```

#### CRIT-002: Missing Authentication
- **Category**: Security
- **File**: `routes/user.js:11`
- **Issue**: No authentication middleware
- **Impact**: Anyone can access any user's data (IDOR)
- **Fix**: Add auth middleware
  ```javascript
  router.get('/users/:id', requireAuth, async (req, res) => {
  ```

#### CRIT-003: Missing Authorization
- **Category**: Security
- **File**: `routes/user.js:11, 20, 31`
- **Issue**: No check if user can access this resource
- **Impact**: Users can access other users' data
- **Fix**: Verify ownership
  ```javascript
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Access denied' })
  }
  ```

---

### 🟠 High Issues

#### HIGH-001: N+1 Query Problem
- **Category**: Performance
- **File**: `routes/user.js:35-42`
- **Issue**: Query in loop for user's orders
- **Impact**: O(n) database queries
- **Fix**: Use JOIN or batch query
  ```javascript
  const orders = await db.query(`
    SELECT o.* FROM orders o
    JOIN user_orders uo ON o.id = uo.order_id
    WHERE uo.user_id = ?
  `, [req.params.id])
  ```

#### HIGH-002: No Input Validation
- **Category**: Correctness
- **File**: `routes/user.js:20-23`
- **Issue**: No validation on name/email
- **Impact**: Invalid data stored in database
- **Fix**: Add validation
  ```javascript
  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Invalid email' })
  }
  ```

---

### 🟡 Medium Issues

#### MED-001: Missing Error Handling
- **Category**: Correctness
- **File**: Multiple
- **Issue**: No try/catch blocks
- **Impact**: Unhandled exceptions crash server
- **Fix**: Add error handling

#### MED-002: Generic Error Messages
- **Category**: Security
- **File**: `routes/user.js:25`
- **Issue**: Error details may leak to client
- **Fix**: Return generic errors to client, log details

---

### 🟢 Low Issues

- Missing rate limiting
- No request logging
- Inconsistent response format (array vs object)

---

## Report Generated

This scenario demonstrates the comprehensive review process with:
- 3 Critical security issues (SQL injection, auth, authorization)
- 2 High performance/correctness issues
- 2 Medium issues
- Multiple low priority improvements
