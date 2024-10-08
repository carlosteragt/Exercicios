def analisar_numeros():
    numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]
    soma = sum(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return soma, maior, menor

print(analisar_numeros()) 
