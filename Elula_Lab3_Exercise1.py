
# List of sample integers
input_list = [2, 4, 3]

# Using list comprehension to find the square of odd numbers
output_list = [n**2 for n in input_list if n & 2 !=0]

print(output_list)