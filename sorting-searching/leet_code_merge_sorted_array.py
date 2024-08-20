"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of
 elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""


"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

"""


"""
approach 

brute force 
1. remove the zeros in the both arrays 
2. add the both array 
3. sort the merged array 


-------------------------
two pointer approach 

m and n can act as length of the traversal 

make a new empty list = []

i,j = 0,0
res_lst = []

while i + j < m+n:
    
    if nums1[i] < nums2[j]:
        res_lst.append(nums1[i])
        i +=1
    
    elif nums1[i] == nums2[j]:
        res_lst.append(nums[i])
        res_lst.append(nums[j])
        i +=1
        j +=1
    
    else:
        res_lst.append(nums2[j])
        j +=1

return res_lst


"""


class Solution_inc:
    def merge(self, nums1 : list, m: int, nums2 : list , n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #vars
        i , j = 0, 0 
        res_lst = []

        while i + j < m + n - 1:

            if nums1[i] < nums2[j] and i < m:
                res_lst.append(nums1[i])
                i +=1

            elif nums1[i] == nums2[j]:
                res_lst.append(nums1[i])
                res_lst.append(nums2[j])
                i +=1 
                j +=1
            
            elif nums1[i] > nums2[j] and j < n:
                res_lst.append(nums2[j])
                j +=1
        
        return res_lst
    

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        code passes leetcode
        """
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge nums1 and nums2 starting from the end of nums1 array
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1