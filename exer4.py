from biblioteca.matematica import soma
# Validação de cenários de teste

assert soma(3, 7) == 10, "Cenário 1 falhou."
assert soma(6, 5) == 11, "Cenário 2 falhou."
assert soma(-2, 8) == 6, "Cenário 3 falhou."

# Imprime mensagem apenas se todos os casos de testes forem satisfeitos
print("todos os testes passaram com sucesso!")
