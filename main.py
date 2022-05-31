string = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
string_lst = string.split()

print(string[:15])

print(string[24:34])

string_lst[3] = 'PC-12092'
print(*string_lst)

print(string.find('failed'))

print(string.lower().count('s'))

time_summa = [int(i) for i in string_lst[2].split(':')]
print(sum(time_summa))