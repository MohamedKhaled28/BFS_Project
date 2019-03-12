import pymysql
from tkinter import *

class Application ():
    def __init__(self):
       self.root = Tk()
       self.root.title("Login")
       self.image = PhotoImage(file='Cotton_Candy_Castle_Background.gif')
       self.label11 = Label( image=self.image)
       self.label11.grid(row=0, column=0,columnspan=900,rowspan=900)
       self.user_name=Label(text="User name :")
       self.user_name.grid(row=100,column=50)
       self.UserName_value = Entry( width=30)
       self.UserName_value.grid(row=100, column=51)
       self.password = Label( text="Password :")
       self.password.grid(row=110,column=50)
       self.password_value=Entry(width=30)
       self.password_value.grid(row=110,column=51)
       self.submit = Button( text="submit",command=self.login)
       self.submit.grid(row=115,column=50,columnspan=2)
       self.root.mainloop()
    def login(self):
        name =self.UserName_value.get()
        password = self.password_value.get()
        if (name == "" or password == ""):
            self.out = Label(text="oops!! please fill two inputs").grid(row=130, column=53)
        else:
            db = pymysql.connect(
                host='localhost',
                user='root',
                passwd='',
                db='users'
            )
            cursor = db.cursor()
            sql = "select * from user where user.username = '" + name + "'and user.password = '" + password + "'"
            result = cursor.execute(sql)
            if result:
                self.root.destroy()
                exec(open("graph.py").read(), globals())
            else:
                self.out = Label(text="oops!! invalid username or password").grid(row=130, column=53)
            db.close()
Application()


