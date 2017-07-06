import socket
import re


print_data =''

with open('print.config', 'r') as f:
    for line in f.readlines():
        print_data += line
        # print(line)
# print(print_data)

main_data = {
        'ip' : '10.125.24.220',
        'port' : '9100',
        'barcode':'CJF 202423',
        'vin':'LJDDAA22170202423',
        'spec':'D242342GP3',
        'ocn':'L313',
        'nation':'A07VC',
        'inclr':'NZ',
        'outclr':'VR',
        'order':'D0704L313',
        'bodyno':'CJF 202423',
        'car':'CERATO',
        # 'ocn':'',
}

ip = main_data['ip']
port = main_data['port']

data_t = [main_data['barcode'],main_data['vin'],main_data['spec'],
          main_data['ocn'],main_data['nation'],main_data['inclr'],
          main_data['outclr'],main_data['order'],
          main_data['bodyno'],main_data['ocn'],main_data['car']]
# print(data_t)
# print(print_data.format(data_t)) # {0[0]},{0[1]}...
# print(print_data.format('CJF 202423', 'LJDDAA22170202423', 'D242342GP3', 'L313', 'A07VC', 'NZ', 'VR', 'D0704L313', 'CJF 202423', 'L313', 'CERATO'))

# change to byte

# send_data = b''
# with open('temp','w') as f:
#     f.write(print_data.format(data_t))
# with open('temp','rb') as f:
#     for line in f.readlines():
#         send_data += line
# send_data = print_data.format(data_t).encode('ascii')

def data_printer(main_data=main_data):
    # connect printer and print barcode
    data_t = [main_data['barcode'], main_data['vin'], main_data['spec'],
              main_data['ocn'], main_data['nation'], main_data['inclr'],
              main_data['outclr'], main_data['order'],
              main_data['bodyno'], main_data['ocn'], main_data['car']]
    send_data = print_data.format(data_t).encode('ascii')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        mess = ''
        try:
            s.connect((ip, int(port)))
            s.sendall(send_data)
            info = s.recv(1024)
            mess = 'print success!'
            return mess
        except:
            mess = 'connect failed!'
            return mess
    return info.decode('ascii')
    # return repr(info)

if __name__ == '__main__':
    mess = data_printer()
    print(mess)