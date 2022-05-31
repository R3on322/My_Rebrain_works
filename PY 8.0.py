spisok = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

def mem_ok(list):
    for elem in list:
        id_disk = elem['id']
        total = elem['total']
        used = elem['used']
        free_space = total - used
        free_space_Gb = round((free_space / 2 ** 30), 2)
        free_space_proc = round(((free_space * 100) / total), 2)
#2.0
        if free_space_Gb < 10 or free_space_proc < 5:
            yield {'id': id_disk, 'memory_status': 'memory_critical'}
        elif free_space_Gb < 30 or free_space_proc < 10:
            yield {'id': id_disk, 'memory_status': 'memory_not_enough'}
        else:
            yield {'id': id_disk, 'memory_status': 'memory_ok'}

#3.0

list(a.update(b) for a, b in zip(spisok, [i for i in mem_ok(spisok)]))

#4.0

for i in spisok:
    print(i)

print()
#5.0

list_logs = [
    'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
    'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
    'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
    'May 20 11:01:12 PC-00102 PackageKit: daemon start',
    'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
    'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
    'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
    'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
    'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
    'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'
]
#6.0

list_logs = sorted([i.split() for i in list_logs], key=lambda x: x[2])
print(' '.join(list_logs[2]))

# print()
# for i in list_logs:
#    print(' '.join(i))

#7.0

list_pc_only = list(filter(lambda x: x[3] == "PC-00102", list_logs))
# for i in list_pc_only:
#     print(f'"PC-00102": {i}')

#8.0

list_messages = [' '.join(i[5:]) for i in list_logs if i[4].rstrip(':') == 'kernel']
# for i in list_messages:
#     print(f'Kernel: {i}')