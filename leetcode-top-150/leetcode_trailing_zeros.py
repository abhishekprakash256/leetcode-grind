"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""

"""
Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0

 

Constraints:

0 <= n <= 104


"""

"""
approach 

use a jump of 5 

0 factorial is 1 

1 factorial is 1 

"""



class Solution_wrong:

	def trailingZeroes(self, n: int) -> int:
		"""
		The function to find the trailing zeros 
		The above approach is wrong as uses more 5 in some cases
		"""


		#constraints
		if n == 0 :

			return 0

		#make the ptr
		i = 0

		#make the count
		count = 0

		while True :

			i += 5

			if i <= n :

				count += 1

			else:

				break

		return count



class Solution:
    def trailingZeroes(self, n: int) -> int:
    	"""
    	faster and passes leetcode

    	"""
        fives = 0

        i = 5

        while i <= n:

            fives += n // i
            
            i *= 5
        return fives


sol = Solution()

print(sol.trailingZeroes(10))