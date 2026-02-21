# Reactive Programming Optimization

## Core Patterns

### Debounce

```javascript
function debounce(fn, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn.apply(this, args), delay);
    };
}

// Usage: Only fire after 300ms of no activity
const debouncedSearch = debounce(search, 300);
input.addEventListener('input', debouncedSearch);
```

### Throttle

```javascript
function throttle(fn, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            fn.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Usage: Fire at most once every 100ms
const throttledScroll = throttle(handleScroll, 100);
window.addEventListener('scroll', throttledScroll);
```

### Backpressure

```javascript
// Buffer strategy
class BufferedProcessor {
    constructor(processFn, bufferSize = 100, flushInterval = 1000) {
        this.buffer = [];
        this.processFn = processFn;
        this.bufferSize = bufferSize;
        
        setInterval(() => this.flush(), flushInterval);
    }
    
    add(item) {
        this.buffer.push(item);
        if (this.buffer.length >= this.bufferSize) {
            this.flush();
        }
    }
    
    flush() {
        if (this.buffer.length > 0) {
            this.processFn(this.buffer);
            this.buffer = [];
        }
    }
}
```

### Cold vs Hot Observables

```javascript
// Cold: New execution for each subscriber
const cold$ = new Observable(observer => {
    // Runs for EACH subscriber
    fetch('/api/data').then(data => observer.next(data));
});

// Hot: Share execution among subscribers
const hot$ = cold$.pipe(share());
// Or replay last value
const hotReplay$ = cold$.pipe(shareReplay(1));
```

## RxJS Operators

```javascript
import { fromEvent } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';

// Search with debounce and cancel previous
const search$ = fromEvent(input, 'input').pipe(
    debounceTime(300),
    distinctUntilChanged(),
    switchMap(event => fetch(`/search?q=${event.target.value}`))
);

// Batch updates
import { bufferTime } from 'rxjs/operators';
const batched$ = events$.pipe(bufferTime(100));
```

## Reactive-Specific Optimizations

| Technique | When to Use | Impact |
|-----------|-------------|--------|
| Debounce | Rapid events (typing, resize) | Reduce processing frequency |
| Throttle | Continuous events (scroll, mouse) | Consistent rate |
| Buffer/Batch | High-frequency events | Amortize overhead |
| SwitchMap | Search/typeahead | Cancel stale requests |
| Share | Multiple subscribers | Single execution |
| Backpressure | Producers faster than consumers | Prevent overflow |

## Anti-Patterns

| Anti-Pattern | Issue | Fix |
|--------------|-------|-----|
| Unsubscribed subscriptions | Memory leak | Use takeUntil, async pipe |
| Nested subscriptions | Callback hell | Use switchMap, mergeMap |
| No error handling | Stream dies | Use catchError |
| Over-subscribing | Duplicate work | Use share/shareReplay |
