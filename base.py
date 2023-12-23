import tkinter as tk
import pickle
from tkinter import *
import customtkinter
from tkinter import messagebox as ms, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def out():
    base.destroy()
class NewWindow:
    def __init__(self):
        self.c1 = PhotoImage(file='picture/z1.png')
        self.c2 = PhotoImage(file='picture/z2.png')
        self.load_counts()  # Загружаем значения счетчиков
        self.new_window = tk.Toplevel(base)
        self.new_window.title("Покупка")
        self.new_window.geometry('250x200+0+0')
        self.new_window.resizable(width=False, height=False)
        self.new_window.configure(bg='pink')

        self.button1 = customtkinter.CTkButton(self.new_window, height=100, width=100, text="",  bg_color='#FFC0CB', fg_color='#7C5322', hover_color="#533818", image=self.c1, command=self.button1_click)
        self.button1.grid(row=0, column=0)

        self.button2 = customtkinter.CTkButton(self.new_window, height=100, width=100, text="", bg_color='#FFC0CB', fg_color='#D5923F', hover_color="#A26C2A", image=self.c2, command=self.button2_click)
        self.button2.grid(row=0, column=1)

        # self.button3 = customtkinter.CTkButton(self.new_window, height=100, width=100, text="", bg_color='#FFC0CB',
        #                                        fg_color='#7C5322', hover_color="#533818", image=self.c1,
        #                                        command=self.button3_click)
        # self.button3.grid(row=0, column=0)
        #
        # self.button4 = customtkinter.CTkButton(self.new_window, height=100, width=100, text="", bg_color='#FFC0CB',
        #                                        fg_color='#D5923F', hover_color="#A26C2A", image=self.c2,
        #                                        command=self.button4_click)
        # self.button4.grid(row=0, column=1)

        # Обновляем метки с текущими значениями счетчиков
        self.update_labels()

    def load_counts(self):
        try:
            # Пытаемся загрузить значения счетчиков из файла "counts.pickle"
            with open("counts.pickle", "rb") as f:
                self.count1, self.count2 = pickle.load(f)
        except FileNotFoundError:
            # Если файл не найден, устанавливаем значения счетчиков в 0
            self.count1 = 0
            self.count2 = 0

    def save_counts(self):
        # Сохраняем значения счетчиков в файл "counts.pickle"
        with open("counts.pickle", "wb") as f:
            pickle.dump((self.count1, self.count2), f)

    def update_labels(self):
        # Обновляем метки с текущими значениями счетчиков
        label1.config(text="Bitcoin: {} ".format(self.count1))
        label2.config(text="Ethereum: {} ".format(self.count2))

    def button1_click(self):
        self.count1 += 1
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки

    def button2_click(self):
        self.count2 += 1
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки

class NewWindow2:
    def __init__(self):
        self.c3 = PhotoImage(file='picture/z3.png')
        self.c4 = PhotoImage(file='picture/z4.png')
        self.load_counts()  # Загружаем значения счетчиков
        self.new_window2 = tk.Toplevel(base)
        self.new_window2.title("Покупка")
        self.new_window2.geometry('250x200+225+0')
        self.new_window2.attributes("-topmost",True)
        self.new_window2.resizable(width=False, height=False)
        self.new_window2.configure(bg='pink')


        self.button1 = customtkinter.CTkButton(self.new_window2, height=100, width=100, text="",  bg_color='#FFC0CB', fg_color='#D53FA4', hover_color="#A6267F", image=self.c3, command=self.button1_click)
        self.button1.grid(row=0, column=0)

        self.button2 = customtkinter.CTkButton(self.new_window2, height=100, width=100, text="", bg_color='#FFC0CB', fg_color='#EA488A', hover_color="#D4216A", image=self.c4, command=self.button2_click)
        self.button2.grid(row=0, column=1)

        # Обновляем метки с текущими значениями счетчиков
        self.update_labels()

    def load_counts(self):
        try:
            # Пытаемся загрузить значения счетчиков из файла "counts.pickle"
            with open("counts2.pickle", "rb") as f:
                self.count3, self.count4 = pickle.load(f)
        except FileNotFoundError:
            # Если файл не найден, устанавливаем значения счетчиков в 0
            self.count3 = 0
            self.count4 = 0

    def save_counts(self):
        # Сохраняем значения счетчиков в файл "counts.pickle"
        with open("counts2.pickle", "wb") as f:
            pickle.dump((self.count3, self.count4), f)

    def update_labels(self):
        # Обновляем метки с текущими значениями счетчиков
        label3.config(text="Tether: {} ".format(self.count3))
        label4.config(text="Binance Coin: {} ".format(self.count4))

    def button1_click(self):
        self.count3 += 1
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки

    def button2_click(self):
        self.count4 += 1
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки


