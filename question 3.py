# 1. Prompts the user to enter a positive number n.
n = int(input("Enter a number"))
# 2. Uses a loop (for) to calculate and display the sum of all even numbers from 1.
sum_even = 0
for i in range(2, n+1, 2):
    sum_even += i
print(f"Sum of even numbers: {sum_even}")