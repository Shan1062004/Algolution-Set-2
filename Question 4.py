def is_palindrome(phrase):
    
    cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    
    return cleaned_phrase == cleaned_phrase[::-1]


test_phrase = "A man, a plan, a canal: Panama"
print("Is the phrase a palindrome?", is_palindrome(test_phrase))
