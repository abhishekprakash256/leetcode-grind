"""
Make the lru cache 

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
	If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""



"""






"""






class LRUCache:

    def __init__(self, capacity: int):
    	self.mapper = {}
    	self.lst = []
    	self.capacity = capacity
        

    def get(self, key: int) -> int:
    	"""
		The function to get the value
    	"""
    	
    	if key not in self.mapper:

    		return -1

    	else:
    		

        

    def put(self, key: int, value: int) -> None:
    	"""
		The function to put the value
    	"""

    	pass
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

		

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


