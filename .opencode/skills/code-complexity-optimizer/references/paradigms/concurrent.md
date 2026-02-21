# Concurrent/Parallel Programming Optimization

## Core Techniques

### Work Stealing

```python
from concurrent.futures import ThreadPoolExecutor
import queue

class WorkStealingPool:
    def __init__(self, num_workers):
        self.workers = [queue.Queue() for _ in range(num_workers)]
        self.num_workers = num_workers
    
    def submit(self, task, worker_id=None):
        if worker_id is None:
            worker_id = hash(task) % self.num_workers
        self.workers[worker_id].put(task)
    
    def steal_work(self, idle_worker_id):
        # Try to steal from other workers
        for i in range(self.num_workers):
            if i != idle_worker_id:
                try:
                    return self.workers[i].get_nowait()
                except queue.Empty:
                    continue
        return None
```

### Lock-Free Structures (Python example with atomic operations)

```python
import threading

class LockFreeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    @property
    def value(self):
        return self._value

# For true lock-free, use atomic operations in C/C++/Rust/Go
# Python GIL makes most operations effectively atomic for simple types
```

### Batch Processing

```python
from concurrent.futures import ThreadPoolExecutor

def process_batch(items):
    """Process items in batches to reduce synchronization overhead"""
    return [expensive_operation(item) for item in items]

def parallel_process(all_items, batch_size=100, max_workers=4):
    batches = [all_items[i:i+batch_size] 
               for i in range(0, len(all_items), batch_size)]
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(process_batch, batches)
    
    return [item for batch in results for item in batch]
```

### Data Sharding

```python
class ShardedCache:
    def __init__(self, num_shards=16):
        self.shards = [{} for _ in range(num_shards)]
        self.locks = [threading.Lock() for _ in range(num_shards)]
        self.num_shards = num_shards
    
    def _get_shard(self, key):
        return hash(key) % self.num_shards
    
    def get(self, key):
        shard_idx = self._get_shard(key)
        with self.locks[shard_idx]:
            return self.shards[shard_idx].get(key)
    
    def set(self, key, value):
        shard_idx = self._get_shard(key)
        with self.locks[shard_idx]:
            self.shards[shard_idx][key] = value
```

## Concurrency Patterns

| Pattern | Use Case | Benefit |
|---------|----------|---------|
| Thread Pool | CPU-bound tasks | Reuse threads |
| Connection Pool | Database/HTTP | Avoid connection overhead |
| Map-Reduce | Data processing | Parallel + combine |
| Pipeline | Multi-stage processing | Concurrent stages |
| Actor Model | Isolated state | No shared state |

## Async Patterns (Python)

```python
import asyncio

async def fetch_all(urls):
    """Concurrent async requests"""
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)

async def fetch_with_semaphore(urls, max_concurrent=10):
    """Limit concurrent requests"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def fetch_limited(url):
        async with semaphore:
            return await fetch(url)
    
    return await asyncio.gather(*[fetch_limited(u) for u in urls])
```

## Concurrent-Specific Optimizations

| Technique | When to Use | Impact |
|-----------|-------------|--------|
| Work Stealing | Unbalanced workloads | Better load distribution |
| Lock-Free | High contention | Avoid blocking |
| Batching | High-frequency ops | Reduce synchronization |
| Sharding | Shared data structures | Reduce contention |
| Async I/O | I/O-bound tasks | Non-blocking |

## Anti-Patterns

| Anti-Pattern | Issue | Fix |
|--------------|-------|-----|
| Too many threads | Context switching overhead | Use thread pool |
| Lock granularity | Too coarse = contention | Fine-grained locks |
| Deadlock | Circular wait | Lock ordering, timeout |
| Race condition | Non-atomic operations | Proper synchronization |
