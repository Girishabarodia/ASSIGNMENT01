numbers = input("Enter numbers separated by spaces: ").split()
numbers = list(map(float, numbers))
sum_of_numbers = sum(numbers)
print("Sum of the numbers:", sum_of_numbers)
