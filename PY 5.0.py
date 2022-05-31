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

list = [i.split() for i in list]
list_dict = []
for i in range(len(list)):
        dictionary = dict()
        dictionary['time'] = ' '.join(list[i][:3])
        dictionary['pc_name'] =  ''.join(list[i][3:4])
        dictionary['service_name'] = ''.join(list[i][4:5]).rstrip(":")
        dictionary['message'] = ' '.join(list[i][5:])
        list_dict.append(dictionary)
#3.0

for i in list_dict:
        print(f"Date: {i['time']}")
print()
#4.0

for i in list_dict:
        date = i['time'].split()
        time = date.pop(2)
        i['date'] = ' '.join(date)
        i['time'] = time

for i in list_dict:
        print(f"Time: {i['time']}")
print()
#5.0

pc_filter = [i['message'] for i in list_dict if i['pc_name'] == 'PC0078']
for i in pc_filter:
        print(f"Message: {i}")

#6.0

list_dict_to_dict = {}
for i in range(len(list_dict)):
        list_dict_to_dict[100+i] = list_dict[i]

#проверка
# for k,v in list_dict_to_dict.items():
#         print(f'Keys: {k}, Values: {v}')

print()
#7.0

print(list_dict_to_dict[104])