import humanize

spisok = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

disk_number = int(input(f'Введите номер накопителя(от 0 до {len(spisok)-1}, который нужно проверить: '))
print()

#2.0

print('Через round:')

total = spisok[disk_number]['total']
used = spisok[disk_number]['used']
free_space = total - used
full_space_Gb = round((total/2**30), 2)
free_space_Gb = round((free_space/2**30), 2)
used_space_Gb = round((used/2**30), 2)
free_space_proc = round(((free_space * 100)/total), 2)
print(f'Всего места: {full_space_Gb} Гб, использовано места: {used_space_Gb} Гб')
print(f'Свободного места: {free_space_Gb} Гб, {free_space_proc} %')
print()


print('Через humanize:')
total = spisok[disk_number]['total']
used = spisok[disk_number]['used']
free_space = total - used
full_space_Gb_hum = humanize.naturalsize(total, binary=True)
free_space_Gb_hum = humanize.naturalsize(free_space, binary=True)
used_space_Gb_hum = humanize.naturalsize(used, binary=True)
free_space_proc_hum = round(((free_space * 100)/total), 2)
print(f'Всего места: {full_space_Gb_hum}, использовано места: {used_space_Gb_hum}')
print(f'Свободного места: {free_space_Gb_hum}, {free_space_proc_hum} %')
print()

#3.0

if free_space_Gb < 10 or free_space_proc < 5:
    print(f'На накопителе {disk_number} критически мало свободного места')
elif free_space_Gb < 30 or free_space_proc < 10:
    print(f'На накопителе {disk_number} мало свободного места')
else:
    print(f'На накопителе {disk_number} достаточно свободного места')