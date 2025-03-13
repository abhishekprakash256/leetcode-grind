"""
The median is the middle value in an ordered integer list. If the size of the list is even,
 there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual
 answer will be accepted.

"""


"""
Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

"""


"""
approach -- 

median is middle value 

if odd lemgth middle value 

if even length the two middle / 2 

inilialize the list 

addNum use the append 

findMedian 

get the length and get the median accordingly 

insert and sort()

o(nlogn)

[0,1,2,3,45]


"""

import heapq


class MedianFinder():

    def __init__(self):

        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        """
        The function to add the num value in the lists
        """

        #add in the left part 
        heapq.heappush(self.left, -num)

        if self.left and self.right and (-self.left[0] > self.right[0]) : 

            heapq.heappush(self.right, -heapq.heappop(self.left))


        if len(self.left) > len(self.right) + 1:

            heapq.heappush(self.right, -heapq.heappop(self.left))

        elif len(self.right) > len(self.left):

            heapq.heappush(self.left, -heapq.heappop(self.right))


    def findMedian(self) -> float:
        """
        The function to find the meadian value 
        """

        if len(self.left) > len(self.right):
            return -self.left[0]  # Max of left heap
        
        return (-self.left[0] + self.right[0]) / 2 




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



