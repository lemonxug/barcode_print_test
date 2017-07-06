import tkinter as tk
import hashlib
import socket
import json
# import barcode
import datetime
# from barcode.writer import ImageWriter
# from network import main_data,data_printer

# main window
window = tk.Tk()
window.title('BARCODE_V1')
window.geometry('400x550')
window.resizable(False, False)  # set no resizable

# global variables
main_data = {
    'ip': '10.125.24.220',
    'port': '9100',
    'barcode': 'CJF 202423',
    'vin': 'LJDDAA22170202423',
    'spec': 'D242342GP3',
    'ocn': 'L313',
    'nation': 'A07VC',
    'inclr': 'NZ',
    'outclr': 'VR',
    'order': 'D0704L313',
    'bodyno': 'CJF 202423',
    'car': 'CERATO',
    # 'ocn':'',
}
ocn_lock = True
config = ''
with open('print.config', 'r') as f:
    for line in f.readlines():
        config += line


# validate function


def limit_len(content, l):
    if len(content) > int(l):
        return False
    else:
        return True


def update_ocn(content):
    global ocn_lock
    if len(content) > 9:
        return False
    else:
        if ocn_lock:
            if len(content) > 5:
                ocn.set(content[5:])
            else:
                ocn.set('')
            return True
        else:
            pass
        # print(content)
        return True
        # pass


update_ocn_1 = window.register(update_ocn)
limit_len_1 = window.register(limit_len)
# layout
frm = tk.Frame(window, height=470, width=394, bg='white')
frm.pack()
can = tk.Canvas(frm, height=470, width=394, bg='white')
can.pack()
frm_l = tk.Frame(can, height=470, width=165, bg='white')
frm_l.place(x=15, y=5)
frm_r = tk.Frame(can, height=470, width=210, bg='white')
frm_r.place(x=183, y=5)
frm_r.pack_propagate(0)
frm_2 = tk.Frame(window, height=40, width=390, bg='white')
frm_2.pack()
frm_2.pack_propagate(0)
frm_3 = tk.Frame(window, height=30, width=390, bg='#00BFFF')
frm_3.pack()

# barcode
img_barcode = tk.PhotoImage(file="test1.png")
l_img_barcode = tk.Label(frm_l, width=150, height=410, bg='white', anchor='w')
l_img_barcode["image"] = img_barcode
l_img_barcode.place(x=5, y=20)

# data_t = [main_data['barcode'],main_data['vin'],main_data['spec'],
#           main_data['ocn'],main_data['nation'],main_data['inclr'],
#           main_data['outclr'],main_data['order'],
#           main_data['bodyno'],main_data['ocn'],main_data['car']]
# varible
car = tk.StringVar()
# car.set(main_data['car'])
car.set('CERATO')
bodyno = tk.StringVar()
bodyno.set('CJF 202423')
order = tk.StringVar()
order.set('D0704L313')
ocn = tk.StringVar()
if ocn_lock:
    ocn.set(order.get()[5:])
else:
    ocn.set('L313')
nation = tk.StringVar()
nation.set('A07A')
inclr = tk.StringVar()
inclr.set('NZ')
outclr = tk.StringVar()
outclr.set('VR')
spec = tk.StringVar()
spec.set('D242342GP3')
vin = tk.StringVar()
vin.set('LJDDAA22170202423')

# table

frm_car = tk.Frame(frm_r, height=80, width=195, bg='black', bd=1.5)
frm_car.place(x=2, y=15)
frm_car_1 = tk.Frame(frm_car, height=45, width=195, bg='white', bd=0)  # set width and height in this line
frm_car_1.pack()
e_car = tk.Entry(frm_car_1, textvariable=car, font=('Arial', 22, 'bold'),
                 width=10, foreground='#00BFFF', bd=0,
                 validate="key", validatecommand=(limit_len_1, '%P', 10))
e_car.place(x=1, y=1)

