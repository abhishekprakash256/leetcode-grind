"""
find the duplicate in an array 
"""

#test cases
arr = [1,2,3,1]
out = True


arr2 = [1,2,3]
out2 = False

arr3 = [1]
out3 = False



#make the class for soln 



"""
1 .using the has map top check for the element O(n)
2. sorting O(n)
3. store in set and check the 

"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        mapper = {}

        if len(nums) == 1 or len(nums) == 0:
        	return False

        for i in nums:

        	if i not in mapper:
        		mapper[i] = True

        	else:

        		return True

        return False




if __name__== "__main__":
	sol = Solution()

	res1 = sol.containsDuplicate(arr2)
	print(res1)