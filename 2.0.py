string = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
string_lst = string.split()

PC_name = string_lst[3]
system = string_lst[4].rstrip(':')

failed_text = ' '.join(string_lst[5:11]).rstrip(":")

reason = string[-20:]

time = string[:15]

print(f'The PC {PC_name} receive message from service {system} what says {failed_text} because {reason} at {time}')