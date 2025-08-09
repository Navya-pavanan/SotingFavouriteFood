foods = ["Pizza", "Biryani", "Burger", "Pasta", "Chocolate", "Sushi", "Dosa"]

n = len(foods)
for i in range(n):
    for j in range(0, n-i-1):
        if len(foods[j]) > len(foods[j+1]):
            foods[j], foods[j+1] = foods[j+1], foods[j]

print("Foods sorted by length:", foods)

