def is_palindrome(input_value):
    # Convert input to string for uniform handling of both strings and numbers
    input_str = str(input_value)
    
    # Reverse the string and compare it to the original
    if input_str == input_str[::-1]:
        return True
    else:
        return False

# Test the function
user_input = input("Enter a word or number to check: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
