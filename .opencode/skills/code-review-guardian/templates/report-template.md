# Code Review Report Template

**Review Date**: {date}
**Reviewer**: AI Code Review Guardian
**Files Reviewed**: {file_list}
**Review Scope**: {quick|full|security-only}

---

## Executive Summary

| Metric | Count |
|--------|-------|
| 🔴 Critical | {n} |
| 🟠 High | {n} |
| 🟡 Medium | {n} |
| 🟢 Low | {n} |
| ✅ Passed | {dimensions} |

**Overall Verdict**: {APPROVED | CHANGES_REQUIRED | BLOCKED}

---

## 🔴 Critical Issues (Must Fix Before Merge)

### CRIT-001: {Issue Title}
- **Category**: {Security/Correctness/Performance}
- **File**: `{file_path}:{line_number}`
- **Description**: {what's wrong}
- **Impact**: {why this matters}
- **Code**:
  ```{language}
  // Current problematic code
  ```
- **Suggested Fix**:
  ```{language}
  // Corrected code
  ```
- **References**: {OWASP/CWE/Best Practice link}

---

## 🟠 High Priority Issues

### HIGH-001: {Issue Title}
- **Category**: {category}
- **File**: `{file_path}:{line_number}`
- **Description**: {what's wrong}
- **Suggested Fix**: {how to fix}

---

## 🟡 Medium Priority Issues

### MED-001: {Issue Title}
- **Category**: {category}
- **File**: `{file_path}:{line_number}`
- **Description**: {what's wrong}
- **Suggested Fix**: {how to fix}

---

## 🟢 Low Priority / Nitpicks

### LOW-001: {Issue Title}
- **Category**: Style/Maintainability
- **File**: `{file_path}:{line_number}`
- **Description**: {what's wrong}
- **Suggested Fix**: {how to fix}

---

## ✅ What's Done Well

1. {positive observation with specific example}
2. {another positive}
3. {another positive}

---

## 📋 Checklist Summary

### Security
- [x] Input validation
- [ ] No hardcoded secrets
- [x] Authentication present
- [ ] Authorization checks

### Correctness
- [x] Logic matches requirements
- [x] Edge cases handled
- [ ] Error messages specific

### Architecture
- [x] Single responsibility
- [x] No circular dependencies
- [ ] Dependency injection used

### Performance
- [x] No N+1 queries
- [x] Resources released
- [ ] Caching implemented

### Maintainability
- [x] Clear naming
- [x] Functions < 30 lines
- [ ] Cyclomatic complexity < 10

### Testing
- [x] New code tested
- [ ] Edge cases tested
- [x] All tests pass

### Documentation
- [x] Public APIs documented
- [ ] Complex logic explained

---

## 🔧 Recommended Actions

| Priority | Action | Effort |
|----------|--------|--------|
| 🔴 P0 | {action} | {time} |
| 🟠 P1 | {action} | {time} |
| 🟡 P2 | {action} | {time} |
| 🟢 P3 | {action} | {time} |

---

## 📝 Notes

{Any additional context, suggestions for future improvements, or architectural considerations}

---

**Review Completed**: {timestamp}
**Next Review Recommended**: {after fixes / in 1 week / as needed}
