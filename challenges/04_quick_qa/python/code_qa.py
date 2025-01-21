"""
Code Q&A Example

This file demonstrates how to use GitHub Copilot for quick code-related questions.
Each method contains patterns that you can ask questions about to understand:
- How they work
- Best practices
- Common pitfalls
- Performance implications
"""

from typing import Any, Callable, Dict, List, Optional, Set, TypeVar, Generic
from dataclasses import dataclass
from collections import defaultdict
import time
import asyncio
from weakref import WeakSet

T = TypeVar('T')

class CodeQA:
    """Collection of patterns for asking questions about code"""

    @staticmethod
    def create_observable_map():
        """
        TODO: Ask Copilot questions about the Observer pattern:
        - How does this implementation handle memory leaks?
        - What are the best practices for event handling?
        - When should we use weak references?
        - How can we implement unsubscribe?
        - What are the alternatives to this pattern?
        """
        observers: Set[Callable] = WeakSet()
        store: Dict[str, Any] = {}

        class ObservableMap:
            def set(self, key: str, value: Any) -> None:
                store[key] = value
                for observer in observers:
                    observer({'type': 'set', 'key': key, 'value': value})

            def get(self, key: str) -> Any:
                return store.get(key)

            def delete(self, key: str) -> None:
                value = store.get(key)
                if key in store:
                    del store[key]
                    for observer in observers:
                        observer({'type': 'delete', 'key': key, 'value': value})

            def observe(self, callback: Callable) -> Callable:
                observers.add(callback)
                return lambda: observers.remove(callback)

        return ObservableMap()

    @staticmethod
    def debounce(wait: float, leading: bool = False, trailing: bool = True) -> Callable:
        """
        TODO: Ask Copilot questions about debouncing:
        - What's the difference between debounce and throttle?
        - How does this handle edge cases?
        - When should we use leading vs trailing?
        - What are common use cases?
        - How can we cancel a pending execution?
        """
        def decorator(func: Callable) -> Callable:
            task: Optional[asyncio.Task] = None
            last_args: tuple = ()
            last_kwargs: dict = {}
            last_call_time: float = 0

            async def invoke_func() -> Any:
                nonlocal last_args, last_kwargs, last_call_time
                result = func(*last_args, **last_kwargs)
                last_args = ()
                last_kwargs = {}
                last_call_time = time.time()
                return result

            def should_invoke(current_time: float) -> bool:
                time_since_last_call = current_time - last_call_time
                return last_call_time == 0 or time_since_last_call >= wait

            async def wrapped(*args, **kwargs) -> Any:
                nonlocal task, last_args, last_kwargs
                current_time = time.time()
                is_invoking = should_invoke(current_time)

                last_args = args
                last_kwargs = kwargs

                if is_invoking and leading:
                    return await invoke_func()

                if task:
                    task.cancel()

                if trailing:
                    task = asyncio.create_task(invoke_func())
                    try:
                        return await task
                    except asyncio.CancelledError:
                        pass

            wrapped.cancel = lambda: task.cancel() if task else None
            return wrapped

        return decorator

    @staticmethod
    async def create_cancelable_task(coro) -> Dict[str, Any]:
        """
        TODO: Ask Copilot questions about task cancellation:
        - How does this handle cleanup?
        - What happens to in-flight operations?
        - How can we handle timeouts?
        - What are the race condition concerns?
        - When should we use asyncio.CancelledError?
        """
        task = asyncio.create_task(coro)
        
        def cancel():
            if not task.done():
                task.cancel()

        try:
            result = await task
            return {'task': task, 'result': result, 'cancelled': False}
        except asyncio.CancelledError:
            return {'task': task, 'result': None, 'cancelled': True}

    @staticmethod
    def memoize(maxsize: int = 1000, ttl: Optional[float] = None) -> Callable:
        """
        TODO: Ask Copilot questions about memoization:
        - How does this handle complex arguments?
        - What are the memory implications?
        - When should we clear the cache?
        - How can we implement LRU caching?
        - What are alternatives for performance optimization?
        """
        def decorator(func: Callable) -> Callable:
            cache: Dict[str, Dict[str, Any]] = {}

            def wrapper(*args, **kwargs) -> Any:
                key = str((args, sorted(kwargs.items())))
                
                if key in cache:
                    entry = cache[key]
                    if not ttl or time.time() - entry['timestamp'] < ttl:
                        return entry['value']
                    del cache[key]

                if len(cache) >= maxsize:
                    # Remove oldest entry
                    oldest_key = min(cache.items(), key=lambda x: x[1]['timestamp'])[0]
                    del cache[oldest_key]

                result = func(*args, **kwargs)
                cache[key] = {'value': result, 'timestamp': time.time()}
                return result

            wrapper.cache = cache
            wrapper.clear = cache.clear
            return wrapper

        return decorator

    @staticmethod
    def create_event_emitter():
        """
        TODO: Ask Copilot questions about event emitters:
        - How do we prevent memory leaks?
        - What's the best way to handle errors?
        - How can we implement event priorities?
        - When should we use async listeners?
        - What are the alternatives to pub/sub?
        """
        listeners: Dict[str, Set[Callable]] = defaultdict(set)

        class EventEmitter:
            def on(self, event: str, callback: Callable) -> Callable:
                listeners[event].add(callback)
                return lambda: self.off(event, callback)

            def off(self, event: str, callback: Callable) -> None:
                if event in listeners:
                    listeners[event].discard(callback)
                    if not listeners[event]:
                        del listeners[event]

            def emit(self, event: str, *args, **kwargs) -> None:
                if event in listeners:
                    for callback in list(listeners[event]):
                        try:
                            callback(*args, **kwargs)
                        except Exception as e:
                            print(f'Error in event listener: {e}')

        return EventEmitter()

async def run_examples():
    """Example usage of the patterns"""
    # Test observable map
    store = CodeQA.create_observable_map()
    unsubscribe = store.observe(print)
    store.set('user', {'name': 'Alice'})
    store.delete('user')
    unsubscribe()

    # Test debounce
    @CodeQA.debounce(1.0)
    def debounced_print(*args):
        print(*args)

    await debounced_print('Hello')
    await debounced_print('World')

    # Test cancelable task
    result = await CodeQA.create_cancelable_task(
        asyncio.sleep(1.0)
    )
    print(result)

    # Test memoization
    @CodeQA.memoize(maxsize=10, ttl=5.0)
    def compute(a: int, b: int) -> int:
        print('Computing...')
        return a + b

    print(compute(1, 2))
    print(compute(1, 2))  # Uses cache

    # Test event emitter
    emitter = CodeQA.create_event_emitter()
    off = emitter.on('message', print)
    emitter.emit('message', 'Hello')
    off()

if __name__ == "__main__":
    asyncio.run(run_examples())

# Practice exercises:
# TODO: Ask Copilot questions about these patterns
# 1. State management patterns
# 2. Async control flow
# 3. Memory management
# 4. Error handling strategies
# 5. Performance optimization 