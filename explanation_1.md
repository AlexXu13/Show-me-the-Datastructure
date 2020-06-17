### LRU

As for the first problem, the task is to design a data structure known as Least Recently Used cache. The key point of this structure is that we must remove the least recently used entry when the cache memory reaches its limit.

### Implementation

- I selected dictionary to store key and value that I can use set and get function easily.
- I utilized a list "_keys" to store the updated keys status, after a set or a get operation， the list must be updated by using "key in dict" to identify the existence of corresponding keys.
- if it existed, pop this key from original position, and insert that key into the first position; if not existed, identify whether the size of keys list exceed the cache limit or not, if exceed, pop last key, and insert that key into the first position; if not exceed, insert that key into the first position directly.
Worst case time: O(1);

Space complexity: O(capacity)
