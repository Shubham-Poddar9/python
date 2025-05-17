def all_substrings(s):
    substrings = []
    n = len(s)
    
    for start in range(n):
        for end in range(start + 1, n + 1):
            substrings.append(s[start:end])
    
    return substrings

string = input("Enter a string: ")
result = all_substrings(string)
print("All substrings:")
for substr in result:
    print(substr)
