def divisores(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(divisores(12))
