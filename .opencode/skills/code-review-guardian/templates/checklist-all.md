# Complete Review Checklist

## 🔒 Security

- [ ] All user inputs validated and sanitized
- [ ] No hardcoded credentials or secrets
- [ ] Authentication present on protected routes
- [ ] Authorization checked before operations
- [ ] Sensitive data encrypted at rest
- [ ] Sensitive data encrypted in transit
- [ ] Rate limiting on public endpoints
- [ ] CORS configured properly
- [ ] Security headers present (CSP, HSTS, X-Frame-Options)
- [ ] Dependencies checked for vulnerabilities
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] No CSRF vulnerabilities
- [ ] No command injection vulnerabilities
- [ ] No path traversal vulnerabilities

## 🎯 Correctness

- [ ] Logic matches requirements
- [ ] All branches reachable and tested
- [ ] Null/undefined handled
- [ ] Empty arrays/objects handled
- [ ] Boundary conditions checked
- [ ] Error messages helpful and specific
- [ ] No silent failures
- [ ] Type assertions avoid `as any`
- [ ] Async operations handle rejections
- [ ] Floating point comparisons account for precision
- [ ] Unicode handled correctly
- [ ] Time zones handled correctly

## 🏗️ Architecture

- [ ] Clear separation of concerns
- [ ] Dependencies flow in one direction
- [ ] No circular dependencies
- [ ] Interfaces used for external dependencies
- [ ] Single responsibility maintained
- [ ] Appropriate design patterns applied
- [ ] Business logic separated from infrastructure
- [ ] Configuration externalized
- [ ] Error handling centralized
- [ ] Cyclomatic complexity < 10

## ⚡ Performance

- [ ] No N+1 queries
- [ ] No unnecessary loops
- [ ] Resources properly released
- [ ] Caching considered for hot paths
- [ ] Database queries use indexes
- [ ] Pagination for large lists
- [ ] Lazy loading where appropriate
- [ ] Async/await not blocking
- [ ] No memory leaks
- [ ] Appropriate data structures used

## 🧹 Maintainability

- [ ] Names are self-documenting
- [ ] Functions do one thing
- [ ] Nesting ≤3 levels
- [ ] Magic numbers are constants
- [ ] Complex logic has comments
- [ ] No dead code
- [ ] Consistent style with codebase
- [ ] No deep nesting (early returns)
- [ ] No code duplication

## 🔄 Concurrency

- [ ] Shared state properly synchronized
- [ ] No race conditions
- [ ] Locks acquired in consistent order
- [ ] Timeouts on waits
- [ ] Immutable data preferred
- [ ] Atomic operations used correctly
- [ ] No deadlocks possible
- [ ] Thread pool sized correctly

## ♿ Accessibility

- [ ] All images have meaningful alt text
- [ ] Form inputs have associated labels
- [ ] Color contrast ratio ≥ 4.5:1
- [ ] Focus indicators visible
- [ ] ARIA attributes correct
- [ ] Keyboard navigation works
- [ ] No keyboard traps
- [ ] Proper heading hierarchy
- [ ] Error messages accessible
- [ ] Skip links provided

## 🧪 Testing

- [ ] New code has tests
- [ ] Edge cases tested (null, empty, boundary)
- [ ] Tests are readable
- [ ] No skipped tests without reason
- [ ] Test names describe behavior
- [ ] Assertions are specific
- [ ] Mocks don't hide real issues
- [ ] Integration tests for external services
- [ ] Test coverage > 80%

## 📚 Documentation

- [ ] Public APIs documented (JSDoc/docstrings)
- [ ] Complex logic explained in comments
- [ ] README updated if needed
- [ ] Breaking changes noted
- [ ] Examples provided
- [ ] Type definitions accurate
- [ ] Error codes documented
- [ ] Configuration options documented

---

## Summary Score

| Category | Score |
|----------|-------|
| Security | {x}/{y} |
| Correctness | {x}/{y} |
| Architecture | {x}/{y} |
| Performance | {x}/{y} |
| Maintainability | {x}/{y} |
| Concurrency | {x}/{y} |
| Accessibility | {x}/{y} |
| Testing | {x}/{y} |
| Documentation | {x}/{y} |

**Overall Score**: {x}%

**Recommendation**: {APPROVED / NEEDS_WORK / REJECTED}
