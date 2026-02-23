# Documentation Review Guide

Ensure code is properly documented - APIs, comments, and related materials.

---

## API Documentation

### What to Document

| Type | What's Needed |
|------|---------------|
| Functions | Purpose, parameters, return value, errors |
| Classes | Purpose, constructor params, public methods |
| Interfaces | Purpose, properties, methods |
| Constants | Purpose, allowed values |

---

### Good JSDoc Example

```javascript
/**
 * Creates a new user in the system.
 * 
 * @param {Object} userData - The user data
 * @param {string} userData.name - User's full name (required)
 * @param {string} userData.email - User's email (required, must be valid)
 * @returns {Promise<User>} The created user
 * @throws {ValidationError} If user data is invalid
 * @throws {DuplicateError} If email already exists
 * 
 * @example
 * const user = await createUser({
 *   name: 'John Doe',
 *   email: 'john@example.com'
 * });
 */
async function createUser(userData) { ... }
```

---

## Code Comments

### ✅ Good Comments

```javascript
// Using BFS to find shortest path
// DFS would require exploring all paths
const shortestPath = bfs(start, target)

// Workaround for Chrome bug #12345
// TODO: Remove when Chrome fixes issue
workaroundForChromeBug()
```

### ❌ Bad Comments

```javascript
// Loop through users
users.forEach(user => ...)

// Check if active
if (user.isActive) ...

// This function does something
function processData() { ... }
```

---

## Documentation Checklist

- [ ] Public APIs documented (JSDoc/docstrings)
- [ ] Complex logic explained in comments
- [ ] README updated if needed
- [ ] Breaking changes noted
- [ ] Examples provided
- [ ] Type definitions accurate
- [ ] Error codes documented
- [ ] Configuration options documented

---

## README Checklist

- [ ] Project purpose clearly stated
- [ ] Installation instructions
- [ ] Usage examples
- [ ] API reference or links
- [ ] Contributing guidelines
- [ ] License
- [ ] Status badges (build, coverage)
