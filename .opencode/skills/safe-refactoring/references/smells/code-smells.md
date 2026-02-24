# Code Smells Reference

A comprehensive guide to identifying and addressing code smells.

---

## What is a Code Smell?

A code smell is a surface indication that usually corresponds to a deeper problem in the system. Not all code smells need to be "fixed" - they are hints that something may warrant closer inspection.

---

## The Smell → Fix Mapping

| Smell | Symptoms | Fix |
|-------|----------|-----|
| **Long Method** | >50 lines, too many responsibilities | Extract Method |
| **Large Class** | >500 lines, too many fields/methods | Extract Class |
| **Duplicate Code** | Same code in multiple places | Extract Function, Pull Up |
| **Feature Envy** | Method uses another class more than its own | Move Method, Extract Function |
| **Data Clumps** | Same parameters together everywhere | Introduce Parameter Object, Extract Class |
| **Primitive Obsession** | Using primitives for domain concepts | Replace Primitive with Object |
| **Switch Statements** | Multiple type checks | Polymorphism, Replace Conditional |
| **Parallel Inheritance** | Similar hierarchies | Move Method, Pull Up |
| **Lazy Class** | Does too little | Inline Class, Remove Dead Code |
| **Speculative Generality** | Unused code | Remove Dead Code |
| **Temporary Field** | Fields sometimes null | Extract Class |
| **Message Chains** | a.b().c().d() | Hide Delegate |
| **Middle Man** | Just delegates | Remove Middle Man |
| **Inappropriate Intimacy** | Classes tightly coupled | Move Method, Change Bidirectional |
| **Alternative Classes** | Same interface, different impl | Extract Interface |

---

## Detailed Smell Descriptions

### Long Method

**Symptoms:**
- Method is >50 lines
- Too many comments (each comment = "explain this block")
- Multiple levels of nesting
- Too many parameters

**Why it's bad:**
- Hard to understand
- Hard to test
- Hard to reuse

**Example:**
```javascript
// BAD: 40 lines, does too much
function processOrder(order) {
  // Validation (10 lines)
  if (!order.items || order.items.length === 0) {
    throw new Error('No items');
  }
  // ... more validation
  
  // Calculation (10 lines)
  let total = 0;
  for (const item of order.items) {
    total += item.price * item.quantity;
  }
  // ... more calculation
  
  // Database (10 lines)
  db.orders.insert(order);
  // ... more DB ops
  
  // Notification (10 lines)
  emailService.send(order.customerEmail);
  // ...
}

// GOOD: Each method does ONE thing
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order.items);
  saveOrder(order, total);
  notifyCustomer(order);
}
```

---

### Large Class

**Symptoms:**
- Class has >20 methods
- Class has >10 fields
- Hard to understand what the class does
- Many methods that could be separate classes

**Why it's bad:**
- Hard to maintain
- High coupling
- Single Responsibility Principle violation

**Example:**
```javascript
// BAD: Does everything
class User {
  name; email; password;
  validate() { /* ... */ }
  authenticate() { /* ... */ }
  sendEmail() { /* ... */ }
  generateReport() { /* ... */ }
  exportPDF() { /* ... */ }
  importData() { /* ... */ }
  calculateStats() { /* ... */ }
}

// GOOD: Focused responsibilities
class User {
  name; email; password;
  validate() { /* ... */ }
  authenticate() { /* ... */ }
}

class EmailService {
  sendEmail() { /* ... */ }
}

class ReportGenerator {
  generateReport() { /* ... */ }
  exportPDF() { /* ... */ }
}

class DataImporter {
  importData() { /* ... */ }
}
```

---

### Duplicate Code

**Symptoms:**
- Same logic appears in multiple places
- Copy-paste programming
- Bug fixed in one place but not others

**Why it's bad:**
- Hard to maintain
- Bug duplication
- Inconsistent behavior

**Example:**
```javascript
// BAD: Duplicate validation
function createUser(userData) {
  if (!userData.email.includes('@')) {
    throw new Error('Invalid email');
  }
  // ... create user
}

function updateUser(userId, userData) {
  if (!userData.email.includes('@')) {  // Duplicate!
    throw new Error('Invalid email');
  }
  // ... update user
}

// GOOD: Single source of truth
function validateEmail(email) {
  if (!email.includes('@')) {
    throw new Error('Invalid email');
  }
}

function createUser(userData) {
  validateEmail(userData.email);
  // ... create user
}

function updateUser(userId, userData) {
  validateEmail(userData.email);  // Reuse
  // ... update user
}
```

---

### Feature Envy

**Symptoms:**
- A method is more interested in another class than its own
- Too much data from another class as parameters

**Why it's bad:**
- Logic in wrong place
- Tight coupling

**Example:**
```javascript
// BAD: Order envying OrderItem
class Order {
  calculateTotal() {
    let total = 0;
    for (const item of this.items) {
      total += item.price * item.quantity * (1 - item.discount);
    }
    return total;
  }
}

// GOOD: Let OrderItem calculate its own subtotal
class OrderItem {
  subtotal() {
    return this.price * this.quantity * (1 - this.discount);
  }
}

class Order {
  calculateTotal() {
    return this.items.reduce((sum, item) => sum + item.subtotal(), 0);
  }
}
```

---

### Data Clumps

**Symptoms:**
- Same group of parameters appear together
- Primitive parameters that belong together

**Why it's bad:**
- Error-prone (easy to miss one)
- Hard to understand

**Example:**
```javascript
// BAD: Parameters that go together
function createEvent(name, startDate, endDate, location, description) { /* ... */ }
function updateEvent(id, name, startDate, endDate, location, description) { /* ... */ }

// GOOD: Group related data
function createEvent(eventDetails) { /* ... */ }
function updateEvent(id, eventDetails) { /* ... */ }
```

---

### Primitive Obsession

**Symptoms:**
- Using primitives for domain concepts (String for email, int for money)
- Validation logic scattered

**Why it's bad:**
- No type safety
- Validation duplicated
- Easy to mix up values

**Example:**
```javascript
// BAD: Primitives everywhere
function processPayment(amount, currency) {
  if (amount < 0) throw new Error();
  if (currency !== 'USD' && currency !== 'EUR') throw new Error();
  // ...
}

// GOOD: Rich types
class Money {
  constructor(amount, currency) {
    if (amount < 0) throw new Error('Amount cannot be negative');
    this.amount = amount;
    this.currency = currency;
  }
}

function processPayment(payment) {
  // Validation is encapsulated
}
```

---

### Switch Statements

**Symptoms:**
- Same switch/if-else appears multiple times
- Adding new type requires changing multiple places

**Why it's bad:**
- Violates Open/Closed Principle
- Error-prone

**Example:**
```javascript
// BAD: Type-based conditionals
class Payment {
  process(type) {
    if (type === 'credit') { /* ... */ }
    else if (type === 'debit') { /* ... */ }
    else if (type === 'paypal') { /* ... */ }
  }
}

// GOOD: Polymorphism
interface PaymentProcessor {
  process(payment: Payment): void;
}

class CreditProcessor implements PaymentProcessor { /* ... */ }
class DebitProcessor implements PaymentProcessor { /* ... */ }
class PayPalProcessor implements PaymentProcessor { /* ... */ }
```

---

## Smell Severity Guide

| Severity | When to Fix |
|----------|-------------|
| 🔴 High | Fix before adding new features |
| 🟡 Medium | Fix when you touch this code |
| 🟢 Low | Fix when you have time |

**Consider:**
- How often is this code touched?
- How risky is the change?
- What's the test coverage?
