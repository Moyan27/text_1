import tkinter as tk
from tkinter import messagebox
from check_user_info import Check_info
import made_user
import Main_page

class Goin_page(object):
    def __init__(self, root):
        self.root = root
        self.root.resizable(0, 0)
        self.root.geometry('300x180+500+300')
        self.root.title('登入界面')
        self.root.iconbitmap('1.ico')
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()
        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='账号').grid(row=1, column=1, padx=20, pady=10)
        tk.Entry(self.page, textvariable=self.user_name).grid(row=1, column=2)
        tk.Label(self.page, text='密码').grid(row=2, column=1, padx=20, pady=10)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=2)
        tk.Button(self.page, text='登入', command=self.goin).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.page, text='注册', command=self.create_user).grid(row=3, column=2, padx=10, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=3, padx=10, pady=10)


    def goin(self):
        name = self.user_name.get()
        password = self.password.get()
        flag, message = Check_info().check_info(name, password)
        if flag:
            self.page.destroy()
            Main_page.Main_page(self.root)
        else:
            messagebox.showwarning(title='警告', message=message)

    def create_user(self):
        self.page.destroy()
        made_user.Made_user(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    goin_page = Goin_page(root)
    root.mainloop()
