# Palindrome is string which reads sames left or right

def check_palindrome(user_word: str):
    """
    This Function will take string as input 
    and check if it is palindrome or not
    """

    print(f"Just testing input string {user_word}")

    if user_word[::-1] == user_word:
        return True
s = input("Enter your checking word: ")
result = check_palindrome(s)

if result:
    print("The word you entered is palindrome")

else:
    print("The word you entered is not palindrome")