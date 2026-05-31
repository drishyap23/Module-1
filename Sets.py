pasta_ingredients = {"tomato", "garlic", "olive oil", "chili", "pasta", "garlic"}
print(pasta_ingredients)
print(len(pasta_ingredients))

biryani_ingredients = {"rice", "chili", "garlic", "tomato", "protein", "spices"}

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chili")
print(pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
print("All ingredients:", all_ingredients)
print("Common:", common)

only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)
print("Only in Pasta:", only_pasta)
print("Not shared:", unique_to_each)