# Function to find the length of the shortest initial string
def shortest_initial_string(s):
    # Find the number of 1s at the beginning and end of the string
    prefix_ones = 0
    suffix_ones = 0
    n = len(s)

    for i in range(n):
        if s[i] == '1':
            prefix_ones += 1
        else:
            break

    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            suffix_ones += 1
        else:
            break

    # The shortest initial string would be the one with all 1s in between
    # the prefix and suffix 1s, plus the number of 0s added to the ends
    shortest_length = prefix_ones + suffix_ones + s.count('0')

    return shortest_length

# Input
T = int(input("Enter the number of test cases: "))

for _ in range(T):
    s = input().strip()
    result = shortest_initial_string(s)
    print(result)