frm_ocn = tk.Frame(frm_r, height=80, width=195, bg='black', bd=1.5)
frm_ocn.place(x=2, y=60)
frm_ocn_1 = tk.Frame(frm_ocn, height=45, width=195, bg='white', bd=0)
frm_ocn_1.pack()
l_ocn = tk.Label(frm_ocn_1, text='O.C.N:', font=('Arial', '9', 'bold'), bg='white')
l_ocn.place(x=2, y=1)
if ocn_lock:
    e_ocn = tk.Entry(frm_ocn_1, state='disable', textvariable=ocn, font=('Arial', 15, 'bold'),
                     width=5, foreground='black', bd=0)
else:
    e_ocn = tk.Entry(frm_ocn_1, textvariable=ocn, font=('Arial', 15, 'bold'),
                     width=5, foreground='#00BFFF', validate="key",
                     bd=0, validatecommand=(limit_len_1, '%P', 4))
e_ocn.place(x=20, y=19)

frm_bd = tk.Frame(frm_r, height=80, width=195, bg='black', bd=1.5)
frm_bd.place(x=2, y=105)
frm_bd_1 = tk.Frame(frm_bd, height=60, width=195, bg='white', bd=0)
frm_bd_1.pack()
l_bd = tk.Label(frm_bd_1, text='BODY NO:', font=('Arial', '9', 'bold'), bg='white')
l_bd.place(x=2, y=1)
e_bodyno = tk.Entry(frm_bd_1, textvariable=bodyno, font=('Arial', 24, 'bold'),
                    width=10, foreground='#00BFFF', bd=0,
                    validate="key", validatecommand=(limit_len_1, '%P', 10))
e_bodyno.place(x=10, y=20)

frm_order = tk.Frame(frm_r, height=80, width=195, bg='black', bd=1.5)
frm_order.place(x=2, y=165)
frm_order_1 = tk.Frame(frm_order, height=120, width=195, bg='white', bd=0)
frm_order_1.pack()
l_od = tk.Label(frm_order_1, text='ORDER:', font=('Arial', '9', 'bold'), bg='white')
l_od.place(x=2, y=1)
e_order = tk.Entry(frm_order_1, textvariable=order, font=('Arial', 24, 'bold'),
                   width=10, foreground='#00BFFF', bd=0,
                   validate="key", validatecommand=(update_ocn_1, '%P'))
# e_order.bind('<Key>',update_ocn)
e_order.place(x=10, y=20)
l_na = tk.Label(frm_order_1, text='NATION:', font=('Arial', '9', 'bold'), bg='white')
l_na.place(x=2, y=60)
l_inclr = tk.Label(frm_order_1, text='IN-CLR', font=('Arial', '9', 'bold'), bg='white')
l_inclr.place(x=80, y=60)
l_outclr = tk.Label(frm_order_1, text='OUT-CLR', font=('Arial', '9', 'bold'), bg='white')
l_outclr.place(x=130, y=60)
e_nation = tk.Entry(frm_order_1, textvariable=nation, font=('Arial', 18,),
                    width=10, foreground='#00BFFF', bd=0,
                    validate="key", validatecommand=(limit_len_1, '%P', 5))
e_nation.place(x=4, y=80)

e_inclr = tk.Entry(frm_order_1, textvariable=inclr, font=('Arial', 18),
                   width=3, foreground='#00BFFF', bd=0,
                   validate="key", validatecommand=(limit_len_1, '%P', 2))
e_inclr.place(x=90, y=80)
e_outclr = tk.Entry(frm_order_1, textvariable=outclr, font=('Arial', 18,),
                    width=3, foreground='#00BFFF', bd=0,
                    validate="key", validatecommand=(limit_len_1, '%P', 2))
e_outclr.place(x=140, y=80)

frm_spec = tk.Frame(frm_r, height=80, width=195, bg='black', bd=1.5)
frm_spec.place(x=2, y=285)
frm_spec_1 = tk.Frame(frm_spec, height=128, width=195, bg='white', bd=0)
frm_spec_1.pack()
l_spec = tk.Label(frm_spec_1, text='SPEC:', font=('Arial', '9', 'bold'), bg='white')
l_spec.place(x=2, y=1)
l_ocn_2 = tk.Label(frm_spec_1, text='O.C.N:', font=('Arial', '9', 'bold'), bg='white')
l_ocn_2.place(x=140, y=1)
l_vin = tk.Label(frm_spec_1, text='VIN:', font=('Arial', '9', 'bold'), bg='white')
l_vin.place(x=2, y=65)
e_spec = tk.Entry(frm_spec_1, textvariable=spec, font=('Browallia New', 22, 'bold'),
                  width=15, foreground='#00BFFF', bd=0,
                  validate="key", validatecommand=(limit_len_1, '%P', 10))
