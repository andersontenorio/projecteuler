from functions import is_prime

n = 2000000
sum = 2
for i in range(3, n + 1, 2):
    if is_prime(i): 
        print(i)       
        sum = sum + i

print(sum)