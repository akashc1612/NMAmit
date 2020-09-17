from selenium import webdriver
import tkinter as tk
from time import *
def site1():
    driver = webdriver.Chrome(executable_path="C:/Users/path to/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.nmamit.nitte.edu.in/")
    driver.maximize_window()
    sleep(60 * 60)
def site2():
    driver = webdriver.Chrome(executable_path="C:/Users/path to/chromedriver_win32/chromedriver.exe")
    driver.get("http://guru.nmamit.in/login/index.php")
    driver.maximize_window()
    sleep(60 * 60)
def site3():
    driver = webdriver.Chrome(executable_path="C:/Users/path to/chromedriver_win32/chromedriver.exe")
    driver.get("http://www.ioncudos.com/nmamit_parent/login")
    driver.maximize_window()
    sleep(60 * 60)





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
canvas1.create_text(150, 30, text = 'WELCOME TO NMAMIT')
canvas1.create_window(150, 100, window = browseButton_site1)
canvas1.create_window(150, 150, window = browseButton_site2)
canvas1.create_window(150, 200, window = browseButton_site3)
root.mainloop()
