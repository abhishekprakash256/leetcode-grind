"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least 
h papers that have each been cited at least h times.

"""

"""
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.



Input: citations = [1,3,1]
Output: 1


"""



"""

first find max 

max = (len(nums) % 2) + 1 

[0,1,3,5,6]

[1,1,3]

brute force approach -- 

[1,1,3] odd length len(nums) % 2 

[1,2,4,5]

(len(nums)%2) - 1 

a = [5, 2, 9, 1, 5, 6]

# Sort the value in increasing order
a.sort()
print(a)

---------------------------------------------

[3,0,6,1,5]

[0,1,3,5,6]
3

[1,3,1]

[1,1,3]
1

[0,1]
1

[0,0,0,1,1,2,2,3]
1

[0,0,0,0,0,1]
0

approach using this - 

sort the array 
nums.sort()

make a small choice till geater than half 

exception min is not 0 
not update the min if zero update only if greater than zero 
and return on the more than half length 








"""






class Solution():
    

    def hIndex_optimal(self, citations: List[int]) -> int:
        # h_index = max(h : published at least h papers cited at least h times)
        citations.sort()

        for i, v in enumerate(citations):
            if len(citations) - i <= v:
                return len(citations) - i
        
        return 0

    def hIndex(self, citations) -> int:
        """
        Find the H-index of the citations.
		passes leetcode 
        """
        # Base case: if only one paper
        if len(citations) == 1:
            return 1 if citations[0] > 0 else 0

        # Sort citations in ascending order
        citations.sort()

        hindex = 0
        r = len(citations) - 1

        # Iterate from the end of the sorted array
        while r >= 0:
            # Check if citations[r] is at least the number of remaining papers (h candidates)
            h_candidate = len(citations) - r  # Number of papers including this one
            if citations[r] >= h_candidate:
                hindex = h_candidate
            else:
                break  # Once we find a value less than h_candidate, we stop
            r -= 1

        return hindex




if __name__ == '__main__':
	sol = Solution()
	print(sol.hIndex([3,0,6,1,5]))





