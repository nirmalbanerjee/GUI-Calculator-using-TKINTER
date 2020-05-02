from tkinter import *
from tkinter import ttk
import math
import tkinter
import tkinter.messagebox


root= Tk()  #top parent
root.title('operationsOnNumbers')
root.resizable(0,0)
color = '#004d80'
root.configure(bg=color)
root.iconbitmap(r"\icon.ico") #enter your own path

#===================================================================================
#                                     STYLE
#===================================================================================
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 400) #progress bar top
progressbar.pack(fill = X, expand = 1)
progressbar.config(mode = 'indeterminate')
progressbar.start()

progressbar = ttk.Progressbar(root, orient = VERTICAL, length = 300) #progress bar left
progressbar.pack(side=LEFT)
progressbar.config(mode = 'indeterminate')
progressbar.start()

progressbar = ttk.Progressbar(root, orient = VERTICAL, length = 300) #progress bar right
progressbar.pack(side=RIGHT)
progressbar.config(mode = 'indeterminate')
progressbar.start()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 400) #progress bar bottom
progressbar.pack(side=BOTTOM)
progressbar.config(mode = 'indeterminate')
progressbar.start()

ttk.Style().configure("TButton", background="#ff3333") #Button style (applied to both the tabs)
ttk.Style().configure("TLabel", background="#ffff80") #Label style (applied to both the tabs)

#===================================================================================
#                                LABEL_FRAME/NOTEBOOK/TABS
#===================================================================================
topframe = ttk.LabelFrame(root, text=' On how many numbers do you want to perform the operation ?')
topframe.pack(expand=1)
tabControl = ttk.Notebook(topframe)          
tabControl.pack(expand=1, fill="both")

tab1 = ttk.Frame(tabControl)           
tabControl.add(tab1, text='1 number') 
tab2 = ttk.Frame(tabControl)           
tabControl.add(tab2, text='2 numbers')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='     Info     ')

text = Text(tab3, width = 40, height = 10, wrap=WORD, background = '#ffd699')
text.pack()
image = PhotoImage(file = r'\info.png').subsample(3,3) #enter your own path
text.image_create('insert', image = image)
text.insert('1.0 + 2 lines lineend', '\nThis GUI app is developed by Nirmal Banerjee.\nGithub: https://github.com/nirmalbanerjee \nLinkedIn: https://www.linkedin.com/in/nirmalbanerjee/')
text.config(state=DISABLED)

#=================================================================================
#                                      TAB 1
#=================================================================================

single_number_frame = ttk.LabelFrame(tab1, text=' Operation on Single Number ')
single_number_frame.pack()

# ==================================================Variables=======================

number = StringVar()
ans = StringVar()

# ==================================================Frames==========================

top_first = Frame(single_number_frame, width=800, height=80)
top_first.pack()
top_second = Frame(single_number_frame,  width=800, height=80)
top_second.pack()
top_third = Frame(single_number_frame, width=800, height=80)
top_third.pack()
top_fourth = Frame(single_number_frame, width=800, height=80)
top_fourth.pack()

# ==================================================Functions=======================

def errorMsg(msg): #error message
    if msg == 'error':
        tkinter.messagebox.showerror('A Friendly Message :)', 'Something went wrong :( \n Check the Input !!')

def square(): #SQUARE
    try:
        value = math.pow(float(number.get()),2)
        ans.set(value)
    except:
        errorMsg('error')

def sq_rt(): #SQUARE_ROOT
    try:
        value = math.sqrt(float(number.get()))
        ans.set(value)

    except:
         errorMsg('error')

def cube(): #CUBE
    try:
        value = math.pow(float(number.get()),3)
        ans.set(value)
    except:
        errorMsg('error')

def log10(): #LOGARITHM
    try:
        value = math.log10(float(number.get()))
        ans.set(value)
    except:
        errorMsg('error')

def factorial(): #FACTORIAL
    try:
        value = math.factorial(float(number.get()))
        ans.set(value)
    except:
        errorMsg('error')

def cos(): #COSINE
    try:
        value = math.cos(float(number.get()))
        ans.set(value)
    except:
        errorMsg('error')

def sine(): #SINE
    try:
        value = math.sin(float(number.get()))
        ans.set(value)
    except:
        errorMsg('error')

def tan(): #TANGENT
    try:
        value = math.tan(float(number.get()))
        ans.set(value)
    except:
        errorMsg('error')

# ==================================================Button=================

btn_add = ttk.Button(top_second, text="Square", width=8, command=square)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_second, text="Sq. Root", width=8, command=sq_rt)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_second, text="Cube", width=8, command=cube)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_second, text="Log 10", width=8, command=log10)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_second, text="Factorial", width=8, command=factorial)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_third, text="Cosine", width=8, command=cos)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_third, text="Sine", width=8, command=sine)
btn_add.pack(side=LEFT,  padx=5, pady=5)

