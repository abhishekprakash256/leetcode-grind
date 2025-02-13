"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

"""


"""
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""


"""

approach -- 

median odd -> then len(nums)//2 

median even -> then (len(nums) //2 , len(nums) //2 -1 ) / 2 

binary search ? 

brurte force 

will be array add 
then sort 

two pointer merging


compare and move and merge 


"""



from typing import List

class Solution_brute_force():

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The function to find the meadian of the array

        """

        #megee the array 
        nums1 = nums1 + nums2 

        #sort the array 
        nums1.sort()

        if len(nums1) % 2 == 0 :

            #even case 
            pos = (len(nums1) - 1) // 2 
            pos2 = ((len(nums1) -1 ) // 2) + 1

            return (nums1[pos] + nums1[pos2]) / 2

        else:

            #odd case 
            pos =  (len(nums1) - 1 ) // 2 

            return nums1[pos]



class Solution_slow():
    """
    passes leetcode but O(m+n) soln 
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The function to find the meadian of the array

        """

        #ptrs 
        l , r = 0 ,0 

        #lengths 
        length = len(nums1) - 1
        length2 = len(nums2) - 1

        #res array 
        result = []

        #mereg the array loop 
        while l <= length and r <= length2 :

            if nums1[l] < nums2[r] :

                result.append(nums1[l])

                l +=1

            else :

                result.append(nums2[r])

                r += 1

        #add the remaining 
        while l <= length :

            result.append(nums1[l])

            l +=1 


        while r <= length2 :

            result.append(nums2[r])

            r += 1 


        #the median logic
        
        if len(result) % 2 == 0 :

            #even case 
            pos = (len(result) - 1) // 2 
            pos2 = ((len(result) -1 ) // 2) + 1

            return (result[pos] + result[pos2]) / 2

        else:

            #odd case 
            pos =  (len(result) - 1 ) // 2 

            return result[pos]


 

class Solution_optim():
    """
    passes leetcode with log(m+n) time 
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:

            partition1 = (low + high) // 2

            partition2 = (m + n + 1) // 2 - partition1

            
            # Handle edge cases where partitions are at the beginning or end
            if partition1 == 0:
                maxLeft1 = float('-inf')  

            else :
                maxLeft1 = nums1[partition1 - 1]

            if partition1 == m :

                minRight1 = float('inf')  
            else :
                minRight1 = nums1[partition1]
            
            if partition2 == 0 :
                maxLeft2 = float('-inf')  
            else:
                maxLeft2 =  nums2[partition2 - 1]

            if partition2 == n :
                minRight2 = float('inf')  
            else:
                minRight2 = nums2[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Correct partition found, compute median
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Move left in nums1
                high = partition1 - 1
            else:
                # Move right in nums1
                low = partition1 + 1

