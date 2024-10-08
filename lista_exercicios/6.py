import math

def raizesSegundoGrau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não possui raízes reais"
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2

print(raizesSegundoGrau(1, -3, 2))
