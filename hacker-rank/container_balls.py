"""
David has several containers, each with a number of balls in it. He has just enough 
containers to sort each type of ball he has into its own container.
 David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

Each container contains only balls of the same type.
No two balls of the same type are located in different containers.


"""


"""
give out -- 

possible or impossible 

"""



"""
approach -- 

  0     1 
[1,1],[0,1]  -> possible

  0      1
[1,0], [0,1] -> impossible

brute force will be like 

for i in range(len(conatiners[0])):

	#start the swap two 



"""

def organizingContainers(containers):
	
    # Compute row sums (container capacities)
    containerSum = [sum(row) for row in containers]
    # Compute column sums (total balls of each type)
    typeSum = [sum(col) for col in zip(*containers)]
    
    # Sort both lists
    containerSum.sort()
    typeSum.sort()
    
    # Compare the sorted lists
    return "Possible" if containerSum == typeSum else "Impossible"