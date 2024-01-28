"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

"""


#test cases 

numCourses = 2, prerequisites = [[1,0]]
out = True 


numCourses2 = 2 , prerequisites2 = [[1,0],[0,1]]
out2 = False


class Solution():

	def canFinish(self,numCourses, prerequisites):
		"""
		The function to give the course output
		"""

		#make the list 

		premap = { i:[] for i in range(numCourses)}


		print(premap)



if __name__ == '__main__':
	sol =  Solution()
	res = sol.canFinish(numCourses,prerequisites)


	print(res)