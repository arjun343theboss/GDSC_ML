# Function to find the length of the shortest initial string
def shortest_initial_string(final_string):
    n = len(final_string)
    
    # Find the longest prefix of 1s
    prefix_length = 0
    while prefix_length < n and final_string[prefix_length] == '1':
        prefix_length += 1
    
    # Find the longest suffix of 1s
    suffix_length = 0
    while suffix_length < n and final_string[n - suffix_length - 1] == '1':
        suffix_length += 1
    
    # The shortest initial string consists of all 0s between the prefix and suffix
    shortest_length = prefix_length + suffix_length
    
    return shortest_length

# Input
T = int(input("Enter the number of test cases: "))

for _ in range(T):
    final_string = input().strip()
    result = shortest_initial_string(final_string)
    print(result)
