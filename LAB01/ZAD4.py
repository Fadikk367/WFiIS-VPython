def get_divisors(num):
    divisors = []
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def get_perfect_numbers():
    perfect = []
    for i in range(1, 10000):
        if i == sum(get_divisors(i)):
            perfect.append(i)
    return perfect

print(get_perfect_numbers())