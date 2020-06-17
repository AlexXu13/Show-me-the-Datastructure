# -*- coding: utf-8 -*-

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self._size = capacity
        self._cache = {}
        self._keys = []


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self._cache:
            self._keys.remove(key)
            self._keys.insert(0,key)
            return self._cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self._cache:
            self._keys.remove(key)
            self._keys.insert(0,key)
            self._cache[key] = value
        elif len(self._keys) == self._size:
            last = self._keys.pop()
            self._cache.pop(last)
            self._keys.insert(0,key)
            self._cache[key] = value
        else:
            self._keys.insert(0,key)
            self._cache[key] = value

def test(number):
    our_cache = LRU_Cache(number)
    for i in range(1,number+1):
        our_cache.set(i, i)
    for i in range(1,number+1):
        print(our_cache.get(i)) #return i
    #edge case
    print(our_cache.get(number+5))


# test case1
print("NEW TEST :")
test(5)  #test set and get function ,then print all, including edge case

# test case2
print("NEW TEST :")
test(0)  #test set and get function ,then print all, including edge case

# test case3
print("NEW TEST :")
test(7)  #test set and get function ,then print all, including edge case

