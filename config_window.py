import tkinter as tk
import hashlib
from network import main_data

config = ''
with open('print.config','r') as f:
    for line in f.readlines():
        config += line

window_config = tk.Tk()
window_config.geometry('400x450')
window_config.title('CONFIG')
window_config.resizable(False,False)
frm_1 = tk.Frame(window_config, bd=1.5)
frm_1.pack(fill='x')
# lf_ip_port = tk.LabelFrame(frm_1, height=80, width=195, bd=1.5)
# lf_ip_port.pack()
l_ip_address = tk.Label(frm_1, text='IP ADDRESS',width='15', relief='ridge',
                        font=('Arial', '12', 'bold'), fg='white', bg='#00BFFF')
l_ip_address.grid(row=0,column=0)
ip = tk.StringVar()
ip.set(main_data['ip'])
e_ip = tk.Entry(frm_1, textvariable=ip, width=30).grid(row=0,column=1)
l_ip_address = tk.Label(frm_1, text='PORT NO',width='15', relief='ridge',
                        font=('Arial', '12', 'bold'), fg='white', bg='#00BFFF')
l_ip_address.grid(row=1,column=0)
port = tk.StringVar()
port.set(main_data['port'])
e_port = tk.Entry(frm_1,  textvariable=port, width=30).grid(row=1,column=1,padx=6) # padx 设置边距

frm_2 = tk.Frame(window_config, bd=1.5)
frm_2.pack()
t_config = tk.Text(frm_2, font=('Arial','9','bold'))
t_config.pack()
t_config.insert('1.0', config)
frm_3= tk.Frame(window_config, bd=1.5)
frm_3.pack(side='top', fill='x', expand=1)

def close_window():
    window_config.destroy()

def getSig(contents):
    m=hashlib.md5(contents.encode())
    return m.digest()
config_1 = t_config.get('1.0','end')
sig = getSig(config_1)
def save_config():
    content = t_config.get('1.0','end')
    if sig != getSig(content):
        with open('print_new.config','w') as f:
            f.write(content)
        # print('changed')
    else:
        pass
        # print('good')

b_close = tk.Button(frm_3, text='CLOSE', command=close_window)
b_close.pack(side='right')
b_save = tk.Button(frm_3, text='SAVE', command=save_config)
b_save.pack(side='right')

# labelframe = tk.LabelFrame(window_config, text="This is a LabelFrame")
# labelframe.pack(fill="both", expand="yes")
# left = tk.Label(labelframe, text="Inside the LabelFrame")
# left.pack()
window_config.mainloop()