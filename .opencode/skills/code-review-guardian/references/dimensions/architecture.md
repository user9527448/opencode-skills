# Architecture Review Guide

Evaluate code design and structure - patterns, principles, and overall system organization.

---

## SOLID Principles

### Single Responsibility Principle (SRP)

**Definition**: A class should have only one reason to change.

| ✅ Good | ❌ Bad |
|---------|--------|
| `UserRepository` handles database operations | `UserManager` handles DB, email, validation |
| `PaymentProcessor` handles payments | `OrderManager` handles orders, payments, notifications |

**Detection**: If a class name has "And" or "Manager", it's likely violating SRP.

---

### Open/Closed Principle (OCP)

**Definition**: Open for extension, closed for modification.

**Good Example:**
```typescript
// Instead of modifying existing code to add new behavior
interface Shape {
  area(): number
}

class Circle implements Shape {
  constructor(public radius: number) {}
  area() { return Math.PI * this.radius ** 2 }
}

class Rectangle implements Shape {
  constructor(public width: number, public height: number) {}
  area() { return this.width * this.height }
}

// Add new shapes without modifying existing code
```

---

### Liskov Substitution Principle (LSP)

**Definition**: Subtypes must be substitutable for their base types.

**Violation:**
```typescript
class Rectangle {
  setWidth(w: number) { this.width = w }
  setHeight(h: number) { this.height = h }
}

class Square extends Rectangle {
  setWidth(w: number) {
    this.width = w
    this.height = w  // Breaks expectation!
  }
}

// This will fail unexpectedly
function resize(rect: Rectangle) {
  rect.setWidth(10)
  rect.setHeight(20)
  assert(rect.width * rect.height === 200) // Fails for Square!
}
```

---

### Interface Segregation Principle (ISP)

**Definition**: Prefer small, focused interfaces over large ones.

| ✅ Good | ❌ Bad |
|---------|--------|
| `Printable`, `Scannable`, `Faxable` | `Machine` with all methods |
| `Readable`, `Writable` | `IOManager` |

---

### Dependency Inversion Principle (DIP)

**Definition**: Depend on abstractions, not concretions.

```typescript
// ❌ Bad: Direct dependency on concrete class
class OrderService {
  private database = new MySQLDatabase()  // Tight coupling
}

// ✅ Good: Depend on interface
class OrderService {
  constructor(private database: Database) {}  // Loose coupling
}
```

---

## Common Architecture Issues

| Issue | Detection | Impact |
|-------|-----------|--------|
| **God Class** | >500 lines, >10 methods | Hard to test, maintain |
| **Circular Dependency** | Import cycles | Initialization order problems |
| **Tight Coupling** | Direct instantiation | Hard to replace components |
| **Feature Envy** | Method uses another class more than its own | Logic in wrong place |
| **Primitive Obsession** | Using primitives for domain concepts | Missing type safety |
| **Shotgun Surgery** | One change requires many file edits | High coupling |

---

## Design Patterns

### When to Use

| Pattern | Use Case | Warning |
|---------|----------|---------|
| Repository | Data access abstraction | Don't over-abstract simple queries |
| Factory | Complex object creation | Can add complexity |
| Strategy | Interchangeable algorithms | May be overkill for simple cases |
| Observer | Event-driven updates | Watch for memory leaks |
| Decorator | Add behavior dynamically | Can create deep call stacks |
| Dependency Injection | Manage dependencies | Requires framework or setup |

---

## Architecture Checklist

- [ ] Clear separation of concerns
- [ ] Dependencies flow in one direction
- [ ] No circular dependencies
- [ ] Interfaces used for external dependencies
- [ ] Single responsibility maintained
- [ ] Appropriate design patterns applied
- [ ] Business logic separated from infrastructure
- [ ] Configuration externalized
- [ ] Error handling centralized

---

## Cyclomatic Complexity

| Score | Risk Level | Action |
|-------|------------|--------|
| 1-10 | Low | Acceptable |
| 11-20 | Medium | Consider refactoring |
| 21-50 | High | Refactor required |
| 50+ | Very High | Must refactor |

**How to reduce:**
- Extract methods
- Use early returns
- Simplify conditions
- Remove nested loops
