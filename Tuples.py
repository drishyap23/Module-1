pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
print(pasta)
print(pasta[0])
print(pasta[-1])

biryani = ("Biryani", "South Asian and Persian", 20, "Medium")
print(biryani)
print(biryani[0])
print(biryani[-1])

all_recipes = (pasta, biryani)
print(all_recipes[0][0])
print(all_recipes[1][2])
print(pasta[1:3])

for detail in pasta:
    print(" -", detail)