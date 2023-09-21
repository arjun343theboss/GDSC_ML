def check_characters_present(string1, string2):
    
    string1 = string1.lower()
    string2 = string2.lower()

    
    set_string2 = set(string2)

    for char in string1:
        if char not in set_string2:
            return "No"
    
    return "Yes"


T = int(input("Enter the number of test cases: "))


for _ in range(T):
    
    input_strings = input("Enter two strings separated by a space: ").split()
    
    
    if len(input_strings) != 2:
        print("Invalid input format. Please enter two strings separated by a space.")
    else:
        string1, string2 = input_strings
        result = check_characters_present(string1, string2)
        print(result)
