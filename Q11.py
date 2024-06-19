n = int(input("Enter the number of terms: "))
a, b = 0, 1
fibonacci_sequence = []

for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b

print("The first", n, "numbers in the Fibonacci sequence are:", fibonacci_sequence)