btn_add = ttk.Button(top_third, text="Tangent", width=8, command=tan)
btn_add.pack(side=LEFT,  padx=5, pady=5)

# ==================================================Entry+Labels================

label_input = ttk.Label(top_first, text = 'Enter the number: ')
label_input.pack(side=LEFT, padx=10, pady=10)
input_number = ttk.Entry(top_first, textvariable=number)
input_number.pack(side=LEFT)

label_output = ttk.Label(top_fourth, text = 'Result: ')
label_output.pack(side=LEFT, padx=10, pady=10)
output = ttk.Entry(top_fourth, textvariable=ans)
output.pack(side=LEFT)


#===================================================================================
#                                       TAB 2
#===================================================================================
two_numbers_frame = ttk.LabelFrame(tab2, text=' Operations on Two Numbers ')
two_numbers_frame.pack()

# ==================================================Variables=======================

num1 = StringVar()
num2 = StringVar()
res = StringVar()

# ==================================================Frames==========================
top_first = Frame(two_numbers_frame, width=800, height=80)
top_first.pack()
top_second = Frame(two_numbers_frame,  width=800, height=80)
top_second.pack()
top_third = Frame(two_numbers_frame, width=800, height=80)
top_third.pack()
top_fourth = Frame(two_numbers_frame, width=800, height=80)
top_fourth.pack()
top_fifth = Frame(two_numbers_frame, width=800, height=80)
top_fifth.pack()

# ==================================================Functions=======================


def errorMsg(msg): #error Message
    if msg == 'error':
        tkinter.messagebox.showerror('A Friendly Message :)', 'Something went wrong :( \n Check the Inputs !!')
    elif msg == 'divisionerror':
        tkinter.messagebox.showerror(' Cannot divide by 0 -_-')


def addition(): #ADDITION
    try:
        value = float(num1.get()) + float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def substraction(): #SUBSTRACTION
    try:
        value = float(num1.get()) - float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def multiplication(): #MULTIPLICATION
    try:
        value = float(num1.get()) * float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def division(): #DIVISION
    
    if num2.get() == '0':
        errorMsg('divisionerror')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res.set(value)
        except:
            errorMsg('error')

def power(): #POWER
    try:
        value = math.pow(float(num1.get()),float(num2.get()))
        res.set(value)
    except:
        errorMsg('error')

def permutation(): #PERMUTATION
    try:
        value = math.perm(float(num1.get()),float(num2.get()))
        res.set(value)
    except:
        errorMsg('error')

def combination(): #COMBINATION
    try:
        value = math.comb(float(num1.get()),float(num2.get()))
        res.set(value)
    except:
        errorMsg('error')
# ==================================================Button=================


btn_plus = ttk.Button(top_third, text="Add", width=8, command=addition)
btn_plus.pack(side=LEFT,  padx=5, pady=5)

btn_minus = ttk.Button(top_third, text="Substract", width=8, command=substraction)
btn_minus.pack(side=LEFT,  padx=5, pady=5)

btn_mul = ttk.Button(top_third, text="Multiply", width=8, command=multiplication)
btn_mul.pack(side=LEFT,  padx=5, pady=5)

btn_div = ttk.Button(top_third, text="Divide", width=8, command=division)
btn_div.pack(side=LEFT,  padx=5, pady=5)

btn_div = ttk.Button(top_fourth, text=" A^B(Power) ", width=12, command=power)
btn_div.pack(side=LEFT,  padx=5, pady=5)

btn_div = ttk.Button(top_fourth, text="Perm (A,B)", width=12, command=permutation)
btn_div.pack(side=LEFT,  padx=5, pady=5)

btn_div = ttk.Button(top_fourth, text="Comb (A,B)", width=12, command=combination)
btn_div.pack(side=LEFT,  padx=5, pady=5)
# ==================================================Entry+Labels================


label_first_num = ttk.Label(top_first, text="Enter Number A :")
label_first_num.pack(side=LEFT, padx=10, pady=10)
first_num = ttk.Entry(top_first, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = ttk.Label(top_second, text="Enter Number B :")
label_second_num.pack(side=LEFT, padx=10, pady=10)
second_num = ttk.Entry(top_second, textvariable=num2)
second_num.pack(side=LEFT)


label_third_num = ttk.Label(top_fifth, text="Result :")
label_third_num.pack(side=LEFT, padx=5, pady=5)
result = ttk.Entry(top_fifth, textvariable=res)
result.pack(side=LEFT)


root.mainloop()