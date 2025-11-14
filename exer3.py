# Definição da função 'soma'
from biblioteca.matematica import soma

# Validação de cenári de teste
assert soma(4, 5) == 9, "cenário 1 falhou."
assert soma(10, 15) == 25, "cenário 2 falhou."
assert soma("-3", "7") == 4, "cenario 3 falhou."


print("todos os testes passaram com sucesso!")