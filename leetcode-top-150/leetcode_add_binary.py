"""
Given two binary strings a and b, return their sum as a binary string.

"""

"""
Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itse

"""


"""
approach --- 

carry = 0 

make both the aray equal and 0 on smaller array

play with carry rule 


"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.
        """
        # Make the lengths equal by padding with leading zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)  # Pad with zeros to the left
        b = b.zfill(max_len)
        
        carry = 0
        result = []
        
        # Traverse from right to left
        for i in range(max_len - 1, -1, -1):
            # Convert characters to integers and calculate the sum
            sum_val = int(a[i]) + int(b[i]) + carry
            
            # Determine the bit to add to the result and the carry
            result.append(str(sum_val % 2))  # Append remainder (0 or 1)
            carry = sum_val // 2  # Update carry (0 or 1)
        
        # If there's a leftover carry, add it to the result
        if carry:
            result.append('1')
        
        # The result is in reverse order, so reverse it back
        return ''.join(result[::-1])

# Example usage:
solution = Solution()
print(solution.addBinary("11", "1"))  # Output: "100"











