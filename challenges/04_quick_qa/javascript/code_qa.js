/**
 * Code Q&A Example
 * This file demonstrates how to use GitHub Copilot for quick code-related questions.
 * Each section contains code that you can ask questions about.
 */

class CodeQA {
    /**
     * Observable Map Implementation
     * Ask questions about:
     * - How does the observer pattern work?
     * - What are the use cases for observable data?
     * - How to handle memory leaks?
     * - Best practices for event handling
     */
    static createObservableMap() {
        const observers = new Set();
        const store = new Map();

        return {
            set(key, value) {
                store.set(key, value);
                observers.forEach(observer => observer({ type: 'set', key, value }));
            },
            get(key) {
                return store.get(key);
            },
            delete(key) {
                const value = store.get(key);
                store.delete(key);
                observers.forEach(observer => observer({ type: 'delete', key, value }));
            },
            observe(callback) {
                observers.add(callback);
                return () => observers.delete(callback);
            }
        };
    }

    /**
     * Debounce Implementation
     * Ask questions about:
     * - How does debouncing work?
     * - When to use debounce vs throttle?
     * - How to handle edge cases?
     * - Common use cases and best practices
     */
    static debounce(func, wait, options = {}) {
        let timeoutId;
        let lastArgs;
        let lastThis;
        let result;
        let lastCallTime = 0;
        const { leading = false, trailing = true } = options;

        const invokeFunc = (time) => {
            const args = lastArgs;
            const thisArg = lastThis;

            lastArgs = lastThis = undefined;
            lastCallTime = time;
            result = func.apply(thisArg, args);
            return result;
        };

        const shouldInvoke = (time) => {
            const timeSinceLastCall = time - lastCallTime;
            return lastCallTime === 0 || timeSinceLastCall >= wait;
        };

        const debounced = function(...args) {
            const time = Date.now();
            const isInvoking = shouldInvoke(time);

            lastArgs = args;
            lastThis = this;

            if (isInvoking && leading) {
                return invokeFunc(time);
            }

            clearTimeout(timeoutId);

            if (trailing) {
                timeoutId = setTimeout(() => invokeFunc(Date.now()), wait);
            }

            return result;
        };

        debounced.cancel = () => {
            clearTimeout(timeoutId);
            lastArgs = lastThis = undefined;
        };

        return debounced;
    }

    /**
     * Cancelable Promise Implementation
     * Ask questions about:
     * - How to handle promise cancellation?
     * - What are the race conditions?
     * - Error handling best practices
     * - Memory management considerations
     */
    static createCancelablePromise(promise) {
        let isCanceled = false;
        
        const wrappedPromise = new Promise((resolve, reject) => {
            promise.then(
                value => isCanceled ? reject({ isCanceled: true }) : resolve(value),
                error => isCanceled ? reject({ isCanceled: true }) : reject(error)
            );
        });

        return {
            promise: wrappedPromise,
            cancel: () => { isCanceled = true; }
        };
    }

    /**
     * Memoization Implementation
     * Ask questions about:
     * - How does memoization work?
     * - When to use memoization?
     * - Cache invalidation strategies
     * - Performance considerations
     */
    static memoize(fn, options = {}) {
        const cache = new Map();
        const { maxSize = 1000, ttl } = options;

        return function(...args) {
            const key = JSON.stringify(args);
            
            if (cache.has(key)) {
                const { value, timestamp } = cache.get(key);
                if (!ttl || Date.now() - timestamp < ttl) {
                    return value;
                }
                cache.delete(key);
            }

            if (cache.size >= maxSize) {
                const firstKey = cache.keys().next().value;
                cache.delete(firstKey);
            }

            const result = fn.apply(this, args);
            cache.set(key, { value: result, timestamp: Date.now() });
            return result;
        };
    }

    /**
     * Event Emitter Implementation
     * Ask questions about:
     * - How does pub/sub pattern work?
     * - Memory leak prevention
     * - Error handling in events
     * - Event ordering guarantees
     */
    static createEventEmitter() {
        const listeners = new Map();

        return {
            on(event, callback) {
                if (!listeners.has(event)) {
                    listeners.set(event, new Set());
                }
                listeners.get(event).add(callback);
                return () => this.off(event, callback);
            },
            off(event, callback) {
                const eventListeners = listeners.get(event);
                if (eventListeners) {
                    eventListeners.delete(callback);
                    if (eventListeners.size === 0) {
                        listeners.delete(event);
                    }
                }
            },
            emit(event, ...args) {
                const eventListeners = listeners.get(event);
                if (eventListeners) {
                    eventListeners.forEach(callback => {
                        try {
                            callback(...args);
                        } catch (error) {
                            console.error('Error in event listener:', error);
                        }
                    });
                }
            }
        };
    }
}

// Example usage and test cases
const observableMap = CodeQA.createObservableMap();
const unsubscribe = observableMap.observe(console.log);
observableMap.set('user', { name: 'Alice' });
observableMap.delete('user');
unsubscribe();

const debouncedFn = CodeQA.debounce(console.log, 1000);
debouncedFn('Hello');
debouncedFn('World');

const cancelable = CodeQA.createCancelablePromise(
    new Promise(resolve => setTimeout(() => resolve('Done'), 1000))
);
cancelable.promise.catch(console.log);
cancelable.cancel();

const memoizedFn = CodeQA.memoize(
    (a, b) => { console.log('Computing...'); return a + b; },
    { maxSize: 10, ttl: 5000 }
);
console.log(memoizedFn(1, 2));
console.log(memoizedFn(1, 2)); // Uses cache

const emitter = CodeQA.createEventEmitter();
const off = emitter.on('message', console.log);
emitter.emit('message', 'Hello');
off();

// Questions to ask Copilot:
// 1. How does the observer pattern in createObservableMap work?
// 2. What's the difference between debounce and throttle?
// 3. How to handle memory leaks in event emitters?
// 4. When should I use memoization?
// 5. What are the best practices for promise cancellation?

// Practice exercises:
// 1. Ask Copilot to explain the implementation details
// 2. Request suggestions for error handling improvements
// 3. Ask about performance optimizations
// 4. Get examples of real-world use cases
// 5. Learn about alternative implementations

module.exports = CodeQA; 