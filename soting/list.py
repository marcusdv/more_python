li = [9, 1, 8, 2, 7, 3, 6, 4, 5]


# Retorna uma nova lista
sorted_li = sorted(li)
reverse_li = sorted(li, reverse=True)


print(f'1 ► Sorted list = {sorted_li}')
print(f'2 ► Original list = {li}')


# Altera a lista original
li.sort()


print(f'3 ► Original list after sort() = {li}')
print(f'4 ► Reversed = {reverse_li}')


li2 = [-6, -5, -4, 1, 2, 3]


sorted_by_absolute_value = sorted(li2, key = abs)


print(f'{sorted_by_absolute_value}')