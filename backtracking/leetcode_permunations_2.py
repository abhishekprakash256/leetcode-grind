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


        

"""
pass the i value and skip that 

sort 

and pass the index i + 1 

"""

class Solution_wrong2:

    def __init__(self):

        self.results = []

    def _helper_dfs(self,idx, permutations):
        """
        The helper function to make the permuattaion decision
        """

        #base case 
        if len(permutations) == len(self.nums) :

            self.results.append(permutations[:])

            return


        #make the recuriosn calls
        for i in range(idx, len(self.nums)) :

            permutations.append(self.nums[i])

            self._helper_dfs(i+1,permutations)

            permutations.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        The function to make permutation calls
        """

        self.nums = nums

        #constraint case 
        if len(self.nums) == 1 :

            return [self.nums]
        
        #make the recusion calls
        self._helper_dfs(0,[])

        return self.results





class Solution_worng3():

    def __init__(self):
        
        self.results = []

    def _helper_dfs(self,idx,permutations):
        """
        The helper function to make the dfs calls with condn
        """

        #base case
        if len(permutations) == len(self.nums):

            self.results.append(permutations[:])

            return

        #make the recursive calls
        for i in range(idx,len(self.nums)) :

            if i > 0 and self.nums[i] == self.nums[i-1] :

                continue

            permutations.append(self.nums[i])

            self._helper_dfs(i+1, permutations)

            permutations.pop()



    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        The function to make permutation calls
        """
        self.nums = nums

        self.nums.sort()

        #constraint case 
        if len(self.nums) == 1 :

            return [self.nums]

        #vars
        permutations = []

        #make the recursion calls
        self._helper_dfs(0,permutations)

        #make the return
        return self.results





from typing import List

class Solution:
    def __init__(self):
        self.results = []

    def _helper_dfs(self, used, path):
        # base case
        if len(path) == len(self.nums):
            self.results.append(path[:])  # copy the current path
            return

        for i in range(len(self.nums)):
            # Skip used elements
            if used[i]:
                continue
            # Skip duplicates
            if i > 0 and self.nums[i] == self.nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(self.nums[i])

            self._helper_dfs(used, path)

            path.pop()
            used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.nums = sorted(nums)
        used = [False] * len(nums)

        self._helper_dfs(used, [])

        return self.results





      












