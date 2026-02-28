---
name: test-driven-debugging
description: Four-phase systematic debugging methodology - root cause investigation, pattern analysis, hypothesis testing, minimal fix implementation. Enhanced with causal debugging, deterministic replay, and verification gates.
license: MIT
compatibility: opencode
metadata:
  references:
    patterns: references/patterns/
    scenarios: examples/scenarios/
    templates: templates/
    lockfiles: references/environment/
#RK|
  triggers:
    - "test failed"
    - "debug this"
    - "fix bug"
    - "regression"
    - "flaky test"
    - "CI red"
---

# Test-Driven Debugging

> NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
> 
> Enhanced with Causal Debugging principles: deterministic replay, dynamic slicing, and verification gates.

---

## 🚨 When to Activate This Skill

| Trigger | Priority | Notes |
|---------|----------|-------|
| Any test failure | HIGH | Start immediately |
| CI/CD pipeline red | HIGH | Blocked deployment |
| "Works on my machine" | MEDIUM | Environment issue |
| Flaky test detection | MEDIUM | Non-deterministic |
| Regression after changes | HIGH | Recently introduced |
| Production incident | CRITICAL | Time-sensitive |

---

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST

If you haven't completed Phase 1, you cannot propose fixes.
Violating this is violating the spirit of debugging.

Additionally: NEVER ship unverified fixes
- Coverage must meet threshold
- Mutation tests must pass
- All existing tests must pass
```

---

## Core Principles

### 1. 🟢 Deterministic First

Before anything else, make the failure reproducible:

```bash
# Freeze environment
npm install --frozen-lockfile
node --version
npm --version

# Capture exact inputs
cp -r test/fixtures/ /tmp/debug/
```
### 1. 🟢 Deterministic First
#VW|
#VT|Before anything else, make the failure reproducible:
#JN|
#BV|```bash
#MR|# Freeze environment (see lockfiles reference for your language)
#RH|# For npm: npm install --frozen-lockfile
#RH|# For poetry: poetry install --no-root
#RH|# For pip: pip install --require-hashes -r requirements.txt
#RH|# ... see references/environment/lockfiles.md for full list
#MN|node --version
#RZ|npm --version
#KB|
#NM|# Capture exact inputs
#QQ|cp -r test/fixtures/ /tmp/debug/
#JH|```
### 2. 🔬 Scientific Method

Debugging is hypothesis testing, not guessing:

```
HYPOTHESIS → TEST → EVIDENCE → CONCLUSION

Never: "I think this might work"
Always: "If X causes Y, then Z should happen"
```

### 3. 📏 Minimal Reproduction

Isolate to the smallest possible case:

```
❌ "The whole test suite fails"
✅ "This single test fails with these exact inputs"
```

### 4. 🛡️ Verification Gates

Never ship without proof:

| Gate | Threshold | Tool |
|------|-----------|------|
| Unit tests | 100% pass | jest, pytest |
| Coverage | >80% changed | coverage report |
| Mutation | >90% killed | stryker, mutmut |
| Type check | 0 errors | tsc --noEmit |

---

## Phase 1: Root Cause Investigation

**Time box: 15-30 minutes maximum**

### Step 1.1: Error Analysis

Every word in an error message matters:

```markdown
## Error Analysis

### Full Error Message
[Copy COMPLETE - no truncation]

### Stack Trace Reading
- Entry point: Where flow started
- Failure point: Where it crashed  
- Key frames: [list important calls]

### Error Classification
[ ] TypeError - null/undefined access
[ ] ReferenceError - variable not found
[ ] SyntaxError - parsing failed
[ ] AssertionError - expectation failed
[ ] TimeoutError - async never resolved
[ ] NetworkError - API unreachable
[ ] MemoryError - OOM, stack overflow
```

### Step 1.2: Deterministic Reproduction

```bash
# Isolate the exact failing case
npm test -- --grep "exact test name" --verbose

# Run in isolation (no parallel)
npm test -- --runInBand

# Capture environment
node --version > env.txt
npm list > deps.txt

# Freeze random seeds
export seed=12345
### Step 1.2: Deterministic Reproduction
#QS|
#BV|```bash
#ZX|# Isolate the exact failing case
#QZ|npm test -- --grep "exact test name" --verbose
#WX|
#KR|# Run in isolation (no parallel)
#TJ|npm test -- --runInBand
#BT|
#JY|# Capture environment
#ZS|node --version > env.txt
#RJ|npm list > deps.txt
#SS|
#BZ|# Freeze random seeds
#KQ|export seed=12345
#XQ|
#HM|**Environment-Specific Commands:**
#HM|See `references/environment/lockfiles.md` for:
#HM|- npm/yarn/pnpm (JavaScript/Node.js)
#HM|- pip/pipenv/poetry (Python)
#HM|- Maven/Gradle (Java)
#HM|- go mod (Go)
#HM|- Cargo (Rust)
#HM|- And more...

