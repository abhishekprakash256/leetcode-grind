"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) 
subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

"""


"""

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104


"""



"""
appprioch -- 


make all the subarray get the with the min 

how to check ? 

check with the least value is there ? 

make a _helper_dfs -- 

check if the min value in the temp_combination 

then make it 

get the min and add the value 

fist make teh combinfation and add 

"""



from typing import List


class Solution_slow:
    """
    The solution is slow 
    """

    def __init__(self):

        self.results = 0 
        self.MOD = 10 ** 9 + 7

    def _helper_dfs(self,idx,temp_lst):
        """
        The fuunctoin to make the combinations with min value 
        """

        #base case 
        if temp_lst :

            self.results += min(temp_lst)

        #make the recursive calls 

        if idx < len(self.arr) :

            self._helper_dfs(idx + 1 , temp_lst + [self.arr[idx]])


        



    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        The function to find the min array sum 
        """

        #constraint case 
        if len(arr) == 1 :

            return arr[0]

        self.arr = arr
        self.min_val = min(self.arr)

        #vars 
        temp_lst = []

        #the function calls 
        for i in range(len(arr)) :

            self._helper_dfs(i,temp_lst)

        return self.results % MOD






class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] # keep index for the latest smaller values
        res = [0] * len(arr)

        for i in range(len(arr)):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack :

                j = stack[-1] 
            else :
                
                j = -1

            res[i] = res[j] + (i - j) * arr[i]

            stack.append(i)
        
        return sum(res) % (10**9+7)





















# Example usage




arr = [3,1,2,4]

sol = Solution()


print(sol.sumSubarrayMins(arr))




