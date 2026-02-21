---
name: skill-structure-organizer
description: Guides restructuring of OpenCode skills into modular structure when they exceed 500 lines. Analyzes, extracts, and reorganizes content into references/, examples/, templates/, scripts/.
license: MIT
compatibility: opencode
metadata:
  author: user9527448
  tags:
    - skill-writing
    - refactoring
    - organization
  triggers:
    - "restructure skill"
    - "skill too long"
    - "organize skill"
    - "模块化skill"
---

# Skill Structure Organizer

## Overview

Guides the restructuring of OpenCode skills from single-file format to modular directory structure when they exceed complexity thresholds.

## Trigger Conditions

**Use this skill when:**
- A skill's SKILL.md exceeds 500 lines
- Multiple language/paradigm guides are embedded in single file
- Helper scripts need organization
- User mentions "restructure skill", "skill too long", "organize skill"

---

## The Iron Law

> **Core workflow stays in SKILL.md.** Detailed references go in subdirectories. Never mix them.

---

## Phase 1: Analysis

### Step 1.1: Assess Current Structure

```bash
# Count lines
wc -l .opencode/skills/<skill-name>/SKILL.md

# List current files
find .opencode/skills/<skill-name> -type f
```

### Step 1.2: Identify Extraction Candidates

| Content Type | Should Extract? | Target Directory |
|--------------|-----------------|------------------|
| Language-specific guides | Yes, if > 1 language | `references/languages/` |
| Paradigm-specific guides | Yes, if > 1 paradigm | `references/paradigms/` |
| Code examples (> 50 lines) | Yes | `examples/` |
| Templates/boilerplate | Yes | `templates/` |
| Helper scripts | Yes | `scripts/` |
| Core workflow (Phase 1-N) | No | Keep in SKILL.md |
| Quick reference | No | Keep in SKILL.md |
| Trigger conditions | No | Keep in SKILL.md |

### Step 1.3: Decision Matrix

```
IF SKILL.md < 400 lines:
    → Keep simple structure
    
ELIF SKILL.md < 600 lines:
    → Consider restructuring if:
        - Multiple language guides
        - Multiple paradigm guides
        - Helper scripts present
        
ELSE (SKILL.md >= 600 lines):
    → MUST restructure
```

---

## Phase 2: Create Directory Structure

### Step 2.1: Create Standard Directories

```bash
cd .opencode/skills/<skill-name>

# Create all potential directories
mkdir -p references/languages
mkdir -p references/paradigms
mkdir -p examples
mkdir -p templates
mkdir -p scripts
```

### Step 2.2: Directory Purpose

| Directory | Contents | File Format |
|-----------|----------|-------------|
| `references/languages/` | Language-specific guides | `{lang}.md` |
| `references/paradigms/` | Paradigm-specific patterns | `{paradigm}.md` |
| `examples/` | Code examples, patterns | `{type}-{pattern}.md` |
| `templates/` | Reusable templates | `{name}.py` or `.md` |
| `scripts/` | Executable helpers | `{name}.py` or `.sh` |

---

## Phase 3: Extract Content

### Step 3.1: Extract Language Guides

For each language section in SKILL.md:

1. Create `references/languages/{lang}.md`
2. Copy language-specific content
3. Add header with language name
4. Remove from SKILL.md

**Example extraction:**
```python
# Content to extract from SKILL.md:
## Python
| Anti-Pattern | Complexity | Solution |
...

# Becomes references/languages/python.md:
# Python Optimization Guide

## Anti-Patterns
| Anti-Pattern | Complexity | Solution |
...
```

### Step 3.2: Extract Paradigm Guides

Same process for paradigms → `references/paradigms/{paradigm}.md`

### Step 3.3: Extract Examples

Code examples over 50 lines → `examples/{type}.md`

### Step 3.4: Move Scripts

```bash
mv *.py scripts/
mv *.sh scripts/
```

---

## Phase 4: Update SKILL.md

### Step 4.1: Target Structure

