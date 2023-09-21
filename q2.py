n = int(input("Enter the value of n: "))

num = 1  # Initialize the starting number

# Loop to iterate through each row
for i in range(1, n + 1):
    # Loop to print the numbers in each row
    for j in range(i):
        print(num, end=" ")
        num += 1  # Increment the number for the next position
    print()  # Move to the next line after each row
