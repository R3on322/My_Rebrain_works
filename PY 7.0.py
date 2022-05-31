list = ['May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
        'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
        'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
        'May 20 11:01:12 PC-00102 PackageKit: daemon start',
        'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
        'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
        'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
        'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
        'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
        'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
        'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.']

#2.0

def list_func(list, *args):
        for i in range(len(args)):
                dict = {}
                dict['time'] = ' '.join(args[i][:3])
                dict['pc_name'] = ''.join(args[i][3])
                dict['service_name'] = ''.join(args[i][4]).rstrip(":")
                dict['message'] = ' '.join(args[i][5:])
                list.append(dict)

list = [i.split() for i in list]

#3.0

print_list = []
list_func(print_list, list[0], list[1], list[3])
for i in print_list:  #  можно и в одну строку, но мне вывод так больше нравится)
        print(i)
print()

#4.0

spisok = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

def proverka(id, full_space, free_space, free_space_percent):
        if free_space < 10 or free_space_percent < 5:
                print(f'Диск номер {id}. Cвободно: {free_space} ({free_space_percent} %) Gb из {full_space} Gb. Памяти очень мало!')
        elif free_space < 30 or free_space_percent < 10:
                print(f'Диск номер {id}. Cвободно: {free_space}({free_space_percent} %) Gb из {full_space} Gb. Памяти мало!')
        else:
                print(f'Диск номер {id}. Cвободно: {free_space}({free_space_percent} %) Gb из {full_space} Gb. Памяти достаточно!')

#5.0
def disk_size(list):
        dict_id = {'memory_critical':[], 'memory_not_enough': [], 'memory_ok': []}
        for disk_number in range(len(list)):
                id_disk = list[disk_number]['id']
                total = list[disk_number]['total']
                used = list[disk_number]['used']
                free_space = total - used
                full_space_Gb = round((total / 2 ** 30), 2)
                free_space_Gb = round((free_space / 2 ** 30), 2)
                used_space_Gb = round((used / 2 ** 30), 2)
                free_space_proc = round(((free_space * 100) / total), 2)

                if free_space_Gb < 10 or free_space_proc < 5:
                        dict_id['memory_critical'].append(id_disk)
                elif free_space_Gb < 30 or free_space_proc < 10:
                        dict_id['memory_not_enough'].append(id_disk)
                else:
                        dict_id['memory_ok'].append(id_disk)
                #проверка верности вывода данных:
                #proverka(id_disk, full_space_Gb, free_space_Gb, free_space_proc)

        return dict_id
#6.0

print(disk_size(spisok))