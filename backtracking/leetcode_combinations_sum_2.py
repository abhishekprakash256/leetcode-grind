"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


"""


Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30



"""


"""
approch -- 

using a index 

pass the +1 index 

use the total to carry the sum 

"""


from typing import List

class Solution():

    def __init__(self):

        self.results = []

    def _helper_dfs(self,idx, combinations , total) :
        """
        The helper dfs function to make the combinations
        """

        #base case 
        if total > self.target :

            return

        #if the total equal
        if total == self.target :

            self.results.append(combinations[:])

            return


        for i in range(idx, len(self.candidates)) :

            # Skip duplicates: If the current element is the same as the previous one, skip it
            if i > idx and self.candidates[i] == self.candidates[i - 1]:
                
                continue

            combinations.append(self.candidates[i])

            self._helper_dfs(i + 1 , combinations , total + self.candidates[i])

            combinations.pop()


        

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        The function to make the sum combinations 
        """

        self.candidates = candidates

        self.target = target

        self.results = []

        self.candidates.sort()

        if len(self.candidates) == 1:

            if self.candidates[0] == self.target:

                self.results.append([self.candidates[0]])

                return self.results

        combinations = []
        
        total = 0 

        idx = 0 

        self._helper_dfs(idx, combinations, total )

        return self.results




candidates = [10,1,2,7,6,1,5]
target = 8



sol = Solution()
print(sol.combinationSum2(candidates , target))