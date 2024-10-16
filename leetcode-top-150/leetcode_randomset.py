"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""


"""
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

"""


"""

data structure 
set 
hashmap as well 

random = int(0,len(set))

set.add()

set.remove()




"""

import random


class RandomizedSet_brute:
	"""
	Passes the leetcode but slow

	"""

	def __init__(self):
		self.set_map = set()

	def insert(self, val: int) -> bool:
		if val in self.set_map:
			return False
		else:
			self.set_map.add(val)
			return True

	def remove(self, val: int) -> bool:
		if val in self.set_map:
			self.set_map.remove(val)
			return True
		else:
			return False

	def getRandom(self) -> int:
		# Convert set to list to access by index
		set_list = list(self.set_map)
		# Get a random index between 0 and len(set_list) - 1
		val = random.randint(0, len(set_list) - 1)
		return set_list[val]



import random


class RandomizedSet:

    def __init__(self):
        self.lst = []  # List to store elements
        self.mapper = {}  # Dictionary to store element-to-index mappings

    def insert(self, val: int) -> bool:
        """
        Insert the value if not present. Returns True if inserted, False if already exists.
        """
        if val in self.mapper:
            return False  # Value already exists
        
        # Append to the list and store its index in the dictionary
        self.lst.append(val)
        self.mapper[val] = len(self.lst) - 1  # Store the index
        return True

    def remove(self, val: int) -> bool:
        """
        Remove the value from the set. Returns True if the value existed, False otherwise.
        """
        if val not in self.mapper:
            return False  # Value doesn't exist

        # Get index of the element to remove
        idx_to_remove = self.mapper[val]
        
        # Move the last element in the list to the index of the element to remove
        last_element = self.lst[-1]
        self.lst[idx_to_remove] = last_element  # Replace with the last element
        self.mapper[last_element] = idx_to_remove  # Update the index of the last element
        
        # Remove the last element from the list
        self.lst.pop()
        del self.mapper[val]  # Remove from the dictionary

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.lst:  # Check if the list is empty
            raise ValueError("RandomizedSet is empty")
        
        idx = random.randint(0, len(self.lst) - 1)
        return self.lst[idx]













