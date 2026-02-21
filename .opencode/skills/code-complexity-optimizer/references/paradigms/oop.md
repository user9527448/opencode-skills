# Object-Oriented Programming Optimization

## Design Patterns for Performance

### Lazy Loading (Proxy Pattern)

```python
class ExpensiveResource:
    _instance = None
    _loaded = False
    
    @property
    def resource(self):
        if not self._loaded:
            self._instance = self._load_expensive()
            self._loaded = True
        return self._instance
    
    def _load_expensive(self):
        # Expensive initialization
        return load_from_database()
```

### Flyweight Pattern

```python
class TreeType:
    """Shared intrinsic state"""
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

class TreeFactory:
    _types = {}
    
    @classmethod
    def get_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._types:
            cls._types[key] = TreeType(name, color, texture)
        return cls._types[key]

class Tree:
    """Extrinsic state + reference to flyweight"""
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.type = tree_type  # Shared
```

### Object Pool

```python
from queue import Queue

class ConnectionPool:
    def __init__(self, factory, max_size=10):
        self.factory = factory
        self.pool = Queue(max_size)
        for _ in range(max_size):
            self.pool.put(factory())
    
    def acquire(self):
        return self.pool.get()
    
    def release(self, conn):
        self.pool.put(conn)

# Usage
with pool.acquire() as conn:
    conn.execute(query)
```

### Cache Invalidation (Observer)

```python
class Cache:
    def __init__(self):
        self._cache = {}
        self._observers = []
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def _notify(self, key):
        for observer in self._observers:
            observer.on_cache_invalidate(key)
    
    def invalidate(self, key):
        if key in self._cache:
            del self._cache[key]
            self._notify(key)
```

## OOP-Specific Optimizations

| Technique | When to Use | Impact |
|-----------|-------------|--------|
| Lazy Loading | Expensive initialization | Defer cost until needed |
| Flyweight | Many similar objects | Reduce memory |
| Object Pool | Expensive creation | Avoid allocation |
| Prototype | Clone vs create | Faster instantiation |
| Singleton | Shared state | Avoid duplication |

## Anti-Patterns

| Anti-Pattern | Issue | Fix |
|--------------|-------|-----|
| God Object | Single class does too much | Split responsibilities |
| Deep Inheritance | Hard to understand, slow dispatch | Prefer composition |
| Premature Encapsulation | Unnecessary getters/setters | Direct access where safe |
| Excessive Copying | Clone in setters | Immutable or reference |
