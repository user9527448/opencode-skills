# Hypothesis Testing Template

Use this template for systematic hypothesis testing during debugging.

---

## Hypothesis #

**Number:** 
**Date:** 
**Context:** 

### Statement

"The error occurs because:"

```
[Specific technical reason]
```

### Evidence

Supporting facts:

- [ ] 
- [ ] 
- [ ] 

### Test Design

Minimal test to verify:

```javascript
// Test case
```

### Expected Result

If hypothesis is TRUE, we should see:

```
[Observable outcome]
```

### Actual Result

| Run | Result |
|-----|--------|
| 1 | ✓ / ✗ |
| 2 | ✓ / ✗ |
| 3 | ✓ / ✗ |

### Conclusion

- [ ] **CONFIRMED** - Hypothesis explains the bug
- [ ] **DISPROVEN** - Something else is causing this
- [ ] **INCONCLUSIVE** - Need more evidence

### New Information Learned

```
[What we learned that changes our understanding]
```

### Next Hypothesis

If disproven, what to test next:

```
[Next hypothesis to test]
```

---

## Hypothesis Log

| # | Hypothesis | Evidence | Test | Result | Conclusion |
|---|------------|----------|------|--------|------------|
| 1 | | | | ✓/✗ | |
| 2 | | | | ✓/✗ | |
| 3 | | | | ✓/✗ | |
| 4 | | | | ✓/✗ | |
| 5 | | | | ✓/✗ | |

---

## Time Boxing

| Hypothesis | Start Time | End Time | Time Spent |
|------------|------------|----------|------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Total time spent:** 

**Decision:** Continue / Take break / Consult colleague
