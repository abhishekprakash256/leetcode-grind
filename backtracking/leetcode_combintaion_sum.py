"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the

of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


"""
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40



"""



"""
approach -- 

using a dfs and tree structure 

if sum > target

    return 

if sum is equal to number then append 


repeat all the elemnets 
"""





from typing import List

class Solution:

    def __init__(self):
        self.results = []

    def _helper_dfs(self, start: int, combinations: List[int], total):
        """
        DFS to find unique combinations that sum to target
        """
            
        #base case 

        if total > self.target:

            return

        if total == self.target:

            self.results.append(combinations[:])

            return


        for i in range(start, len(self.candidates)):

            combinations.append(self.candidates[i])

            total += self.candidates[i]

            self._helper_dfs(i, combinations, total)  

            total -= self.candidates[i]

            combinations.pop()



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.candidates = candidates

        self.target = target

        self.results = []

        if len(self.candidates) == 1:

            if self.candidates[0] == self.target:

                self.results.append([self.candidates[0]])

                return self.results

        combinations = []
        
        total = 0 

        self._helper_dfs(0, combinations,total)

        return self.results
