main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if substring in main_string:
    print("Substring '{}' is present in the main string.".format(substring))
else:
    print("Substring '{}' is not present in the main string.".format(substring))