**Reproduction Checklist:**
- [ ] Can trigger reliably (>3 times)?
- [ ] Exact steps documented?
- [ ] Same in CI AND local?
- [ ] Minimal input that fails?

### Step 1.3: Git Archaeology

```bash
# Recent changes to file
git log --oneline -10 -- path/to/file.ts

# What changed in this commit?
git show <commit> --stat

# Find breaking commit (if regression)
git bisect start
git bisect bad HEAD
git bisect good <known-good-commit>
git bisect run npm test
```

### Step 1.4: Dynamic Slicing (Advanced)

Identify only code that contributed to failure:

```
Concept: Dynamic Slice = minimal code path causing bug

Techniques:
1. Start from failure point
2. Trace backwards through stack
3. Include only variables that affected failure
4. Ignore unrelated code
```

---

## Phase 2: Pattern Analysis

### Step 2.1: Failure Pattern Library

| Pattern | Likely Cause | Quick Check |
|---------|--------------|-------------|
| `Expected X got Y` | Off-by-one, wrong value | Print actual |
| `Cannot read prop of undefined` | Missing null guard | Trace source |
| `Timeout exceeded` | Async never resolved | Log async steps |
| `Mock not called` | Wrong params/module | Log actual calls |
| `Element not found` | Selector stale | Check DOM snapshot |
| `Works local, fails CI` | Env difference | Compare configs |
| `Flaky: sometimes passes` | Race condition | Add delays |
| `Memory leak` | Unreleased reference | Heap snapshot |

### Step 2.2: Compare Working vs Failing

| Aspect | Working | Failing | Delta |
|--------|---------|---------|-------|
| Input | ? | ? | ? |
| State | ? | ? | ? |
| Config | ? | ? | ? |
| Timing | ? | ? | ? |

### Step 2.3: LLM-Assisted Analysis

Use AI to accelerate pattern recognition:

```
Prompt: "Analyze this stack trace and suggest likely root causes:
[paste full error]"
```

**Valid AI suggestions with:**
- Manual verification
- Small test case
- Not just accepting at face value

---

## Phase 3: Hypothesis Testing

### Hypothesis Template

```markdown
### Hypothesis #N

**Statement:** "The error occurs because [specific reason]"

**Evidence:**
- [fact 1 supporting]
- [fact 2 supporting]

**Test:** [minimal test to verify]

**Expected if true:** [specific observable]

**Result:** [CONFIRMED / DISPROVEN / INCONCLUSIVE]

**New information:** [what we learned]
```

### Hypothesis Testing Log

| # | Hypothesis | Test | Result | Conclusion |
|---|------------|------|--------|------------|
| 1 | | | ✓/✗ | |
| 2 | | | ✓/✗ | |
| 3 | | | ✓/✗ | |

### Rules

1. Test ONE hypothesis at a time
2. Make minimal changes to test
3. Document BEFORE moving on
4. If disproven, update mental model

### Time Boxing

```
Set explicit time limits:
- Hypothesis testing: 15 min max
- If no progress: take a break
- After 3 failed attempts: consult colleague
```

---

## Phase 4: Implementation

### Step 4.1: Create Reproduction Test

```javascript
// FIRST: Write test that fails due to bug
it('should handle edge case X', () => {
  const result = process(X);
  expect(result).toBe(expected); // Currently throws/fails
});
```

**Why first?** Ensures bug is fixed, not just masked

### Step 4.2: Minimal Fix

```javascript
// Change ONLY what's necessary
// NO refactoring
// NO adding features
// JUST fix the bug
```

### Step 4.3: Verification Gates

```bash
# 1. Unit tests
npm test -- --grep "related"

# 2. Coverage gate
npm run test -- --coverage
# Must cover >80% of CHANGED code

# 3. Mutation testing (recommended)
npx stryker run
# Must kill >90% of mutants

# 4. Full suite
npm test
```

---

## 📁 Directory Structure

