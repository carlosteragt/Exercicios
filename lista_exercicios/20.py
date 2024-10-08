def contar_vogais_espacos(s):
    vogais = "aeiouAEIOU"
    num_vogais = sum(1 for char in s if char in vogais)
    num_espacos = s.count(" ")
    return num_vogais, num_espacos

print(contar_vogais_espacos("Meu nome é Carlos"))
