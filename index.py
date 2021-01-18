import subprocess
import tkinter as tk
from tkinter import StringVar

output = subprocess.check_output('cmd /c "netsh int ipv4 show glob"')

if b'128' in output:
    value = 'TTL HACK IS DISABLE'

if b'65' in output:
    value = 'TTL HACK IS ENABLE'
    
def ttlhackon ():
    output = subprocess.check_output('cmd /c "netsh int ipv4 set glob defaultcurhoplimit=65"')
    print(output)
    updatettlstatus()
    
def ttlhackoff ():
    output = subprocess.check_output('cmd /c "netsh int ipv4 set glob defaultcurhoplimit=128"')
    print(output)
    updatettlstatus()

def updatettlstatus():
    output = subprocess.check_output('cmd /c "netsh int ipv4 show glob"')

    if b'128' in output:
        var.set('TTL HACK IS DISABLE')

    if b'65' in output:
        var.set('TTL HACK IS ENABLE')
    
root = tk.Tk()
root.resizable(False, False)
root.title('TTL HACK')
var = StringVar()
var.set(value)

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = '#2C2F33', relief = 'raised')
canvas1.pack()
message = tk.Label(textvariable=var, bg='#7289DA', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 80, window=message)

button1 = tk.Button(text=' TTL HACK ON ', command=ttlhackon, bg='#7289DA', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 120, window=button1)
button2 = tk.Button(text=' TTL HACK OFF ', command=ttlhackoff, bg='#7289DA', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 160, window=button2)
root.mainloop()
//penisman
