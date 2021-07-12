import tkinter as tk
import math
import sys


def add_digit(digit):
    value = calc.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_dot(dot):
    value = calc.get()
    if value[-1]=='.':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value+dot)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*%':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)

def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value +value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,eval(value))

def dl():
    value = calc.get()
    value=value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value)
    if len(value) == 0:
        calc.delete(0,tk.END)
        calc.insert(0,'0')

def ln():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.log(float(value)))

def cos():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.cos(math.radians(float(value))))

def sin():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.sin(math.radians(float(value))))

def tan():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.tan(math.radians(float(value))))

def ctg():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,1/math.tan(math.radians(float(value))))

def log():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,math.log10(float(value)))

def percent():
    value = calc.get()
    if '*' in value:
        calc.delete(0,tk.END)
        calc.insert(0,eval(value+'/100'))
    elif '/' in value:
        calc.delete(0,tk.END)
        calc.insert(0,eval(value)*100)
    elif '+' in value:
        sr=''
        for i in range(len(value)):
            if value[i]!='+' and value[i]!='-':
                sr=sr+value[i]
            else:
                break
        calc.delete(0,tk.END)
        calc.insert(0,eval(value+'/100*'+sr))
    elif '-' in value:
        sr=''
        for i in range(len(value)):
            if value[i]!='+' and value[i]!='-':
                sr=sr+value[i]
            else:
                break
        calc.delete(0,tk.END)
        calc.insert(0,eval(value+'/100*'+sr))
    else:
        calc.delete(0,tk.END)
        calc.insert(0,'0')

def binnary():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,bin(int(value)))




def clear():
    calc.delete(0,tk.END)
    calc.insert(0,'0')

def make_dot_button(dot):
    return tk.Button(text=dot, bd=5,font=('Arial', 13), command=lambda : add_dot(dot))

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5,font=('Arial', 13), command=lambda : add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=lambda : add_operation(operation))

def make_del_button(delete):
    return tk.Button(text=delete, bd=5,font=('Arial', 13), command=dl)

def make_calc_button(calc):
    return tk.Button(text=calc, bd=5,font=('Arial', 13), command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=clear)

def make_ln_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=ln)

def make_cos_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=cos)

def make_sin_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=sin)

def make_tan_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=tan)

def make_ctg_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=ctg)

def make_log_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=log)

def make_percent_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=percent)

def make_binnary_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=binnary)

win = tk.Tk()
win.geometry(f"325x315+100+200")
win.title("Calculator")

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0,column=0,columnspan=6, stick='we', padx=5)

make_digit_button('1').grid(row=1,column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1,column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1,column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2,column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2,column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2,column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3,column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3,column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3,column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4,column=0, stick='wens', padx=5, pady=5)

make_dot_button('.').grid(row=1,column=5, stick='wens', padx=5, pady=5)


make_operation_button('+').grid(row=1,column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2,column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3,column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4,column=3, stick='wens', padx=5, pady=5)

make_del_button('del').grid(row=1,column=4, stick='wens', padx=5, pady=5)

make_cos_button('cos').grid(row=5,column=0, stick='wens', padx=5, pady=5)
make_sin_button('sin').grid(row=5,column=1, stick='wens', padx=5, pady=5)
make_tan_button('tan').grid(row=5,column=2, stick='wens', padx=5, pady=5)
make_ctg_button('ctg').grid(row=5,column=3, stick='wens', padx=5, pady=5)
make_log_button('log').grid(row=5,column=4, stick='wens', padx=5, pady=5)
make_ln_button('ln').grid(row=4,column=4, stick='wens', padx=5, pady=5)
make_percent_button('%').grid(row=3,column=4, stick='wens', padx=5, pady=5)
make_binnary_button('bin').grid(row=2,column=4, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4,column=2, stick='wens', padx=5, pady=5)


make_clear_button('c').grid(row=4,column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.mainloop()
