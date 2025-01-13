"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of 
all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
"""


"""

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".


Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.

"""


"""
approach -- 


using graph ? 

bread -> yeast, flour -> yeast, flour, meat 
sandwich -> bread, meat -> yeast, flour , meat 

graph of list -- 

bread -> [yeast,flour] -> { yeast, flour, meat }
sandwich -> [bread, meat] -> {yeast, flour, meat }


make hasmap of things 

one recipe with ingredients

res_lst = []

recipie = { bread : [yeast,flour] , sandwich : [bread, meat] } 

ingredinets = {yeast, flour, meat }



"""

class Solution_brute_force:
	def findAllRecipes(self, recipes, ingredients, supplies):
		"""
		The function to find the recipes that can be made given supplies and ingredients.
		"""
		# Create a supply map for quick lookup
		supply_map = set(supplies)
		result = []

		# Keep track of recipes that have already been checked
		recipes_checked = set()

		# Repeat until no new recipes can be made
		while True:

			found_new_recipe = False

			for i, recipe in enumerate(recipes):

				if recipe in recipes_checked:
					continue  # Skip recipes we've already processed

				# Check if all ingredients for this recipe are in supply_map
				if all(ingredient in supply_map for ingredient in ingredients[i]):
					supply_map.add(recipe)  # Add the recipe to supplies
					result.append(recipe)
					recipes_checked.add(recipe)
					found_new_recipe = True

			if not found_new_recipe:
				break  # Exit loop if no new recipes were added in this iteration

		return result




from collections import defaultdict, deque

class Solution():

	def findAllRecipes(self, recipes, ingredients, supplies):
		"""
		The function to find the recipies possible
		"""

		graph = defaultdict(list)
		in_degree = defaultdict(int)

		for recipie, recipie_ingrdients in zip(recipes,ingredients) :

			for ingredient in recipie_ingrdients :

				graph[ingredient].append(recipie)

				in_degree[recipie] += 1 

		
		queue = deque(supplies)

		result = []


		while queue :

			curr = queue.popleft()

			if curr in recipes :

				result.append(curr)


			for dependent_recipe in graph[curr] :

				in_degree[dependent_recipe] -= 1

				if in_degree[dependent_recipe] == 0 :

					queue.append(dependent_recipe)

		return result









recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]

sol = Solution()

print(sol.findAllRecipes(recipes,ingredients, supplies))







