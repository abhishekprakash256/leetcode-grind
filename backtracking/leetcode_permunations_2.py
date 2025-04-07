"""

Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.
"""

"""
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10


"""

"""
appraoch -- 

using the index to iter 



"""


class Solution_wrong:

    def __init__(self):

        self.results = []

    def _helper_dfs(self,idx, permutations) :
        """
        The function to make helper dfs
        """

        #base case 
        if len(permutations) == len(self.nums) :

            self.results.append(permutations[:])


        #make the permutations
        for i in range(idx, len(self.nums)) :

            permutations.append(self.nums[i])

            self._helper_dfs(i+1, permutations)

            permutations.pop()


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        The function to make the permunations 
        """

        self.nums = nums

        #make the constraint case 
        if len(self.nums) == 1 :

            self.results.append(nums)

            return self.results
        
        #make the recursive funtion calls 
        self._helper_dfs(0,[])

        return self.results


        