Keep in SKILL.md (~300-400 lines):
- Frontmatter (with metadata.references)
- Overview
- Trigger Conditions
- The Iron Law
- Core Workflow (Phase 1-N)
- Quick Reference Card
- Tool Integration (brief)
- Reference Files table
- Integration Notes
- Red Flags
- Limitations

### Step 4.2: Add Reference Metadata

```yaml
---
name: skill-name
description: Brief description
metadata:
  references:
    languages: references/languages/
    paradigms: references/paradigms/
    examples: examples/
    templates: templates/
    scripts: scripts/
---
```

### Step 4.3: Add Reference Table

```markdown
## Reference Files

| Category | Location | Contents |
|----------|----------|----------|
| **Languages** | `references/languages/` | Python, JavaScript, Java, C++, Go guides |
| **Paradigms** | `references/paradigms/` | OOP, FP, Reactive, Concurrent patterns |
| **Examples** | `examples/` | Optimization patterns with before/after |
| **Templates** | `templates/` | Verification and benchmark templates |
| **Scripts** | `scripts/` | Helper tools |
```

---

## Phase 5: Create README.md

### Required Sections

```markdown
# Skill Name

> Brief description

## Overview
## Features
## Directory Structure
## Quick Start
## Installation
## Usage
## Quick Reference
## Example
## References (table)
## Integration
## Limitations
## License
## Author
## Links
```

---

## Phase 6: Verification

### Verification Checklist

- [ ] SKILL.md reduced to < 400 lines
- [ ] All extracted content in correct directories
- [ ] SKILL.md has reference table
- [ ] metadata.references added to frontmatter
- [ ] README.md created
- [ ] All internal links updated
- [ ] Scripts moved to scripts/
- [ ] Global installation updated

### Validation Commands

```bash
# Verify line count
wc -l .opencode/skills/<skill-name>/SKILL.md

# List new structure
find .opencode/skills/<skill-name> -type f | sort

# Check total files
find .opencode/skills/<skill-name> -type f | wc -l
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────┐
│        SKILL RESTRUCTURING WORKFLOW         │
├─────────────────────────────────────────────┤
│ 1. ANALYZE                                  │
│    Count lines, identify extraction targets │
│                                             │
│ 2. CREATE                                   │
│    mkdir references/ examples/ scripts/     │
│                                             │
│ 3. EXTRACT                                  │
│    Languages → references/languages/        │
│    Paradigms → references/paradigms/        │
│    Examples → examples/                     │
│    Scripts → scripts/                       │
│                                             │
│ 4. UPDATE                                   │
│    Add metadata.references                  │
│    Add reference table                      │
│    Reduce SKILL.md to < 400 lines           │
│                                             │
│ 5. DOCUMENT                                 │
│    Create README.md                         │
│                                             │
│ 6. VERIFY                                   │
│    Check all checklists                     │
└─────────────────────────────────────────────┘
```

---

## Anti-Patterns

| Anti-Pattern | Issue | Fix |
|--------------|-------|-----|
| Extract too much | Core workflow scattered | Keep Phases in SKILL.md |
| No reference table | Agent can't find guides | Add table to SKILL.md |
| Skip README.md | Poor discoverability | Always create README.md |
| Keep scripts in root | Disorganized | Always use scripts/ |

---

## Integration Notes

- Use after `SKILL_WRITING_BEST_PRACTICES` skill for guidance
- Works with `safe-refactoring` for safe restructuring
- Use `code-review-guardian` after restructuring for quality check

---

## Case Study: code-complexity-optimizer

### Before
```
SKILL.md: 721 lines (too long)
Scripts: Mixed in root directory
```

### After
```
SKILL.md: 357 lines (-50%)
+ 5 language guides in references/languages/
+ 4 paradigm guides in references/paradigms/
+ 3 example files in examples/
+ 1 template in templates/
+ 2 scripts in scripts/
+ README.md
```

### Key Changes
1. Extracted language-specific optimizations
2. Extracted paradigm-specific patterns
3. Separated code examples
4. Added reference metadata to frontmatter
5. Created comprehensive README.md
