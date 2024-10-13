
def vowelsToUpper(s: str) -> str:
    # List of vowels
    vowels = "aeiouAEIOU"
    
    # Use list comprehension 
    return ''.join([ch.upper() if ch in vowels else ch for ch in s])

print(vowelsToUpper(""))
print(vowelsToUpper("Hello, world!"))
print(vowelsToUpper("hello hi bye"))