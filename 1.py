"""
    Documento com o objetivo de exercitar alguns truques com python
"""



# --------------------------- CONDIÇÕES CURTAS -------------------------------------------------------------

condition = False

if condition: 
    x = 1
else:
    x = 0
    
# Ou

y = 1 if condition else 0

print(f'1 ► x = {x} • y = {y}')
    
# ---------------------------- VIZUALIZANDO MELHOR GRANDES NUMEROS ------------------------------------------------------------

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'2 ► num1 = {num1} • num2 = {num2} • total = {num1 + num2}')
print(f'3 ► total = {num1 + num2:,}')

# ---------------------------- ABRINDO ARQUIVOS COM WITH------------------------------------------------------------

f = open('test.txt', 'r')

file_contents = f.read()

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(f'4 ► total de palavras = {word_count}')

# Melhor ►

# utilizando contexto?
with open('test.txt', 'r') as f:
    file_contents = f.read()
    
words = file_contents.split(' ')
word_count = len(words)
print(f'4 ► total de palavras = {word_count}')

# ---------------------------------- ENUMERATE ------------------------------------------------------

names = ['Corey', 'João', 'Bruna', 'Babidi']

index = 0
for name in names:
    print(f'5 ► index = {index} nome = {name}')
    
    index += 1
    
# Melhor ►
for index, name in enumerate(names):
    print(f'5 ► index = {index} nome = {name}')
    
# -------------------------------- ZIP --------------------------------------------------------

names = ['Corey', 'João', 'Bruna', 'Babidi']
heroes = ['Homem Aranha', 'Batman', 'Wolwerine', 'Goku']
idades = [16, 42, 41, 34]

for name, hero, idade in zip(names, heroes, idades):
    print(f'6 ► Nome = {name} Heroi = {hero} Idade = {idade}')

# com um único argumento, ele retorna uma tupla com todos os valores
for valores in zip(names, heroes, idades):
    print(f'6 ► Valores = {valores}')
    
# -------------------------------- ITEMS, KEYS, VALUES  --------------------------------------------------------

dic = {'nome': 'joão', 'idade': 40, 'nacionalidade': 'brasileira'}

for key, value in dic.items():
    print(f'7 ► key, value =  {key, value}')
    
for key in dic.keys():
    print(f'7► key = {key}')

for value in dic.values():
    print(f'7► value = {value}')
    
# -------------------------------- Unpacking --------------------------------------------------------
 
items = (1, 2)

a, b = items
c, d = (3, 4)
e, f = [5, 6]
# sets não mantém a ordem, por isso imprimiu 8, 7
g, h = {7, 8}

print(f'8 ► {a, b, c, d, e, f, g, h}')

# -------------------------------- Ignorando variavel, "COm exemplo em unpacking" --------------------------------------------------------

# Maneira convencional de ignorar um valor é "_"
i, _ = 4, 6
i, _, _, _, j = 1, 2, 3, 4, 6
_, _, _, *k  = 1, 2, 3, 4, 6
l, *_   = 1, 2, 3, 4, 6
*_, m, n   = 1, 2, 3, 4, 6

print(f'9 ► i, j = {i, j}')
print(f'9 ► k = {k}')
print(f'9 ► m, n  = {m, n}')

