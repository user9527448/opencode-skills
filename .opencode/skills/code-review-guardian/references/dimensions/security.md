# Security Review Guide

**Priority**: ALWAYS FIRST - Security review must be completed before any other dimension.

---

## OWASP Top 10 (2021)

| # | Risk | What to Look For | Severity |
|---|------|------------------|----------|
| A01 | Broken Access Control | Missing auth checks, IDOR, privilege escalation | 🔴 Critical |
| A02 | Crypto Failures | Weak algorithms, hardcoded keys, improper key management | 🔴 Critical |
| A03 | Injection | String concat in SQL/commands, LDAP, NoSQL | 🔴 Critical |
| A04 | Insecure Design | Missing security controls, business logic flaws | 🟡 High |
| A05 | Security Misconfiguration | Default creds, verbose errors, missing hardening | 🟡 High |
| A06 | Vulnerable Components | Outdated packages, known CVEs | 🟡 High |
| A07 | Auth Failures | Weak passwords, session fixation, missing MFA | 🔴 Critical |
| A08 | Software/Data Integrity Failures | Unvalidated updates, insecure deserialization | 🟡 High |
| A09 | Logging Failures | Missing audit trails, sensitive data in logs | 🟡 High |
| A10 | SSRF | User input in URLs, file imports | 🟡 High |

---

## Common Vulnerability Patterns

### SQL Injection

**❌ Vulnerable:**
```python
# Python
query = f"SELECT * FROM users WHERE id = {user_id}"

# Node.js
db.query("SELECT * FROM users WHERE id = " + userId)
```

**✅ Secure:**
```python
# Python (parameterized)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Node.js
db.query("SELECT * FROM users WHERE id = ?", [userId])
```

---

### Command Injection

**❌ Vulnerable:**
```python
os.system(f"ping {user_input}")  # Never do this
subprocess.call(user_input, shell=True)  # Dangerous
```

**✅ Secure:**
```python
# Use list form
subprocess.run(["ping", user_input], shell=False)

# Or validate input strictly
import re
if not re.match(r'^[a-zA-Z0-9.]+$', user_input):
    raise ValueError("Invalid input")
```

---

### Path Traversal

**❌ Vulnerable:**
```python
file_path = f"/var/files/{filename}"
with open(file_path) as f:
    return f.read()
```

**✅ Secure:**
```python
import os
from pathlib import Path

base_path = Path("/var/files")
file_path = (base_path / filename).resolve()

# Verify the resolved path is within base_path
if not str(file_path).startswith(str(base_path)):
    raise ValueError("Invalid path")
```

---

### Cross-Site Scripting (XSS)

**❌ Vulnerable:**
```javascript
// DOM XSS
element.innerHTML = userInput
document.write(userInput)

// Reflected XSS
res.send('<h1>' + req.query.name + '</h1>')
```

**✅ Secure:**
```javascript
// DOM XSS - use textContent or safe APIs
element.textContent = userInput
element.innerText = userInput

// Reflected - use template engines
res.render('template', { name: escapeHtml(req.query.name) })

// Use security headers
res.setHeader('Content-Security-Policy', "script-src 'self'")
```

---

### Hardcoded Secrets

**❌ Vulnerable:**
```javascript
const apiKey = "sk_live_abc123..."
const dbPassword = "secret123"
```

**✅ Secure:**
```javascript
// Use environment variables
const apiKey = process.env.API_KEY
const dbPassword = process.env.DB_PASSWORD

// Validate at startup
if (!apiKey) throw new Error('API_KEY is required')
```

---

### Insecure Direct Object Reference (IDOR)

**❌ Vulnerable:**
```javascript
// User can access any user's data
app.get('/api/user/:id', (req, res) => {
  const user = db.findUser(req.params.id)
  res.json(user)
})
```

**✅ Secure:**
```javascript
app.get('/api/user/:id', requireAuth, (req, res) => {
  // Verify user can access this resource
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Access denied' })
  }
  const user = db.findUser(req.params.id)
  res.json(user)
})
```

---

## Security Checklist

- [ ] All user inputs validated and sanitized
- [ ] No hardcoded credentials or secrets
- [ ] Authentication present on protected routes
- [ ] Authorization checked before operations
- [ ] Sensitive data encrypted at rest (AES-256)
- [ ] Sensitive data encrypted in transit (TLS 1.2+)
- [ ] Rate limiting on public endpoints
- [ ] CORS configured properly (whitelist origins)
- [ ] Security headers present (CSP, HSTS, X-Frame-Options, X-Content-Type-Options)
- [ ] Dependencies checked for known vulnerabilities
- [ ] Error messages don't leak sensitive information
- [ ] Logging doesn't capture sensitive data (passwords, tokens)
- [ ] File uploads validated and sandboxed
- [ ] Memory-safe languages used or memory issues addressed

---

## Severity Classification

| Severity | Criteria | Response Time |
|----------|----------|---------------|
| 🔴 Critical | RCE, SQL injection, auth bypass | Immediate |
| 🟠 High | XSS (persistent), CSRF, information disclosure | 24 hours |
| 🟡 Medium | Weak crypto, missing security headers | 1 week |
| 🟢 Low | Verbose errors, informational | Next release |

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/data/definitions/1000.html)
- [Mozilla Security Guidelines](https://wiki.mozilla.org/Security)