class NewWindow3:
    def __init__(self):
        self.c1 = PhotoImage(file='picture/z1.png')
        self.c2 = PhotoImage(file='picture/z2.png')
        self.load_counts()  # Загружаем значения счетчиков
        self.new_window3 = tk.Toplevel(base)
        self.new_window3.title("Продажа")
        self.new_window3.geometry('250x200+0+0')
        self.new_window3.resizable(width=False, height=False)
        self.new_window3.configure(bg='pink')

        self.button1 = customtkinter.CTkButton(self.new_window3, height=100, width=100, text="",  bg_color='#FFC0CB', fg_color='#7C5322', hover_color="#533818", image=self.c1, command=self.button1_click)
        self.button1.grid(row=0, column=0)

        self.button2 = customtkinter.CTkButton(self.new_window3, height=100, width=100, text="", bg_color='#FFC0CB', fg_color='#D5923F', hover_color="#A26C2A", image=self.c2, command=self.button2_click)
        self.button2.grid(row=0, column=1)


        # Обновляем метки с текущими значениями счетчиков
        self.update_labels()

    def load_counts(self):
        try:
            # Пытаемся загрузить значения счетчиков из файла "counts.pickle"
            with open("counts.pickle", "rb") as f:
                self.count1, self.count2 = pickle.load(f)
        except FileNotFoundError:
            # Если файл не найден, устанавливаем значения счетчиков в 0
            self.count1 = 0
            self.count2 = 0

    def save_counts(self):
        # Сохраняем значения счетчиков в файл "counts.pickle"
        with open("counts.pickle", "wb") as f:
            pickle.dump((self.count1, self.count2), f)

    def update_labels(self):
        # Обновляем метки с текущими значениями счетчиков
        label1.config(text="Bitcoin: {} ".format(self.count1))
        label2.config(text="Ethereum: {} ".format(self.count2))

    def button1_click(self):
        if (self.count1 >= 1):
            self.count1 -= 1
        else:
            ms.showinfo('Вы бомж')
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки

    def button2_click(self):
        if (self.count2 >= 1):
            self.count2 -= 1
        else:
            ms.showinfo('Вы бомж')
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки

class NewWindow4:
    def __init__(self):
        self.c3 = PhotoImage(file='picture/z3.png')
        self.c4 = PhotoImage(file='picture/z4.png')
        self.load_counts()  # Загружаем значения счетчиков
        self.new_window4 = tk.Toplevel(base)
        self.new_window4.title("Продажа")
        self.new_window4.geometry('250x200+0+225')
        self.new_window4.attributes("-topmost",True)
        self.new_window4.resizable(width=False, height=False)
        self.new_window4.configure(bg='pink')


        self.button1 = customtkinter.CTkButton(self.new_window4, height=100, width=100, text="",  bg_color='#FFC0CB', fg_color='#D53FA4', hover_color="#A6267F", image=self.c3, command=self.button1_click)
        self.button1.grid(row=0, column=0)

        self.button2 = customtkinter.CTkButton(self.new_window4, height=100, width=100, text="", bg_color='#FFC0CB', fg_color='#EA488A', hover_color="#D4216A", image=self.c4, command=self.button2_click)
        self.button2.grid(row=0, column=1)

        # Обновляем метки с текущими значениями счетчиков
        self.update_labels()

    def load_counts(self):
        try:
            # Пытаемся загрузить значения счетчиков из файла "counts.pickle"
            with open("counts2.pickle", "rb") as f:
                self.count3, self.count4 = pickle.load(f)
        except FileNotFoundError:
            # Если файл не найден, устанавливаем значения счетчиков в 0
            self.count3 = 0
            self.count4 = 0

    def save_counts(self):
        # Сохраняем значения счетчиков в файл "counts.pickle"
        with open("counts2.pickle", "wb") as f:
            pickle.dump((self.count3, self.count4), f)

    def update_labels(self):
        # Обновляем метки с текущими значениями счетчиков
        label3.config(text="Tether: {} ".format(self.count3))
        label4.config(text="Binance Coin: {} ".format(self.count4))

    def button1_click(self):
        if (self.count3 >= 1):
            self.count3 -= 1
        else:
            ms.showinfo('Вы бомж')
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки

    def button2_click(self):
        if (self.count4 >= 1):
            self.count4 -= 1
        else:
            ms.showinfo('Вы бомж')
        self.update_labels()
        self.save_counts()  # Сохраняем значения после каждого нажатия кнопки



