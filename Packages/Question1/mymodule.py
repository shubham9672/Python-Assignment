
def reverse_str(s):
    return f"Reverse string = {s[::-1]}"


def check_palindrome(s):
    return f"String is Plaindrome = {s[::-1] == s}"

def even_odd(n):
    if n%2==0:
        return "Number is even"
    return "Number is odd"