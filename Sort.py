# Bubble Sort: Sorting my favorite foods by name length

# List of my favorite foods
foods = ["Pizza", "Biryani", "Burger", "Pasta", "Chocolate", "Sushi", "Dosa"]

# Bubble Sort algorithm
n = len(foods)
for i in range(n):
    # Last i elements are already sorted
    for j in range(0, n-i-1):
        # Compare lengths of food names
        if len(foods[j]) > len(foods[j+1]):
            # Swap if the current item is longer than the next
            foods[j], foods[j+1] = foods[j+1], foods[j]

# Output the sorted list
print("Foods sorted by length:", foods)

# One-liner for GitHub submission:
# Sorted my favorite foods by name length using Bubble Sort.

