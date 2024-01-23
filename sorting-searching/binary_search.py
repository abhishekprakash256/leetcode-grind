"""
implement the binary search in the list 
"""

arr = [1,2,3,4,6,7,8,9]
n = 4 
out = True 

arr2 = []
n2 = 2 
out2 = False

arr3 = [1,2,3,4,5,6]
n3 = 3 
out3 = True 


arr4 = [1,2,3,4]
n4 = 4 
out4 = True 


arr5 = [1,2,3,4,5]
n5 = 5 
out5 = True 


arr6 = [1,2,3,4,5]
n6 = 10 
out6 = False


class Solution():

    def binarySearch(self,nums,n):
        """
        function to find the elelemnt in the sorted array 
        """

        #initilaize the pointers 
        l,r = 0 , len(nums) - 1

        #start the loop 
        while  l <= r : 
            
            #find the mid element 
            mid = (l+r) // 2

            if nums[mid] == n : 
                return True

            elif nums[mid] < n :
                
                l = mid + 1 
            
            else:

                r = mid - 1 


        return False


if __name__ == "__main__":

    sol = Solution()

    res = sol.binarySearch(arr5,n5)

    print(res)