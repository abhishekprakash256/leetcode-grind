"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either
 empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4]
  is [2, 3].
"""

"""
examples - 
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []



"""

"""

list length can vary 

list can be 0 too 

both list have to merge 

[[0,2],[5,10],[13,23],[24,25]]
    
[[1,5],[8,12],[15,24],[25,26]]

[1,2] , [5,5] , [8,10], []


combine the array ---

[0,2][1,5][5,10],[8,12],[13,23],[15,24],[24,25],[25,26]

[1,2], [5,5],[8,10],[15,23],[24,24],[25,25]


sort both the array 

max_first = 
min_last = 

problem = can't keep the equal ones

how to do ? 

[[0,2],[5,10],[13,23],[24,25]]
    
[[1,5],[8,16],[17,24],[25,26]]

check for last interval ?? 


"""

class Solution:
    """
    passes leetcode
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        The function to combine the intervals in the given lists and give out the intersection
        """

        #constraint case of no list
        if not firstList or not secondList :

            return []

        #ptrs 
        i , j = 0 , 0 

        #result list
        result = []

        #start the iteration 
        while i <= len(firstList) - 1 and j <= len(secondList) - 1 :

            lo = max(firstList[i][0] , secondList[j][0])
            high = min(firstList[i][1] ,secondList[j][1] )

            if lo <= high :

                result.append([lo,high])


            if firstList[i][1] < secondList[j][1] :

                i +=1 

            else :

                j += 1

        return result
