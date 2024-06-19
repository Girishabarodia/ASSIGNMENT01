lines = []
while True:
    line = input("Enter a line (press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

print("\n".join(lines))

