# Review Scenario: React Component

## Context
Reviewing a new React component for user profile display.

## Code Under Review

```jsx
// components/UserProfile.jsx
import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

function UserProfile() {
  const { id } = useParams()
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    fetch(`/api/users/${id}`)
      .then(res => res.json())
      .then(data => {
        setUser(data)
        setLoading(false)
      })
  }, [id])
  
  if (loading) return <div>Loading...</div>
  
  return (
    <div>
      <h1>{user.name}</h1>
      <img src={user.avatar} />
      <p>{user.bio}</p>
      <button onClick={() => alert(user.email)}>Show Email</button>
      <div className="modal">
        <h2>Edit Profile</h2>
        <input type="text" placeholder="Name" />
      </div>
    </div>
  )
}
```

---

## Findings

### 🔴 Critical Issues

#### CRIT-001: Missing Alt Text
- **Category**: Accessibility
- **File**: `components/UserProfile.jsx:24`
- **Issue**: Image has no alt attribute
- **Impact**: Screen reader users can't understand image content
- **Fix**: Add alt text
  ```jsx
  <img src={user.avatar} alt={`${user.name}'s avatar`} />
  ```

---

### 🟠 High Issues

#### HIGH-001: Email Exposure
- **Category**: Security
- **File**: `components/UserProfile.jsx:25`
- **Issue**: Clicking button exposes email via alert
- **Impact**: Email can be extracted via DOM or screen readers
- **Fix**: Remove button or mask email

#### HIGH-002: Missing Error Handling
- **Category**: Correctness
- **File**: `components/UserProfile.jsx:17-21`
- **Issue**: No error handling for fetch failures
- **Impact**: Silent failures, poor UX
- **Fix**: Add error state
  ```jsx
  const [error, setError] = useState(null)
  
  useEffect(() => {
    fetch(`/api/users/${id}`)
      .then(res => {
        if (!res.ok) throw new Error('Failed to load')
        return res.json()
      })
      .then(data => {
        setUser(data)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [id])
  ```

---

### 🟡 Medium Issues

#### MED-001: Missing Form Label
- **Category**: Accessibility
- **File**: `components/UserProfile.jsx:27`
- **Issue**: Input has no associated label
- **Impact**: Screen reader users can't understand input purpose
- **Fix**: Add label
  ```jsx
  <label htmlFor="name-input">Name</label>
  <input id="name-input" type="text" placeholder="Name" />
  ```

#### MED-002: Keyboard Inaccessible Modal
- **Category**: Accessibility
- **File**: `components/UserProfile.jsx:26-29`
- **Issue**: Modal not focusable, no keyboard trap
- **Impact**: Keyboard users can't access modal
- **Fix**: Add proper modal attributes and focus management

---

### 🟢 Low Issues

- Loading state should be accessible (aria-busy)
- Consider showing loading indicator instead of text
- Modal should have role="dialog" and aria-modal="true"

---

## Report Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical | 1 |
| 🟠 High | 2 |
| 🟡 Medium | 2 |
| 🟢 Low | 2 |

**Key Takeaways**:
1. Always include alt text for images
2. Handle both loading and error states
3. Make modals accessible (ARIA + keyboard)
4. Never expose sensitive data in DOM
