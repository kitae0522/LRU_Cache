![Python badge](https://img.shields.io/badge/Python-v3.8-blue.svg)

# 1. Introduction
Cache memory is a high-speed semiconductor memory that is installed between CPU and main memory.

It is often useful to have these things in memory.
Of course, it is desirable to ensure that the capacity of cache memory does not become too large, as it slows down as capacity increases.

This module provides such a cache.

In most cases, the following may be used:

# 2. How to use this module

Default nodeMap form : **`nodeMap = {key: [value, count]}`**

The functions of the module are as follows.

| what it does              |      FUnc       |                             Remark |
| :------------------------ | :-------------: | ---------------------------------: |
| Search value in the Queue |    get(key)     |              Return value in 'key' |
| Put value in the Queue    | put(key, value) | Add 'value' corresponding to 'key' |

```python
from LRUCache import *  # import module

lru = LRUCache(2)   # Set Cache Size (args: int)

lru.put(1, 1)   # put(key, value)
print(lru.get(1))   # get(key)
print(lru.nodeMap)  # print nodeMap
```
This is a simple use.<br>
An example of using this is as follows.

## Example:

```python
from LRUCache import *

lru = LRUCache(2)

if __name__ == "__main__":
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # returns 1
    lru.put(3, 3)   # evicts key 2
    print(lru.get(2))   # returns -1 (not found)
    lru.put(4, 4)   # evicts key 1
    print(lru.get(1))   # returns -1 (not found)
    print(lru.get(3))   # returns 3
    print(lru.get(4))   # returns 4
    print(lru.nodeMap)  # show nodeMap
```

# 3. When does cache eviction occur?
By default, this cache only expires each time an item is stabbed, and all methods in this class are cleaned up.

# 4. Usage in Python3
Note that this module should probably not be used in python3 projects, since the standard library already has one. The only feature this one has which that one lacks is timed eviction.

# 5. Developer Info
- Developer : Song Kitae
- Feedback : kitae040522@gmail.com or leave an issue
- Git : [http://github.com/kitae0522/LRU_Cache](http://github.com/kitae0522/LRU_Cache)

# 6. Referenced Document
- [LRU Cache - 더블에스 devlog - 티스토리](https://doublesprogramming.tistory.com/254)
- [LRU Cache Algorithm 정리 - Jins' Dev Inside - 티스토리](https://jins-dev.tistory.com/entry/LRU-Cache-Algorithm-%EC%A0%95%EB%A6%AC)
- [LRU Cache 구현하기 (Least-Recently Used Cache (LRU ...)](https://0th-lab.tistory.com/6)
- [LRU Cache in Python using OrderedDict - GeeksforGeeks](https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/)
- [양파개발자 SW의 블로그입니다^^ : [LeetCode OJ] LRU Cache - Hard](http://oniondev.egloos.com/9749896)
