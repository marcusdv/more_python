my_nums = [x * x for x in [1,2,3,4,5]]
print(my_nums)

#generator
my_nums_g = (x * x for x in [1,2,3,4,5])
print(my_nums_g)

# for num in my_nums_g:
#     print(num)

# transformar generator numa lista

listado = list(my_nums_g)
print(listado)