"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

	FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
	int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
	void add(int value) insert value to the queue.

"""


"""


Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1


"""


"""

approach can be using a counter of dict 

when get the data store in the collection counter 

and get the uinique value which comes 1 times and make as unique

when we add the value match with with unique value and update the collection counter as well 

if multplile unique we have move the pointer one step back to the new value

"""

from collections import Counter


class FirstUnique_wrong:

	def __init__(self, nums: List[int]):

		self.nums = nums

		self.mapper = Counter(self.nums)

		self.unique_lst = []

		for key in self.mapper:

			if self.mapper[key] == 1 :

				self.unique_lst.append(key)

		

	def showFirstUnique(self) -> int:
		"""
		The function to get the first value
		"""

		if len(self.unique_lst) > 0 :

			left_val = self.unique_lst.pop()

			self.unique_lst.insert(0,left_val)

			return left_val

		return -1



		

	def add(self, value: int) -> None:
		"""
		The function to add into the queue
		"""

		self.nums.append(value)

		self.mapper = Counter(self.nums)


















