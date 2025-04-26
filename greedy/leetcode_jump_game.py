"""
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element
 in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


"""


"""
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105


"""


"""
approach -- 

take a max value and keep subtrarting 1 

and replace the max when get higher 

start the jump = 0 

if jump < 0 :

    return False



max_jump = 0 

for i in nums :

    if max_jump < 0 :

        return False

    max_jump = max(max_jump , i)

    max_jump -= 1


return True
"""





class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        The funciton to find the car jump 
        """


        max_jump = 0 

        for i in nums :

            if max_jump < 0 :

                return False

            max_jump = max(max_jump , i )

            max_jump -= 1


        return True


        
























