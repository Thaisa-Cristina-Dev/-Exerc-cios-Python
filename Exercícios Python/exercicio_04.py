"""
4. Leia um número real e imprima o resultado do quadrado desse número.
"""

try:
    number = float(input("Digite um número inteiro: "))
except ValueError:
    print("O valor digitado deve ser um número inteiro.")
else:
    print(f"O quadrado do número {number:.2f} é: {number**2:.2f}")