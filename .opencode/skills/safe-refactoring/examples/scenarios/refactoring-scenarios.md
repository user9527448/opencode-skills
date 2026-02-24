# Refactoring Scenarios

Real-world refactoring examples with step-by-step process.

---

## Scenario 1: Extract Class from God Class

### Before: User Class (400 lines)

```javascript
class User {
  // Properties (50 lines)
  id; name; email; password; phone; address; avatar;
  createdAt; updatedAt; lastLogin; role; status;
  
  // Validation methods (100 lines)
  validate() { /* ... */ }
  validateEmail() { /* ... */ }
  validatePassword() { /* ... */ }
  validatePhone() { /* ... */ }
  validateAddress() { /* ... */ }
  
  // Auth methods (50 lines)
  login() { /* ... */ }
  logout() { /* ... */ }
  resetPassword() { /* ... */ }
  changePassword() { /* ... */ }
  
  // Email methods (80 lines)
  sendWelcomeEmail() { /* ... */ }
  sendPasswordResetEmail() { /* ... */ }
  sendNotificationEmail() { /* ... */ }
  
  // Report methods (120 lines)
  generateProfileReport() { /* ... */ }
  generateActivityReport() { /* ... */ }
  exportToPDF() { /* ... */ }
  exportToCSV() { /* ... */ }
}
```

### Goal
Split into focused classes with single responsibility.

### Execution Steps

```
Step 1: Identify Responsibilities
        → Group related methods
        → Validation: validateEmail, validatePassword, validatePhone
        → Authentication: login, logout, resetPassword
        → Email: sendWelcomeEmail, sendPasswordResetEmail
        → Reporting: generateProfileReport, exportToPDF/CSV

Step 2: Create New Classes (empty)
        → class UserValidator { }
        → class AuthService { }
        → class EmailService { }
        → class ReportGenerator { }
        → Test → GREEN → Commit

Step 3: Move Validation Methods
        → Move validateEmail, validatePassword to UserValidator
        → Test → GREEN → Commit

Step 4: Move Auth Methods
        → Move login, logout, resetPassword to AuthService
        → Test → GREEN → Commit

Step 5: Move Email Methods
        → Move send* methods to EmailService
        → Test → GREEN → Commit

Step 6: Move Report Methods
        → Move generateReport, export* to ReportGenerator
        → Test → GREEN → Commit

Step 7: Final Cleanup
        → Remove empty methods from User
        → Update all references
        → Test → GREEN → Commit
```

### After: Focused Classes

```javascript
class User {
  id; name; email; password; phone; address; avatar;
  createdAt; updatedAt; lastLogin; role; status;
}

class UserValidator {
  validate(user) { /* ... */ }
  validateEmail(email) { /* ... */ }
  validatePassword(password) { /* ... */ }
}

class AuthService {
  constructor(userRepository) { /* ... */ }
  login(credentials) { /* ... */ }
  logout(userId) { /* ... */ }
}

class EmailService {
  sendWelcomeEmail(user) { /* ... */ }
  sendPasswordResetEmail(user) { /* ... */ }
}

class ReportGenerator {
  generateProfileReport(user) { /* ... */ }
  exportToPDF(user) { /* ... */ }
}
```

---

## Scenario 2: Replace Nested Conditionals

### Before: Deeply Nested Code

```javascript
function getEmployeeBonus(employee) {
  if (employee !== null) {
    if (employee.isActive) {
      if (employee.department) {
        if (employee.department.type === 'sales') {
          if (employee.sales > 100000) {
            return employee.sales * 0.15;
          } else if (employee.sales > 50000) {
            return employee.sales * 0.10;
          } else {
            return employee.sales * 0.05;
          }
        } else if (employee.department.type === 'engineering') {
          return employee.salary * 0.10;
        } else {
          return employee.salary * 0.05;
        }
      } else {
        return 0;
      }
    } else {
      return 0;
    }
  } else {
    return 0;
  }
}
```

