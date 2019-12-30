from functions import is_prime

n_prime = 0
n = 1
prime_max = 10001

while n_prime < prime_max:
    n = n + 1
    if is_prime(n):
        n_prime = n_prime + 1
    

print(n)
    