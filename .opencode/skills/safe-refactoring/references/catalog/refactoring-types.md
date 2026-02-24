# Refactoring Catalog

Comprehensive list of refactoring techniques with before/after examples.

---

## 1. Extract Method

**When:** A code block can be named and has a clear purpose

**Before:**
```javascript
function processUserRegistration(userData) {
  // Validate email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(userData.email)) {
    throw new Error('Invalid email');
  }
  
  // Validate password strength
  if (userData.password.length < 8) {
    throw new Error('Password too short');
  }
  
  // Save to database
  const user = db.users.create(userData);
  
  // Send welcome email
  emailService.send(user.email, 'Welcome!');
}
```

**After:**
```javascript
function processUserRegistration(userData) {
  validateEmail(userData.email);
  validatePassword(userData.password);
  
  const user = db.users.create(userData);
  sendWelcomeEmail(user.email);
}

function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    throw new Error('Invalid email');
  }
}

function validatePassword(password) {
  if (password.length < 8) {
    throw new Error('Password too short');
  }
}
```

---

## 2. Rename (Variable/Function/Class)

**When:** Name doesn't communicate intent

**Before:**
```javascript
const d = new Date();
const temp = users.filter(u => u.a);
const list = data.map(x => x.val);
```

**After:**
```javascript
const currentDate = new Date();
const activeUsers = users.filter(user => user.isActive);
const orderValues = orders.map(order => order.value);
```

---

## 3. Extract Constant

**When:** Magic numbers/strings appear

**Before:**
```javascript
if (user.age >= 18) { /* ... */ }
setTimeout(callback, 30000);
const rate = price * 0.15;
```

**After:**
```javascript
const LEGAL_AGE = 18;
const SESSION_TIMEOUT_MS = 30000;
const TAX_RATE = 0.15;

if (user.age >= LEGAL_AGE) { /* ... */ }
setTimeout(callback, SESSION_TIMEOUT_MS);
const rate = price * TAX_RATE;
```

---

## 4. Introduce Parameter Object

**When:** Multiple parameters go together

**Before:**
```javascript
function createEvent(name, startDate, endDate, location, description) {
  // ...
}
```

**After:**
```javascript
function createEvent(eventDetails) {
  const { name, startDate, endDate, location, description } = eventDetails;
  // ...
}

createEvent({ name: 'Party', startDate: ..., endDate: ..., ... });
```

---

## 5. Replace Conditional with Polymorphism

**When:** Complex switch/if-else based on type

**Before:**
```javascript
class Payment {
  process(payment) {
    if (payment.type === 'credit') {
      // Credit processing
    } else if (payment.type === 'debit') {
      // Debit processing
    } else if (payment.type === 'paypal') {
      // PayPal logic
    }
  }
}
```

**After:**
```javascript
class CreditPayment { process() { /* ... */ } }
class DebitPayment { process() { /* ... */ } }
class PayPalPayment { process() { /* ... */ } }
```

---

## 6. Move Method

**When:** Method uses another class more than its own

**Before:**
```javascript
class Order {
  calculateTotal() {
    let total = 0;
    for (const item of this.items) {
      total += item.price * item.quantity;
      total *= (1 - item.discount);
    }
    return total;
  }
}
```

**After:**
```javascript
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

## 7. Replace Nested Conditionals with Guard Clauses

**When:** Deep nesting from conditionals

**Before:**
```javascript
function getPayAmount(employee) {
  if (employee !== null) {
    if (employee.isSeparated) {
      if (employee.isRetired) {
        return getSeparatedRetiredPay(employee);
      } else {
        return getSeparatedPay(employee);
      }
    } else {
      if (employee.isRetired) {
        return getRetiredPay(employee);
      } else {
        return getNormalPay(employee);
      }
    }
  } else {
    return 0;
  }
}
```

**After:**
```javascript
function getPayAmount(employee) {
  if (employee === null) return 0;
  if (employee.isSeparated) return employee.isRetired 
    ? getSeparatedRetiredPay(employee) 
    : getSeparatedPay(employee);
  if (employee.isRetired) return getRetiredPay(employee);
  return getNormalPay(employee);
}
```

---

## 8. Extract Class

**When:** A class has multiple responsibilities

**Before:**
```javascript
class User {
  name;
  email;
  passwordHash;
  validatePassword() { /* ... */ }
  sendEmail() { /* ... */ }
  generateReport() { /* ... */ }
}
```

**After:**
```javascript
class User {
  name;
  email;
  passwordHash;
  validatePassword() { /* ... */ }
}

class EmailService {
  sendEmail() { /* ... */ }
}

class ReportGenerator {
  generateReport() { /* ... */ }
}
```

---

## 9. Inline Method

**When:** Method body is as clear as its name

**Before:**
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}

function getScore() {
  const rating = getRating(driver);
  // use rating
}
```

**After:**
```javascript
function getScore() {
  const rating = driver.numberOfLateDeliveries > 5 ? 2 : 1;
  // use rating
}
```

---

## 10. Remove Dead Code

**When:** Code is unused

**Before:**
```javascript
function calculateDistanceLegacy(x1, y1, x2, y2) {
  return Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
}
```

**After:** Delete the function

---

## 11. Rename Class

**When:** Class name doesn't describe its responsibility

**Before:**
```javascript
class Utils {
  static formatDate() { /* ... */ }
  static calculate() { /* ... */ }
  static parse() { /* ... */ }
}
```

**After:**
```javascript
class DateFormatter { /* date methods */ }
class OrderCalculator { /* calculation methods */ }
class ResponseParser { /* parsing methods */ }
```

---

## 12. Introduce Assertion

**When:** Code assumes something that might not be true

**Before:**
```javascript
function divide(a, b) {
  return a / b;
}
```

**After:**
```javascript
function divide(a, b) {
  console.assert(b !== 0, 'Division by zero');
  return a / b;
}
```

---

## 13. Replace Error Code with Exception

**When:** Method returns error codes

**Before:**
```javascript
function withdraw(account, amount) {
  if (account.balance < amount) {
    return -1;
  }
  account.balance -= amount;
  return 0;
}
```

**After:**
```javascript
function withdraw(account, amount) {
  if (account.balance < amount) {
    throw new InsufficientFundsError('Not enough balance');
  }
  account.balance -= amount;
}
```

---

## 14. Add Parameter

**When:** Method needs more information

**Before:**
```javascript
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

**After:**
```javascript
function calculateTotal(items, taxRate = 0, discount = 0) {
  const subtotal = items.reduce((sum, item) => sum + item.price, 0);
  return subtotal * (1 - discount) * (1 + taxRate);
}
```

---

## 15. Split Loop

**When:** One loop does multiple things

**Before:**
```javascript
let total = 0;
let count = 0;
for (const order of orders) {
  total += order.amount;
  count++;
}
const average = total / count;
```

**After:**
```javascript
const total = orders.reduce((sum, o) => sum + o.amount, 0);
const count = orders.length;
const average = total / count;
```

---

## Risk Assessment

| Refactoring Type | Risk | Recommended Approach |
|------------------|------|---------------------|
| Rename variable | 🟢 Low | Direct change, verify tests |
| Extract constant | 🟢 Low | Direct change |
| Remove dead code | 🟢 Low | Verify no references first |
| Extract method | 🟡 Medium | Keep signature, test thoroughly |
| Move method | 🟡 Medium | Check all call sites first |
| Extract class | 🔴 High | Add tests first, incremental |
| Replace algorithm | 🔴 High | Compare outputs before/after |
| Change inheritance | 🔴 High | Full regression testing |
