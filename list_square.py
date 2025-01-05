# Sqauares using list concept

n = int(input("Enter the number till you wan't the square : "))
squares = [x ** 2 for x in range(n+1)]
print(squares)

# OP : Enter the number till you wan't the square : 10
#      [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ____________________________________________

# Cubes using list

n = int(input("Enter the number till you wan't the cubes : "))
cubes = [x ** 3 for x in range(n+1)]
print(cubes)

# Enter the number till you wan't the cubes : 10
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
