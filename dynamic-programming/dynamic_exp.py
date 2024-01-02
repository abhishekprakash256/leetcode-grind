"""
make the fibonacci series 
"""

#find the fibboncai series 
"""
the fucntion for finding the fibbonaci serires 
using memozation top bottom 
"""
def fibbo(n):

    if n <= 1:
        return 1 

    else:
        return fibbo(n-1) + fibbo(n-2)



#coin change problem 

"""
Problem: Find the minimum number of coins required to make a given amount using a set of coin denominations.
Example: Coin denominations: [1, 2, 5], amount:
using tabulation bottom up approach 
"""


def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

print(coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)




"""
Problem: Find the length of the longest common subsequence between two strings.
Example: Given strings "ABCBDAB" and "BDCAB," the longest common subsequence is "BCAB" with a length of 4.
using memoization top down 

"""

def longestCommonSubsequence(text1, text2, memo={}):
    if not text1 or not text2:
        return 0
    if (text1, text2) in memo:
        return memo[(text1, text2)]
    if text1[0] == text2[0]:
        memo[(text1, text2)] = 1 + longestCommonSubsequence(text1[1:], text2[1:], memo)
    else:
        memo[(text1, text2)] = max(longestCommonSubsequence(text1[1:], text2, memo), longestCommonSubsequence(text1, text2[1:], memo))
    return memo[(text1, text2)]

print(longestCommonSubsequence("ABCBDAB", "BDCAB"))  # Output: 4
