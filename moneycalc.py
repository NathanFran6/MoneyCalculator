import tkinter as tk

win = tk.Tk()
win.title('Money Use Calculator')


win.geometry('750x350')

title = tk.Label(win, text ='Money Use Calculator', font=('Arial', 25))
title.pack()
brake  = tk.Label(win, text ='', font=('Arial', 40))
brake.pack()
prompt = tk.Label(win, text ='Enter Last 2 Weeks Pay:', font=('Arial', 10))
prompt.pack()
def display_money():
    global entry 
    money = entry.get()
    save = int(money)*.80

    spend= int(money)*.15 

    give= int(money)*.05 

    display = ('Save: $'+ str(save),'Spend: $' + str(spend), 'Give: $' + str(give))
    label.configure(text=display, width =50)

entry = tk.Entry(fg='black', bg='white', width=20, font= ('Arial', 25))
entry.pack()

button = tk.Button(text='Calulate', font=('Arial', 15), height= 3, width =15, command = display_money).pack()

label = tk.Label(win, text='', font =('Arial', 25))
label.pack()

win.mainloop()