# Accessibility Review Guide (Frontend)

Ensure web applications are accessible to all users, including those using assistive technologies.

---

## WCAG 2.1 Principles

### Perceivable

| Guideline | Check |
|-----------|-------|
| Text Alternatives | Images have alt text |
| Captions | Videos have captions |
| Color Contrast | Ratio ≥ 4.5:1 (normal), ≥ 3:1 (large) |
| Resize Text | Works up to 200% zoom |

---

### Operable

| Guideline | Check |
|-----------|-------|
| Keyboard Accessible | All functionality via keyboard |
| Focus Visible | Focus indicators clearly visible |
| No Keyboard Traps | Can exit all controls |
| Enough Time | User controls for timing |

---

### Understandable

| Guideline | Check |
|-----------|-------|
| Language | Page has lang attribute |
| Consistent Navigation | Same patterns across pages |
| Error Identification | Errors clearly identified |

---

### Robust

| Guideline | Check |
|-----------|-------|
| Valid HTML | Proper element nesting |
| Name, Role, Value | ARIA used correctly |

---

## Common A11y Issues

### ❌ Bad Practices

```html
<!-- Missing alt text -->
<img src="chart.png">

<!-- Non-descriptive link -->
<a href="/details">Click here</a>

<!-- Missing form labels -->
<input type="text" placeholder="Email">

<!-- No heading hierarchy -->
<b>Title</b>
<span>Content</span>

<!-- Unfocusable modal -->
<div class="modal">...</div>
```

---

### ✅ Accessible Practices

```html
<!-- Descriptive alt text -->
<img src="chart.png" alt="Sales increased 20% in Q4">

<!-- Descriptive link text -->
<a href="/user/profile">View your profile</a>

<!-- Associated labels -->
<label for="email">Email:</label>
<input type="email" id="email">

<!-- Proper headings -->
<h1>Main Title</h1>
<h2>Section</h2>

<!-- Accessible modal -->
<div class="modal" role="dialog" aria-modal="true" 
     aria-labelledby="modal-title" tabindex="-1">
  <h2 id="modal-title">Confirm Action</h2>
  ...
</div>
```

---

## ARIA Attributes

| Attribute | Use |
|-----------|-----|
| `role` | Identifies widget type (dialog, button, etc.) |
| `aria-label` | Provides accessible name |
| `aria-labelledby` | Links to element that names this one |
| `aria-describedby` | Links to element that describes |
| `aria-hidden` | Hides from assistive tech |
| `aria-expanded` | Indicates expanded state |
| `aria-disabled` | Indicates disabled state |

---

## Accessibility Checklist

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

---

## Testing Tools

- **Automated**: axe, lighthouse, WAVE
- **Manual**: Keyboard-only navigation, screen reader testing
- **Contrast**: Color contrast analyzers
