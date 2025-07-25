"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

    HitCounter() Initializes the object of the hit counter system.
    void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
    int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).


"""


"""
Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.



"""


"""

using a hash map to store the hits with timestamp as the key and hit as val

the val can increase with  muitple hits 

sorted dict with keys 

and give the top -300s results total counter number 

"""

class HitCounter:

    def __init__(self):

    	self.hit_mapper = {}
        

    def hit(self, timestamp: int) -> None:
    	"""
		the function to store the hits
    	"""

    	#if the value is not in the hit mapper 
    	if timestamp not in self.hit_mapper:

    		self.hit_mapper[timestamp] = 1

    	#if the value in the hit mapper
    	self.hit_mapper[timestamp] = self.hit_mapper[timestamp] + 1

    	#sort the hit_mapper
        

    def getHits(self, timestamp: int) -> int:
    	"""
		function to get the hits
    	"""

    	last_timestamp = timestamp - 300

    	#find all the last till 300
    	




