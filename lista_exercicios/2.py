def soma_digitos(num):
    if num < 100:
        return sum(int(x) for x in str(num))
    return "Número inválido"

print(soma_digitos(91))