e_spec.place(x=10, y=20)
if ocn_lock:
    e_ocn_2 = tk.Entry(frm_spec_1, state='disabled', textvariable=ocn, font=('Browallia New', 22, 'bold'),
                       width=5, foreground='black', bd=0)
else:
    e_ocn_2 = tk.Entry(frm_spec_1, textvariable=ocn, font=('Browallia New', 22, 'bold'),
                       width=5, foreground='#00BFFF', bd=0,
                       validate="key", validatecommand=(limit_len_1, '%P', 4))
e_ocn_2.place(x=145, y=20)
e_vin = tk.Entry(frm_spec_1, textvariable=vin, font=('Browallia New', 20, 'bold'),
                 width=20, foreground='#00BFFF', bd=0,
                 validate="key", validatecommand=(limit_len_1, '%P', 17))
e_vin.place(x=5, y=90)

frm_last = tk.Frame(frm_r, height=80, width=195, bg='black', bd=1.5)
frm_last.place(x=2, y=413)
frm_last_1 = tk.Frame(frm_last, height=28, width=195, bg='white', bd=0)
frm_last_1.pack()
l_made_info = tk.Label(frm_last_1, text='MADE IN CHINA', font=('Arial', '12', 'bold'), bg='white')
l_made_info.place(x=30, y=4)


# define functions
def format_data(data):
    data_t = [data['barcode'], data['vin'], data['spec'],
              data['ocn'], data['nation'], data['inclr'],
              data['outclr'], data['order'],
              data['bodyno'], data['ocn'], data['car']]
    return data_t


def open_config():
    data = collect_data()
    data_t = format_data(data)
    window_config = tk.Toplevel(window)
    window_config.geometry('400x450')
    window_config.title('CONFIG')
    window_config.resizable(False, False)
    frm_c_1 = tk.Frame(window_config, bd=1.5)
    frm_c_1.pack(fill='x')
    # lf_ip_port = tk.LabelFrame(frm_1, height=80, width=195, bd=1.5)
    # lf_ip_port.pack()
    l_ip_address = tk.Label(frm_c_1, text='IP ADDRESS', width='15', relief='ridge',
                            font=('Arial', '12', 'bold'), fg='white', bg='#00BFFF')
    l_ip_address.grid(row=0, column=0)
    ip = tk.StringVar()
    ip.set(main_data['ip'])
    e_ip = tk.Entry(frm_c_1, textvariable=ip, width=30)
    e_ip.grid(row=0, column=1)
    l_ip_address = tk.Label(frm_c_1, text='PORT NO', width='15', relief='ridge',
                            font=('Arial', '12', 'bold'), fg='white', bg='#00BFFF')
    l_ip_address.grid(row=1, column=0)
    port = tk.StringVar()
    port.set(main_data['port'])
    e_port = tk.Entry(frm_c_1, textvariable=port, width=30)
    e_port.grid(row=1, column=1, padx=6)  # padx 设置边距

    frm_c_2 = tk.Frame(window_config, bd=1.5)
    frm_c_2.pack()
    t_config = tk.Text(frm_c_2, font=('Arial', '9', 'bold'))
    t_config.pack()
    t_config.insert('1.0', config.format(data_t))
    frm_c_3 = tk.Frame(window_config, bd=1.5)
    frm_c_3.pack(side='top', fill='x', expand=1)

    def close_config():
        window_config.destroy()

    def getsig(contents):
        m = hashlib.md5(contents.encode())
        return m.digest()

    config_1 = t_config.get('1.0', 'end')
    sig = getsig(config_1)

    def save_config():
        content = t_config.get('1.0', 'end')
        main_data['ip'] = e_ip.get()
        main_data['port'] = e_port.get()
        if sig != getsig(content):
            with open('print_new.config', 'w') as f:
                f.write(content)
        else:
            pass
    b_c_close = tk.Button(frm_c_3, text='CLOSE', command=close_config)
    b_c_close.pack(side='right')
    b_save = tk.Button(frm_c_3, text='SAVE', command=save_config)
    b_save.pack(side='right')


