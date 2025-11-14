from biblioteca.texto import nomecompleto

assert nomecompleto("João", "Silva") ==  "João Silva", "Cenário 1 falhou"
assert nomecompleto("Maria", "Oliveira") == "Maria Oliveira", "Cenário 2 falhou" 
assert nomecompleto("Pedro", "dos Santos") == "Pedro dos Santos", "Cenario 3 falhou"

#Imprime  mensagem apenas se todos os casos de testes foram satisfeitos
print("Todos os testes passaram com sucesso")



