"""
Make the calendar program to oput the events 
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

	MyCalendar() Initializes the calendar object.
	boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


"""


"""

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
"""

"""

interveal question 

min and max val ? 

when two value comes we calculate the min 

we caqlculate the max value

dict ? 

[10,15] [20,30 ] [40 ,50] , 

first and last 

sort and store 

10 , 15 , 20 , 30 

18 , 19 - 

18 , 24 - 




"""
from sortedcontainers import SortedList



class MyCalendar:

	def __init__(self):

		self.calendar = []
		

	def book(self, startTime: int, endTime: int) -> bool:
		"""
		The function to put the time slot
		"""

		for s,e in self.calendar :

			if startTime < e and s < endTime :

				return False

		self.calendar.append((startTime ,endTime))

		return True

		



class MyCalendar:
	"""
	The optim soln
	"""
    def __init__(self):
        self.start_events = SortedList()
        self.end_events = SortedList()

    def book(self, start: int, end: int) -> bool:


        left = bisect_right(self.end_events, start)


        right = bisect_left(self.start_events, end)

        if left == right:

            # add book
            self.start_events.add(start)
            self.end_events.add(end)
            
            return True
        else: return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)