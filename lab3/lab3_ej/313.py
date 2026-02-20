numbers = input().split()

prime_numbers = list(filter(lambda x: int(x) > 1 and all(int(x) % i != 0 for i in range(2, int(x)-1)), numbers))

if prime_numbers != []:
    print(*prime_numbers)
else :
    print("No primes")
