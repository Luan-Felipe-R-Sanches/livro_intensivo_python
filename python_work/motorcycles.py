# Modificando, adicionando e removendo elementos
motorcycles = ["Harley Davidson", "Ducati", "Yamaha", "Kawasaki"]
print(motorcycles)

motorcycles[0] = 'Ducati'
motorcycles.append("Suzuki")
print(motorcycles)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# Inserindo elemtos em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removendo elementos de uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)


# Removendo elemento com método pop()
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# Removendo elementos de qualquer posição em uma lista
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned}.")

# Removendo um elemento por valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")