def soma_e_media():
    numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media

print(soma_e_media())
