"""
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

"""


"""

Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
							   //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
							   //   - The first, second, and third points
							   //   - The first, third, and fourth points
 

Constraints:

point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count.
"""

"""
approach -- 

using a hash map and make them as tuple 

also add the value for count with +1 every time duplicate
value comes 

how count works ? -- 

x1,y1 - x1,y2
  |       |
x2,y1 - x2,y2


check if the point in this format 


sort the mapper 

if (mapper[0][0] == mapper[1][0]) and (mapper[2][0] == mapper[3][0] )

and  (mapper[0][1] == mapper[1][1]) and (mapper[2][1] == mapper[3][1]) :

	return mapper.sort(keys) -> return first value
 
"""


class DetectSquares_wrong:

	def __init__(self):

		self.mapper = {}
		

	def add(self, point: List[int]) -> None:
		"""
		The function to make add in the dict 
		"""
		
		point = tuple(point)

		if point not in self.mapper :

			self.mapper[point] = 1 

		#increase if get duplicate value
		self.mapper[point] = self.mapper[point] + 1 
		

	def count(self, point: List[int]) -> int:
		"""
		The function to count the number of squares we can make 

		"""
		#make it tuple
		point = tuple(point)

		#add in the mapper
		if point not in self.mapper :

			self.mapper[point] = 1 

		else:

			self.mapper[point] = self.mapper[point] + 1 

		#sort the mapper
		self.mapper = dict(sorted(self.mapper.items()))

		mapper_lst = list(self.mapper.keys())

		#check the square can be formed or not 
		if abs(mapper_lst[0][0] - mapper_lst[1][0]) == 0 and  abs (mapper_lst[2][0] == mapper_lst[3][0]) == 0 :

			self.mapper = sorted(self.mapper.items(), key=lambda item: item[1])  

			return self.mapper[0]

		return 0








class DetectSquares():

	def __init__(self):

		self.mapper = {}


	def add(self,point) :
		"""
		The function to make the default point
		"""

		point = tuple(point)

		if point not in self.mapper :

			self.mapper[point] = 1

		else:

			self.mapper[point] = self.mapper[point] + 1
		

	def count(self,point) :
		"""
		The function to make the square 

		"""

		#make teh vars 
		x, y = point
		total_squares = 0


		for (px,py), count in self.mapper.items():

			if px != x and abs(px-x) == abs(py - y) :

				p1 = (x,py)
				p2 = (px,y)

				if p1 in self.mapper and p2 in self.mapper :

					total_squares += count * self.mapper[p1] * self.mapper[p2]


		return total_squares

























































