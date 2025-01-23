"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s)
receive the immediately following ranking number.
"""


"""

ranked = [100,90,90,80] -> 1,2,2,3 , { 100:1, 90:2, 80:3 }
player = [70,80,105] -> 4,3,1

ranked = [100,100,50,40,40,20,10] -> [1,1,2,3,3,4,5]
player = [5,25,50,120] -> [6,4,2,1]


approach --- 

make the array 

l , r = 0 , 1 

ranking = [1]

"""

"""
def climbingLeaderboard(ranked, player):
    # Remove duplicates and sort in descending order
    #code passes
    ranked = sorted(set(ranked), reverse=True)
    
    result = []
    n = len(ranked)
    
    for score in player:
        # Find the player's rank
        while n > 0 and score >= ranked[n - 1]:

            n -= 1

        result.append(n + 1)
    
    return result

"""


def climbingLeaderboard(ranked, player) :
	"""
	The function to put the players in the rank
	"""

	#make the set and sort it 
	ranked = sorted(set(ranked), reverse = True)

	#make the result list
	result = []

	#take the length
	n = len(ranked)

	for score in player :

		while n > 0 and score >= ranked[n-1]:

			n -= 1 

		result.append(n+1)

	return result




# Example Usage
ranked = [100, 90, 90, 80, 75, 60] #-> #[100,90,80,75,60]
player = [50, 65, 77, 90, 102] #-> #[100,90,80,75,60] 
print(climbingLeaderboard(ranked, player))  # Output: [6, 5, 4, 2, 1]










