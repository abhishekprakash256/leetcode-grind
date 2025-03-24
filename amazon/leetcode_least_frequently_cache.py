"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 
"""


"""
Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.


"""


"""
approach -- 

use two hash maps 

mapper_key_val = {}

mapper_key_freq = {} 

get()

put()

heapq

hepify per count 

hepq for count 

2:2 , 4:4

heapq ((1:2),(2:4))

{2:2 , 4 : 4}

make a mapper for storge 

store the count and key in heapq

check the key and return 


for the update pop the element and push the new with count 


"""
from collections import defaultdict, OrderedDict

class LFUCache:
	"""
	passes leetcode
	"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key: [value, freq]}
        self.freq_map = defaultdict(OrderedDict)  # {freq: OrderedDict({key: None})}
        self.min_freq = 0

    def _update(self, key):
        """Update frequency of an accessed key in O(1)."""
        value, freq = self.cache[key]

        # Remove key from current frequency list
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:  # If empty, remove the list
            del self.freq_map[freq]
            if self.min_freq == freq:  # Update min_freq if necessary
                self.min_freq += 1

        # Move key to the next frequency list
        self.cache[key] = [value, freq + 1]
        self.freq_map[freq + 1][key] = None

    def get(self, key: int) -> int:
        """Retrieve the value of key, update its frequency."""
        if key not in self.cache:
            return -1
        self._update(key)
        return self.cache[key][0]

    def put(self, key: int, value: int):
        """Insert or update a key-value pair in O(1)."""
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key][0] = value
            self._update(key)
            return

        if len(self.cache) >= self.capacity:
            # Remove the LFU key (min_freq list's first item)
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[evict_key]

        # Insert new key with freq 1
        self.cache[key] = [value, 1]
        self.freq_map[1][key] = None
        self.min_freq = 1  # Reset min_freq to 1 for new entry



