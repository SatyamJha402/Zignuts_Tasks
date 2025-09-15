num = int(input("give me the number of primes to print: "))

def prime(n):
    primes = []
    num = 2
    while (len(primes) < n):
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return sum(primes)

print(prime(num))