```
test-driven-debugging/
├── SKILL.md
├── references/
│   └── patterns/
│       └── failure-patterns.md    # Comprehensive pattern library
├── examples/
│   └── scenarios/
│       └── debugging-scenarios.md # Real-world debugging examples
├── templates/
│   ├── hypothesis-template.md     # Hypothesis testing form
│   └── error-analysis.md         # Error analysis worksheet
└── scripts/
    └── bisect-automate.sh        # Git bisect automation
JV|```
#ZS|
#YW|---
#ZK|
#QP|## 📁 Directory Structure
#BY|
JV|```
#KW|test-driven-debugging/
#BS|├── SKILL.md
#MZ|├── references/
#QS|│   ├── environment/
#NM|│   │   └── lockfiles.md         # Multi-language lockfile reference
#QS|│   └── patterns/
#KJ|│       └── failure-patterns.md    # Comprehensive pattern library
#MT|├── examples/
#VH|│   └── scenarios/
#PH|│       └── debugging-scenarios.md # Real-world debugging examples
#NB|├── templates/
#TH|│   ├── hypothesis-template.md     # Hypothesis testing form
#YN|│   └── error-analysis.md         # Error analysis worksheet
#XZ|└── scripts/
#HM|    └── bisect-automate.sh        # Git bisect automation
#JQ|```

---

## 📖 Reference Files

| Category | Location | Contents |
|----------|----------|----------|
| **Patterns** | `references/patterns/` | 20+ failure patterns |
| **Scenarios** | `examples/scenarios/` | Real debugging cases |
| **Templates** | `templates/` | Hypothesis, error analysis |
VB|| Category | Location | Contents |
#ZP||----------|----------|----------|
#BJ|| **Lockfiles** | `references/environment/` | npm, pip, poetry, cargo... |
#NB|| **Patterns** | `references/patterns/` | 20+ failure patterns |
#BK|| **Scenarios** | `examples/scenarios/` | Real debugging cases |
#QB|| **Templates** | `templates/` | Hypothesis, error analysis |
#VW|| **Scripts** | `scripts/` | Automation helpers |

---

## Three-Strike Rule

```
After THREE failed fix attempts:

STOP. This signals:
- Wrong hypothesis about root cause
- Architectural problem
- Missing information

Actions:
1. Revert all changes
2. Take a break (fresh perspective)
3. Consult another engineer
4. Consider if it's worth fixing now
```

---

## 🛑 Red Flags - Stop Immediately

| Thought | Reality | Action |
|---------|---------|--------|
| "Let me try this fix" | Guessing | STOP → Do Phase 1 |
| "Maybe increase timeout" | Masking symptom | Find root cause |
| "Probably just flaky" | Assumption | Investigate systematically |
| "Works on my machine" | Env difference | Compare configurations |
| "Ship it, tests pass" | Coverage ignored | Run mutation tests |

---

## Advanced: Causal Debugging

For complex bugs, apply causal debugging principles:

### 1. Deterministic Replay
```
- Freeze npm versions (--frozen-lockfile)
- Capture exact input data
- Record random seeds
- Note timing/environment
### 1. Deterministic Replay
#MS|#VN|- Freeze versions (see lockfiles reference)
#VN|# Reference: references/environment/lockfiles.md
#VN|# - npm: npm install --frozen-lockfile
#VN|# - poetry: poetry install --no-root
#VN|# - cargo: cargo build --locked
#VN|# - And 10+ other languages
#WR|- Capture exact input data
#WP|- Record random seeds
#RR|- Note timing/environment
#QH|```

### 2. Dynamic Slicing
```
- Start from failure point
- Trace backward through stack
- Keep only influencing variables
- Ignore unrelated code
```

### 3. Counterfactual Reasoning
```
"If we change X, does failure disappear?"
"Does changing Y have no effect?"
```

### 4. Property-Based Testing
```javascript
// After fix: verify no regressions
test('handles random inputs', () => {
  for (let i = 0; i < 1000; i++) {
    const input = randomInput();
    expect(validate(input)).toBeDefined();
  }
});
```

---

## Quick Reference

```
PHASE 1: ROOT CAUSE
□ Read FULL error message
□ Reproduce deterministically
□ Check recent changes (git)
□ Gather evidence

PHASE 2: PATTERN
□ Find working examples
□ Compare vs failing
□ Match pattern library

PHASE 3: HYPOTHESIS
□ Form ONE hypothesis
□ Test minimally
□ Document result

PHASE 4: IMPLEMENT
□ Create failing test
□ Minimal fix
□ Run verification gates:
  □ All tests pass
  □ Coverage >80%
  □ Mutation >90%

NEVER:
- Guess without evidence
- Skip verification gates
- Ship without testing
```

---

## Limitations

- Cannot debug without reproducible case
- Some bugs require specific environment
- Time-sensitive incidents may need workaround
- Third-party library bugs require upstream fix
