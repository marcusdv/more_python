# ---------------------------------- ------------------------------------------------------
"""
    ► COMO ACESSAR E SETAR ATRIBUTOS UTILIZANDO VARIÁVEIS COM getattr() e setattr()

    Como setar um atributo em um objeto quando o nome do atributo é uma variável
    Não é possível fazer person.val1 = val2 ► erro
    Então se usa setattr(objeto, val1, val2)
    
    Não é possível fazer val3 = person.val1
    Então se usa getattr(objeto, val1)
"""


class Person():
    pass

person = Person()

val1 = 'first'
val2 = 'Costa'

# erro ► AttributeError: 'Person' object has no attribute 'first'
# person.val1 = val2

# erro ► AttributeError: 'Person' object has no attribute 'val'
# val3 = person.val

# então pode-se usar
setattr(person, val1, val2)

# e acessa-lá com
val3 = getattr(person, val1)


print(f'1 ► setattr {person.first}')
print(f'1 ► getattr {val3}')