base = tk.Tk()
base.geometry('1200x800')
base.title('CryptoCake')
base.resizable(width=False, height=False)

c1 = PhotoImage(file='picture/z1.png')
c2 = PhotoImage(file='picture/z2.png')
c3 = PhotoImage(file='picture/z3.png')
c4 = PhotoImage(file='picture/z4.png')

bac = PhotoImage(file='picture/92.png')
baac = PhotoImage(file='picture/91.png')

header = customtkinter.CTkFrame(base, height=60, width=1200, fg_color='pink')
header.grid(row=0, column=0)

title = customtkinter.CTkLabel(header, height=38, width=170, bg_color='#FF86AA', text_color='white', text='CryptoCake', font=('', 28))
title.place(relx=0.08, rely=0.5, anchor=CENTER)

go_out = customtkinter.CTkButton(header, height=40, width=100, bg_color='pink', fg_color='#FF86AA', hover_color="#F75080", text_color='white', text='Выход', font=(1, 18), command=out)
go_out.place(relx=0.95, rely=0.5, anchor=CENTER)

qwer = customtkinter.CTkFrame(base, height=740, width=1200)
qwer.grid(row=1, column=0)

bgl = Label(qwer, image=baac)
bgl.grid(row=0, column=0)

graph = customtkinter.CTkFrame(qwer, height=500, width=700)
graph.place(x=850, y=250, anchor=CENTER)

bg_graph = Label(graph, image=bac)
bg_graph.grid(row=0, column=0)

def create_graphs():
    fig = plt.figure(figsize=(7, 5))
    ax1 = fig.add_subplot(221)
    ax1.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 4, 9, 16, 25, 4, 11, 9])
    ax1.set_title('Bitcoin')

    ax2 = fig.add_subplot(222)
    ax2.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 18, 7, 68, 125, 40, 56, 10])
    ax2.set_title('Ethereum')

    ax3 = fig.add_subplot(223)
    ax3.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 400, 340, 200, 184, 150, 90, 99])
    ax3.set_title('Tether')

    ax4 = fig.add_subplot(224)
    ax4.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 32, 243, 1024, 3125, 3000, 2300, 3400])
    ax4.set_title('Binance Coin')

    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.get_tk_widget().grid(row=0, column=0)

card1 = customtkinter.CTkButton(qwer, height=100, width=400, bg_color='#FFC0CB', fg_color='#7C5322', hover_color="#533818", border_width=2, border_color='#CD5C5C', text_color='white', text='Bitcoin           ', font=('', 30), image=c1, compound=LEFT, command=create_graphs)
card1.place(x=30, y=20)
card2 = customtkinter.CTkButton(qwer, height=100, width=400, bg_color='#FFC0CB', fg_color='#D5923F', hover_color="#A26C2A", border_width=2, border_color='#CD5C5C', text_color='white', text='Ethereum      ', font=('', 30), image=c2, compound=LEFT, command=create_graphs)
card2.place(x=30, y=140)
card3 = customtkinter.CTkButton(qwer, height=100, width=400, bg_color='#FFC0CB', fg_color='#D53FA4', hover_color="#A6267F", border_width=2, border_color='#CD5C5C', text_color='white', text='Tether            ', font=('', 30), image=c3, compound=LEFT, command=create_graphs)
card3.place(x=30, y=260)
card4 = customtkinter.CTkButton(qwer, height=100, width=400, bg_color='#FFC0CB', fg_color='#EA488A', hover_color="#D4216A", border_width=2, border_color='#CD5C5C', text_color='white', text='Binance Coin', font=('', 30), image=c4, compound=LEFT, command=create_graphs)
card4.place(x=30, y=380)



