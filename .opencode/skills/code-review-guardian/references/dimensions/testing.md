# Testing Review Guide

Ensure code is properly tested - coverage, quality, and testability.

---

## Test Quality Checks

| Question | Expectation |
|----------|-------------|
| New tests added? | Yes, for new code |
| Edge cases covered? | Not just happy path |
| Tests readable? | Clear intent |
| All tests pass? | Green |
| Mocks appropriate? | Not over-mocked |
| Assertions specific? | Not just "exists" |

---

## Test Patterns

### ❌ Weak Test

```javascript
test('user creation', async () => {
  const result = await createUser({ name: 'test' })
  expect(result).toBeDefined()  // Too broad!
})
```

**Issues:**
- Doesn't verify actual behavior
- Passes even with wrong data
- No specific assertions

---

### ✅ Strong Test

```javascript
test('creates user with valid data and returns user object', async () => {
  const input = { name: 'test', email: 'test@example.com' }
  const result = await createUser(input)
  
  // Specific assertions
  expect(result).toMatchObject({
    id: expect.any(String),
    name: 'test',
    email: 'test@example.com',
    createdAt: expect.any(Date)
  })
  
  // Verify side effects
  expect(mockDb.save).toHaveBeenCalledWith(
    expect.objectContaining(input)
  )
})
```

---

## Test Coverage Areas

### Happy Path
- ✅ Primary use case works
- ✅ Correct output format
- ✅ Expected state changes

### Edge Cases
- ✅ Null/undefined inputs
- ✅ Empty collections
- ✅ Boundary values
- ✅ Very long inputs
- ✅ Special characters

### Error Cases
- ✅ Invalid inputs rejected
- ✅ Error messages helpful
- ✅ Proper error types thrown
- ✅ Cleanup on failure

---

## Testing Checklist

- [ ] New code has tests
- [ ] Edge cases tested (null, empty, boundary)
- [ ] Tests are readable
- [ ] No skipped tests without reason
- [ ] Test names describe behavior
- [ ] Assertions are specific
- [ ] Mocks don't hide real issues
- [ ] Integration tests for external services

---

## Anti-Patterns

| Anti-Pattern | Issue | Fix |
|--------------|-------|-----|
| Test naming | `test1`, `test2` | Describe behavior |
| Over-mocking | Mocking everything | Test real behavior |
| No assertions | Empty test | Add assertions |
| Hard-coded time | `new Date()` in tests | Use fakes |
| Testing implementation | Testing internal methods | Test public API |
