"""
leet code find the intersection of the arrays 
"""

#test casese 
nums1 = []
nums12 = []
out1 = []


nums2 = [1,4,2]
nums22 = [1,4]
out2 = [1,4]

nums3 = [1,1,1,1]
nums32 = [2,2,2]
nums3 = []

nums4 = [1,2,2,2,2,9]
nums42 = [1,4,9,10]
out4 = [1,9]



"""
sort both arrays 
nums1.sort()
nums2.sort()

two pointer in both arrays

l = 0 , nums1
r = 0 nums2 
interct_lst = []

loop over both array 
condn l < len(nums) or r < len(nums)

if nums1[l] < nums2[r]:
    l+=1

elif nums[l] > nums2[r]:
    r +=1

else:
    intesct_lst.append(nums[l])
    l+=1
    r+=1
"""


class Solution():

    def intersect(self,nums1,nums2):
        """
        The function to take two array and give there intersect
        """
        #sort the arrays 
        nums1.sort()
        nums2.sort()

        #initialize the pointers and list
        l , r = 0,0 
        intersect_lst = []

        #start the loop 
        while l < len(nums1) and r < len(nums2):

            if nums1[l] < nums2[r]:
                l+=1

            elif nums1[l] > nums2[r]:
                r+=1

            else:
                intersect_lst.append(nums1[l])
                l +=1
                r +=1

        
        return intersect_lst
        


sol = Solution()
res = sol.intersect(nums4,nums42)

print(res)