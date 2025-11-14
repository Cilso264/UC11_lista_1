def retorne(a, b):
    return (a ** b)
assert retorne(2, 3) == 8, "cenario 1 falhou."
assert retorne(5, 2) == 25, "cenario"
assert retorne(7, 0) == 1, "cenario 3 falhou."
print("Todos estão corretos")