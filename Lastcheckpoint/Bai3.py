def is_palindrome(s):
    return s == s[::-1]

def main():
    s = input("Input a text: ")
    if is_palindrome(s):
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")

main()