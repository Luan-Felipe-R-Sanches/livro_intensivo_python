# Criando uma variável com espaços em branco no início e no final
name = "\t\n  John Doe  \n\t"

# Exibindo o nome com os espaços em branco visíveis
print("Nome com espaços em branco:")
print(f"'{name}'")
print()

# Usando lstrip() - remove espaços à esquerda
print("Usando lstrip():")
print(f"'{name.lstrip()}'")
print()

# Usando rstrip() - remove espaços à direita
print("Usando rstrip():")
print(f"'{name.rstrip()}'")
print()

# Usando strip() - remove espaços de ambos os lados
print("Usando strip():")
print(f"'{name.strip()}'")