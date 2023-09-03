# Define a function to calculate the area of a square
def calculate_area(side_length):
    area = side_length ** 2
    return area

# Input: Get the length of the side of the square from the user
side_length = float(input("Enter the length of the side of the square: "))

# Calculate the area using the function
area_of_square = calculate_area(side_length)

# Output: Display the calculated area
print(f"The area of the square with side length {side_length} is {area_of_square}")
