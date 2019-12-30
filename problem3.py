from functions import is_prime

n = 600851475143
q = n
fmax = 0

while q > 1:
    for i in range(2, q + 1):
        if is_prime(i):
            if q % i == 0:
                q = int(q / i)
                f = i
                if f > fmax:
                    fmax = f
                break

print(fmax)