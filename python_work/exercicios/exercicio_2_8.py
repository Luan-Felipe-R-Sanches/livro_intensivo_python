filename = 'python_notes.txt'

# Exibindo o nome do arquivo original
print(f"Nome do arquivo original: {filename}")

# Usando removesuffix() para remover a extensão
filename_without_extension = filename.removesuffix('.txt')
print(f"Nome do arquivo sem extensão: {filename_without_extension}")