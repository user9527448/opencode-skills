# Maintainability Review Guide

Ensure code is readable, maintainable, and follows best practices - naming, complexity, style.

---

## Code Quality Metrics

| Aspect | Good | Bad |
|--------|------|-----|
| Naming | `getUserById` | `get`, `func1` |
| Length | <30 lines/function | >100 lines/function |
| Complexity | Single responsibility | Multiple concerns |
| DRY | Extracted utilities | Copy-paste code |
| Comments | Explain "why" | Explain "what" |
| Cyclomatic | <10 | >20 |

---

## Naming Conventions

### Variables

| Type | Good | Bad |
|------|------|-----|
| Boolean | `isActive`, `hasPermission` | `flag`, `check` |
| Array | `users`, `orderItems` | `userList`, `data` |
| Function | `calculateTotal` | `process`, `doIt` |
| Class | `UserService` | `Manager`, `Handler` |

---

### Functions

| Aspect | Good | Bad |
|--------|------|-----|
| Verb + Noun | `getUserById` | `getUser` |
| Specific | `validateEmail` | `validate` |
| Consistent | `createUser` / `updateUser` | `makeUser` / `changeUser` |

---

## Cyclomatic Complexity

| Score | Risk | Action |
|-------|------|--------|
| 1-10 | Low | Acceptable |
| 11-20 | Medium | Consider refactoring |
| 21-50 | High | Refactor required |
| 50+ | Very High | Must refactor |

**How to reduce:**
- Extract methods
- Use early returns
- Simplify boolean logic
- Remove nested loops

---

## Code Style Checklist

- [ ] Names are self-documenting
- [ ] Functions do one thing
- [ ] Nesting ≤3 levels
- [ ] Magic numbers are constants
- [ ] Complex logic has comments
- [ ] No dead code
- [ ] Consistent style with codebase
- [ ] No deep nesting (use early returns)

---

## Code Smells

| Smell | Example | Fix |
|-------|---------|-----|
| Long Method | >50 lines | Extract methods |
| Large Class | >500 lines | Split responsibilities |
| Duplicate Code | Copy-paste | Extract to utility |
| Shotgun Surgery | Many files for one change | Increase cohesion |
| Feature Envy | Uses other class more | Move method |
| Data Clumps | Same params together | Extract class |