def collect_data():
    main_data['car'] = car.get()
    main_data['barcode'] = bodyno.get()
    main_data['vin'] = vin.get()
    main_data['spec'] = spec.get()
    main_data['nation'] = nation.get()
    main_data['inclr'] = inclr.get()
    main_data['outclr'] = outclr.get()
    main_data['order'] = order.get()
    main_data['bodyno'] = bodyno.get()
    global ocn_lock
    if ocn_lock:
        main_data['ocn'] = main_data['order'][5:]
    else:
        main_data['ocn'] = ocn.get()
    return main_data


def log(data):
    with open('log.son', 'a') as l:
        dt = datetime.datetime.now()
        dt = dt.strftime('%x-%X')
        logdata = []
        logdata.append({'time': dt})
        tmp = {'data': [data['car'], data['bodyno'], data['order'],
              data['ocn'], data['nation'], data['inclr'],
              data['outclr'], data['spec'],
              data['vin'], data['ip'], data['port']]}
        logdata.append(tmp)
        json.dump(logdata, l)
        l.write('\n')


def data_printer(data=main_data):
    # connect printer and print barcode
    ip = main_data['ip']
    port = main_data['port']
    data_t = format_data(data)
    send_data = config.format(data_t).encode('ascii')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, int(port)))
            s.sendall(send_data)
            recv = s.recv(1024)
            mess = 'print success!1' + recv
            return mess
        except:
            mess = 'connect failed!'
            return mess


def print_barcode():
    data = collect_data()
    log(data)
    global info
    # mess = data_printer(data)
    # info.set('    info  : ' + mess)


def close_window():
    window.destroy()


# def show_barcode():
#     ean = barcode.get('code128', e_bodyno.get(), writer=ImageWriter())
#     img = ean.save('')


def ocn_locker():
    global ocn_lock
    if ocn_lock:
        ocn_lock = False
        b_ocn['text'] = 'ocn unlock'
        e_ocn['state'] = 'normal'
        e_ocn['foreground'] = '#00BFFF'
        e_ocn_2['state'] = 'normal'
        e_ocn_2['foreground'] = '#00BFFF'
    else:
        # global ocn_lock
        ocn_lock = True
        b_ocn['text'] = 'ocn locked'
        e_ocn['state'] = 'disabled'
        e_ocn['foreground'] = 'black'
        e_ocn_2['state'] = 'disabled'
        e_ocn_2['foreground'] = 'black'


# Buttons
b_config = tk.Button(frm_2, text='CONFIG', font=('Arial', '10'), height=1, width=10, command=open_config)
b_config.place(x=5, y=5)
b_ocn = tk.Button(frm_2, text='ocn locked', font=('Arial', '10'), height=1, width=9, command=ocn_locker)
b_ocn.place(x=100, y=5)
# b_config.pack(side="left")
b_print = tk.Button(frm_2, text='PRINT', height=1, width=10, command=print_barcode)
b_print.place(x=220, y=5)
b_close = tk.Button(frm_2, text='CLOSE', height=1, width=10, command=close_window)
b_close.place(x=305, y=5)

# show status
img_icon1 = tk.PhotoImage(file="info.gif")
l_img_icon_1 = tk.Label(frm_3, width=15, height=15, anchor='w')
l_img_icon_1["image"] = img_icon1
l_img_icon_1.place(x=5, y=4)
info = tk.StringVar()
info.set('   info :  ....')
l_info = tk.Label(frm_3, textvariable=info, height=1, width=45, anchor='w')
l_info.place(x=40, y=4)

# print(e_car.get())
# print(car.get())
window.mainloop()
