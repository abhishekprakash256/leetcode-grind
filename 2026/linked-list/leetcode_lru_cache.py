"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

"""

"""

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.


"""

"""

need to make double linked list

head and tail removal and attach can happen 

use a hash map

when we get put at top 

mapper {3, node}

when get operation

check in the mapper

if presernt in mapper 

get the node 

set the node to head 

and put the head to tail

rerturn the node val



put function 

check the capacity 

if curr_capacity < capacity :

	the add in list 

	first add in the bead

	set the head to tail

	upodate the key in mapper as well 



"""

class Node:

	def __init__(self, val , key ):

		self.val = val

		self.key = key

		self.prev = None

		self.next = None




class LRUCache:

	def __init__(self, capacity: int):

		self.capacity = capacity

		self.mapper = {}

		self.head = Node(0,0)

		self.tail = Node(0,0)

		self.head.next = self.tail

		self.tail.prev = self.head




	def remove_node(self,node):
		"""
		The function to remove the node
		"""

		prev_node = node.prev

		next_node = node.next

		prev_node.next = next_node

		next_node.prev = prev_node


	def insert(self,node):
		"""
		The function to insert node in linked list
		"""

		node.next = self.head.next

		node.prev = self.head

		self.head.next.prev = node

		self.head.next = node	




	def get(self, key: int) -> int:
		"""
		The get method of LRU
		"""

		#case when key is not found
		if key not in self.mapper :

			return -1

		#get the node 
		node = self.mapper[key]

		#remove the node from last
		self.remove(node)

		#insert the node in front
		self.insert(node)

		return node.val




		

	def put(self, key: int, value: int) -> None:
		"""
		The put method on the LRU
		"""

		if key in self.mapper :

			self.remove(self.mapper[key])

		node = Node(key,value)

		self.mapper[key] = node

		self.insert(node)

		if len(self.mapper) > self.capacity :

			lru = self.tail.prev

			self.remove(lru)

			del self.mapper[lru.key]







