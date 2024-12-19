"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where 
one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it
a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number 
of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 
"""


"""
approach -- 






"""


class Solution:
	def minMutation(self,start,end,bank):
		"""
		The function to find the min value
		"""

		#base case 
		if start == end :
			return 0


		#make the queue 
		queue = [(start,0)]

		#make the seen set
		seen = set()

		#star the loop
		while queue :

			#take the node out 
			node ,step = queue.pop(0)

			#make the matching case
			if node == end :
				return step

			#explore the neighbor 

			for char in "ACGT" :

				for i in range(len(node)) :

					neighbor = node[:i] + char + node[i+1:]

					if neighbor not in seen and neighbor in bank:

						queue.append((neighbor,step + 1 ))
						seen.add(neighbor)

		return -1