wallet_border = customtkinter.CTkFrame(base, height=200, width=400)
wallet_border.configure(fg_color='#FF7AA7')
wallet_border.place(x=30, y=570)

wallet = customtkinter.CTkFrame(base, height=198, width=398)
wallet.configure(fg_color='#FF7AA7', bg_color='#FF7AA7')
wallet.place(x=31, y=571)

label1 = tk.Label(wallet, text="Bitcoin: ", background='#FF7AA7', fg='white', font=('', 25), anchor='w', justify="left")
label1.pack()

label2 = tk.Label(wallet, text="Ethereum: ", background='#FF7AA7', fg='white', font=('', 25), anchor='w', justify="left")
label2.pack()

label3 = tk.Label(wallet, text="Tether: ", background='#FF7AA7', fg='white', font=('', 25), anchor='w', justify="left")
label3.pack()

label4 = tk.Label(wallet, text="Binance Coin: ", background='#FF7AA7', fg='white', font=('', 25), anchor='w', justify="left")
label4.pack()

def open_new_window():
    new_window = NewWindow()
    new_window2 = NewWindow2()

def sales():
    new_window3 = NewWindow3()
    new_window4 = NewWindow4()



btn_add = customtkinter.CTkButton(qwer, height=80, width=200, text="Купить", font=("", 22), bg_color='#FFC0CB', fg_color='#FF7AA7', hover_color="#FF548E", border_width=1, border_color='#FF548E', text_color='white', command=open_new_window)
btn_add.place(relx=0.51, rely=0.74, anchor=CENTER)

btn_add = customtkinter.CTkButton(qwer, height=80, width=200, text="Продать", font=("", 22), bg_color='#FFC0CB', fg_color='#FF7AA7', hover_color="#FF548E", border_width=1, border_color='#FF548E', text_color='white', command=sales)
btn_add.place(relx=0.51, rely=0.899, anchor=CENTER)

def update_label():
    global total
    input_value = entry.get()
    try:
            if label.cget("text"):
                if int(input_value) <= 100000:
                    total += int(input_value)
                    messagebox.showinfo("Успешно!", "Зачислено: " + str(input_value))
                    label.config(text=str(total))
                else:
                    messagebox.showinfo("Ошибка", "Будь реалистом! пиши числа не больше чем 100000")
            else:
                total = int(input_value)
    except ValueError:
        messagebox.showinfo("Ошибка", "Циферки пиши бро")


    entry.delete(0, tk.END)


def save_total():
    with open("total.txt", "w") as file:
        file.write(str(total))

def load_total():
    global total
    try:
        with open("total.txt", "r") as file:
            total = int(file.read())
            label.config(text=str(total))
    except FileNotFoundError:
        total = 0
        label.config(text="")

def on_closing():
    save_total()
    base.destroy()


total = 0

label = Label(base, text="", font=("", 25), background="#800080", fg='white')
label.place(relx=0.7, rely=0.73)

labell = customtkinter.CTkLabel(base, text="Введите сумму", text_color='white', fg_color='#C030C0', width=160)
labell.place(relx=0.7, rely=0.81)

entry = customtkinter.CTkEntry(base, width=160)
entry.place(relx=0.7, rely=0.85)

sumButton = customtkinter.CTkButton(base, height=50, width=160, text='Пополнить счёт',  fg_color="#C030C0", hover_color="#800080", border_width=1, border_color='#601860', command=update_label)
sumButton.place(relx=0.7, rely=0.899)


base.protocol("WM_DELETE_WINDOW", on_closing)
load_total()




base.mainloop()