numeros = [15, 3, 7, 30, 11, 8, 9, 16, 4, 20]
maior_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
print(f"o maior numero na lista é: {maior_numero}")