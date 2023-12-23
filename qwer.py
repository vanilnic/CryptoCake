from tkinter import *
from tkinter import messagebox as ms
import sqlite3

import customtkinter
from PIL import ImageTk

with sqlite3.connect('avtoriz.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY, password TEX NOT NULL);')
db.commit()
db.close()

class main:
    def __init__(self, master):
        self.master = master
        self.username = customtkinter.StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect('avtoriz.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            root.destroy()
            import base
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n добрый день'
            # self.head['pady'] = 150
        else:
            ms.showerror('Уведомление', 'Данный пользователь не найден!')

    def new_user(self):
        with sqlite3.connect('avtoriz.db') as db:
            c = db.cursor()

        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Уведомление!', 'Имя пользователя занято, попробуйте другое.')
        else:
            ms.showinfo('Успех!', 'Пользователь создан!')
            self.log()

        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.crf.pack()

    def widgets(self):
        self.cakes = PhotoImage(file='picture/mew.png')
        self.cakemain = PhotoImage(file="picture/qq.png")

        self.logf = Frame(self.master, height=600, width=1000)

        self.bg_bg = Label(self.logf, image=self.cakes)
        self.bg_bg.grid(row=0, column=0)

        self.lbl = customtkinter.CTkLabel(self.logf, text="Авторизация", fg_color="white", font=(2, 20))
        self.lbl.place(relx=0.5, rely=0.29, anchor=CENTER)

        self.basefr = Frame(self.logf, height=230, width=300)
        self.basefr.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.lbl = Label(self.basefr, image=self.cakemain)
        self.lbl.grid(row=0, column=0)

        customtkinter.CTkLabel(self.basefr, bg_color='#D94E3F', text_color='black', height=12, text='Логин: ', font=('', 14)).place(relx=0.36, rely=0.28, anchor=CENTER)
        customtkinter.CTkEntry(self.basefr, textvariable=self.username).place(relx=0.5, rely=0.4, anchor=CENTER)
        customtkinter.CTkLabel(self.basefr, bg_color='#F9D2BD', text_color='black', height=12, text='Пароль: ', font=('', 14)).place(relx=0.37, rely=0.55, anchor=CENTER)
        customtkinter.CTkEntry(self.basefr, textvariable=self.password, show='*').place(relx=0.5, rely=0.65, anchor=CENTER)
        customtkinter.CTkButton(self.basefr, fg_color="#800080", hover_color="pink", text_color="#fff", text='Вход', border_color="pink", border_width=1, height=24, width=100, command=self.login).place(relx=0.13, rely=0.8)
        customtkinter.CTkButton(self.basefr, fg_color="#800080", hover_color="pink", text_color="#fff", text='Регистрация', border_color="pink", border_width=1, height=24, width=100, command=self.cr).place(relx=0.55, rely=0.8)


        self.logf.pack()

        self.crf = Frame(self.master, height=600, width=1000)

        self.bg_bg = Label(self.crf, image=self.cakes)
        self.bg_bg.grid(row=0, column=0)

        self.lbl = customtkinter.CTkLabel(self.crf, text="Регистрация", fg_color="white", font=('', 20))
        self.lbl.place(relx=0.5, rely=0.29, anchor=CENTER)

        self.basefr2 = Frame(self.crf, height=230, width=300)
        self.basefr2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.lbl = Label(self.basefr2, image=self.cakemain)
        self.lbl.grid(row=0, column=0)

        customtkinter.CTkLabel(self.basefr2, bg_color='#D94E3F', text_color='black', height=12, text='Логин: ', font=('', 14)).place(relx=0.36, rely=0.28, anchor=CENTER)
        customtkinter.CTkEntry(self.basefr2, textvariable=self.n_username).place(relx=0.5, rely=0.4, anchor=CENTER)
        customtkinter.CTkLabel(self.basefr2, bg_color='#F9D2BD', text_color='black', height=12, text='Пароль: ', font=('', 14)).place(relx=0.37, rely=0.55, anchor=CENTER)
        customtkinter.CTkEntry(self.basefr2, textvariable=self.n_password, show='*').place(relx=0.5, rely=0.65, anchor=CENTER)
        customtkinter.CTkButton(self.basefr2, fg_color="#800080", hover_color="pink", text_color="#fff", text='Регистрация', border_color="pink", border_width=1, height=24, width=100, command=self.new_user).place(relx=0.13, rely=0.8)
        customtkinter.CTkButton(self.basefr2, fg_color="#800080", hover_color="pink", text_color="#fff", text='Назад', border_color="pink", border_width=1, height=24, width=100, command=self.log).place(relx=0.55, rely=0.8)


if __name__ == '__main__':
    root = Tk()
    root.title('Авторизация')
    root.geometry('1000x600')
    root.resizable(width=False, height=False)
    main(root)
    root.mainloop()