### After: Guard Clauses

```javascript
function getEmployeeBonus(employee) {
  if (employee === null) return 0;
  if (!employee.isActive) return 0;
  if (!employee.department) return 0;
  
  const { type } = employee.department;
  
  if (type === 'sales') {
    if (employee.sales > 100000) return employee.sales * 0.15;
    if (employee.sales > 50000) return employee.sales * 0.10;
    return employee.sales * 0.05;
  }
  
  if (type === 'engineering') return employee.salary * 0.10;
  
  return employee.salary * 0.05;
}
```

### Verification

```bash
# Test each branch
expect(getEmployeeBonus(null)).toBe(0);
expect(getEmployeeBonus({isActive: false})).toBe(0);
expect(getEmployeeBonus({isActive: true, department: null})).toBe(0);
expect(getEmployeeBonus({isActive: true, department: {type: 'sales'}, sales: 120000})).toBe(18000);
```

---

## Scenario 3: Introduce Parameter Object

### Before: Too Many Parameters

```javascript
function createEvent(
  name, 
  startDate, 
  endDate, 
  location, 
  description, 
  organizer, 
  capacity, 
  isPublic,
  tags,
  registrationRequired,
  sendNotifications
) {
  // 50 lines of validation and creation logic
}
```

### After: Parameter Object

```javascript
function createEvent(eventDetails) {
  const { 
    name, 
    startDate, 
    endDate, 
    location, 
    description, 
    organizer, 
    capacity, 
    isPublic,
    tags,
    registrationRequired,
    sendNotifications 
  } = eventDetails;
  
  // 50 lines of validation and creation logic
}

// Usage
createEvent({
  name: 'Tech Conference',
  startDate: new Date('2024-03-15'),
  endDate: new Date('2024-03-17'),
  location: 'Convention Center',
  description: 'Annual tech event',
  organizer: 'TechCorp',
  capacity: 500,
  isPublic: true,
  tags: ['tech', 'conference'],
  registrationRequired: true,
  sendNotifications: true
});
```

---

## Scenario 4: Move Method (Feature Envy)

### Before: Feature Envy

```javascript
class Order {
  items = [];
  
  calculateTotal() {
    let total = 0;
    for (const item of this.items) {
      // Using OrderItem data extensively
      const discount = item.isPremium ? 0.2 : 0.1;
      const subtotal = item.price * item.quantity;
      total += subtotal * (1 - discount);
      
      if (item.taxCategory) {
        total += subtotal * item.taxCategory.rate;
      }
      
      if (item.shipping && item.shipping.expedited) {
        total += item.shipping.cost * 0.5;
      }
    }
    return total;
  }
}
```

### After: Move Method to OrderItem

```javascript
class OrderItem {
  price; quantity; isPremium; taxCategory; shipping;
  
  calculateTotal() {
    const discount = this.isPremium ? 0.2 : 0.1;
    const subtotal = this.price * this.quantity;
    let total = subtotal * (1 - discount);
    
    if (this.taxCategory) {
      total += subtotal * this.taxCategory.rate;
    }
    
    if (this.shipping && this.shipping.expedited) {
      total += this.shipping.cost * 0.5;
    }
    
    return total;
  }
}

class Order {
  items = [];
  
  calculateTotal() {
    return this.items.reduce((sum, item) => sum + item.calculateTotal(), 0);
  }
}
```

---

## Common Patterns

### Pattern 1: Extract Then Inline

When you're unsure about extraction:

```
1. Extract the code to a new method (even if long)
2. Test thoroughly
3. If it doesn't improve readability, inline it back
```

### Pattern 2: Parallel Refactoring

When refactoring production and test code:

```
1. Refactor production code
2. Tests fail
3. Fix tests to match new structure
4. All green = refactoring complete
```

### Pattern 3: Branch by Abstraction

For large-scale changes without branching:

```
1. Create abstraction layer
2. New code uses abstraction
3. Gradually migrate old code
4. Remove old implementation when done
```
