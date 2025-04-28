"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

"""


"""
Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104


"""


"""
approach -- 

gives one candy to start with one pass 

for 1st and last pos check right and left only 

in the second pass we compare the values of the rating 

and give the candy



"""



class Solution_Wrong:

    def candy(self, ratings: List[int]) -> int:
        """
        The function to distribute the candy as per rating of the children
        """

        #constraint case
        if len(ratings) == 1:

            return 1

        #first pass to give candy
        total_candy = [1] * len(ratings)

        #compare and give the cnady as per neigbors
        for i in range(len(ratings)) :

            if i == 0 :

                if ratings[i] > ratings[i+1] :

                    total_candy[0] = 2

            elif i == len(ratings) - 1 :

                if ratings[i] < ratings[i-1] :

                    total_candy[len(ratings)-1] = 2

            else :

                if ratings[i] > ratings[i-1] :

                    total_candy[i] = 2

                else :

                    total_candy[i-2] = 2

        return total_candy




class Solution:
    """
    passes leetcode
    """
    def candy(self, ratings: List[int]) -> int:
        """
        The function to find the min needed to give all people
        """

        n = len(ratings)

        #constraint case
        if n == 1:

            return 1

        #first pass to give candy
        total_candy = [1] * n

        #for the first pass
        for i in range(1,n) :

            if ratings[i] > ratings[i-1] :

                total_candy[i] = total_candy[i-1] + 1

        #second pass
        for i in range(n-2, -1,-1) :

            if ratings[i] > ratings[i+1] :

                total_candy[i] = max(total_candy[i], total_candy[i+1]+1)

        return sum(total_candy)


