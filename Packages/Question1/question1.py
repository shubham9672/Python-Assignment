from mymodule import check_palindrome, reverse_str, even_odd
import random


print(f"Random number between 1 to 100 is {random.randint(1,101)}")

res = check_palindrome("madam")
res2 = reverse_str("programming")
res3 = even_odd(9)

print("", res,"\n",res2,"\n",res3)