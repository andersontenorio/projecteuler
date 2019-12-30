from functions import is_palindromic

max_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if is_palindromic(n):
            if n > max_palindrome:
                max_palindrome = n

print(max_palindrome)
