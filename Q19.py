import string

input_string = input("Enter a string: ")
punctuations = string.punctuation

filtered_string = ''.join(char for char in input_string if char not in punctuations)

print("String with punctuation removed:", filtered_string)
