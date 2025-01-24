"""
The factorial of the integer , written , is defined as:

Calculate and print the factorial of a given integer.

For example, if , we calculate  and get .

Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):

n: an integer
Note: Factorials of  can't be stored even in a  long long variable. 
Big integers must be used for such calculations. Languages like Java, Python, Ruby etc.
can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

"""

"""
approach of fatcorial 


if n == 0 :

	return 1 

if n == 1 :

	return 1 



"""


def factorial_rec(num):
	"""
	The function to find the factorial
	"""

	#base case 

	if num == 0 :

		return 1

	if num == 1 :

		return 1 

	return num * factorial_rec(num-1)


 
def factorial_dp(num):
	"""
	The function to find the factorial using DP 
	"""

	res = [1] * (num + 1)

	for i in range(1,num+1) :

		res[i] = i * res[i-1]


	return res[-1]



def extraLongFactorials(n):
    """
    The function to find the factorial using DP 
    passes
    """

    res = [1] * (n + 1)

    for i in range(1,n+1) :

        res[i] = i * res[i-1]


    print(res[-1])



def extraLongFactorials(n):
    """
    Function to calculate and print the factorial of a given integer n.

    :param n: An integer, the number to compute the factorial of
    """
    # Calculate factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Print the result
    print(factorial)


print(factorial_rec(25))

print(factorial_dp(25))

print(extraLongFactorials(25))