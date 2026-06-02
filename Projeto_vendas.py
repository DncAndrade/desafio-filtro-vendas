estoque = [
    {"produto": "Notebook", "quantidade": 5, "preco": 5000.00},
    {"produto": "Mesa", "quantidade": 7, "preco": 500.00},
    {"produto": "Teclado", "quantidade": 9, "preco": 250.00},
    {"produto": "Mouse", "quantidade": 100, "preco": 150.00},
    {"produto": "Monitor", "quantidade": 50, "preco": 700.00}
]
print ("--- / / --- / / --- / / --- / / ---")
print()
print (" Itens em estoque: ")
print ("  Escritório: \n - Notebook(5) = 5.000\n - Mesa(7) = 500,00\n - Teclado(9) = 250,00\n - Mouse(100) = 150,00\n - Monitor(50) = 700,00 ")
print()
print ("--- / / --- / / --- / / --- / / ---")
print()
produto = input("Digite o nome do produto: ")
valor = float(input("Qual o valor do produto: "))

if valor >= 1000:
    print ("Esse produto é Categoria Premium.")
else:
    print("Este produto é Categoria Padrão.")
    print()