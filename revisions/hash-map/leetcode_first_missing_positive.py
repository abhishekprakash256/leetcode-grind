"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""

"""
Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

"""

"""

approach -- 

O(n) and O(1) space 

brute force 

max_num = max(nums)

for i in range(1, max_num + 1 ):

    if i not in nums :
        
        return i

"""

class Solution_wrong():

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        The function to find the first posirtive integer 
        """

        max_num = max(nums)

        for i in range(1,max_num + 1 ) :

            if i not in nums :

                return i

        return i + 1




"""
[3,4,-1,1]

[-1,1,3,4]

2 

[100000, 3, 4000, 2, 15, 1, 99999]

[1,2,3,15,4000,99999,100000]


"""



class Solution_wrong():

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        The function to find the first posirtive integer 
        """

        #constraint case 

        if len(nums) == 1:

            if nums[0] != 1 :

                if nums[0] < 1:

                    return 1 

                else:
                    return 1 
            
            else :

                return 2

        #sort the array 
        nums.sort()

        counter = 1 

        for i in range(0, len(nums)):

            if nums[i] > 0 :

                if counter != nums[i] :

                    return counter

                counter += 1

        return counter






class Solution():
    
    """
    passes leet code
    """
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = [n for n in nums if n > 0]

        for n in nums:
            idx = abs(n) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1