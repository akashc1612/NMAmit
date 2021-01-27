from selenium import webdriver
from selenium.webdriver.common.keys import *
import tkinter as tk
from time import *

def site1():

    driver = webdriver.Chrome(executable_path="C:/Usrs/path/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.nmamit.nitte.edu.in/")
    driver.maximize_window()
    sleep(3 * 60 * 60)




def site2():
    root.destroy()
    root1 = tk.Tk()
    tk.Label(root1, text="Username").grid(row=0, sticky=tk.W)
    tk.Label(root1, text="password").grid(row=1, sticky=tk.W)

    user = tk.Entry(root1)
    passs = tk.Entry(root1)

    user.grid(row=0, column=1)
    passs.grid(row=1, column=1)

    def getInput():
        a = user.get()
        b = passs.get()

        root1.destroy()

        global p
        p = [a, b]

    tk.Button(root1, text="submit",
              command=getInput).grid(row=5, sticky=tk.W)
    tk.mainloop()

    driver = webdriver.Chrome(executable_path="C:/Users/path/chromedriver_win32/chromedriver.exe")
    driver.get("http://guru.nmamit.in/login/index.php")
    driver.maximize_window()
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys(p[0])
    password.send_keys(p[1])
    password.send_keys(Keys.RETURN)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/section/div/div/div[1]/div/div/div[1]/a/div/i").click()
    sleep(3 * 60 * 60)
def site3():
    root.destroy()
    root1 = tk.Tk()
    tk.Label(root1, text="parent mobile").grid(row=0, sticky=tk.W)
    tk.Label(root1, text="password").grid(row=1, sticky=tk.W)

    user = tk.Entry(root1)
    passs = tk.Entry(root1)

    user.grid(row=0, column=1)
    passs.grid(row=1, column=1)

    def getInput():
        a = user.get()
        b = passs.get()

        root1.destroy()

        global p
        p = [a, b]

    tk.Button(root1, text="submit",
              command=getInput).grid(row=5, sticky=tk.W)
    tk.mainloop()

    driver = webdriver.Chrome(executable_path="C:/Users/path/chromedriver_win32/chromedriver.exe")
    driver.get("http://www.ioncudos.com/nmamit_parent/login")
    driver.maximize_window()
    username = driver.find_element_by_name("phone")
    password = driver.find_element_by_name("password")
    username.send_keys(p[0])
    password.send_keys(p[1])
    password.send_keys(Keys.RETURN)
    sleep(3 * 60 * 60)

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()
browseButton_site1 = tk.Button(text="     NMAMIT official site         ",
                                command=site1, bg='blue', fg='black', font=
                                ('helvetica', 14, 'bold'))
browseButton_site2 = tk.Button(text="     Moodle         ",
                                command=site2, bg='blue', fg='black', font=
                                ('helvetica', 14, 'bold'))
browseButton_site3 = tk.Button(text="     Parent login         ",
                                command=site3, bg='blue', fg='black', font=
                                ('helvetica', 14, 'bold'))
browseButton_site4 = tk.Button(root, text="Quit", command=root.destroy).pack()
canvas1.create_text(150, 30, text = 'WELCOME TO NMAMIT')
canvas1.create_window(150, 100, window = browseButton_site1)
canvas1.create_window(150, 150, window = browseButton_site2)
canvas1.create_window(150, 200, window = browseButton_site3)
canvas1.create_window(150,250, window = browseButton_site4)
root.mainloop()
