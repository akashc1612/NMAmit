from selenium import webdriver
from selenium.webdriver.common.keys import *
import tkinter as tk
from tkinter import filedialog
import os
def site1():
    driver = webdriver.Chrome(executable_path="C:/Users/ras73/Desktop/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.nmamit.nitte.edu.in/")
def site2():
    driver = webdriver.Chrome(executable_path="C:/Users/ras73/Desktop/chromedriver_win32/chromedriver.exe")
    driver.get("http://guru.nmamit.in/login/index.php")
def site3():
    driver = webdriver.Chrome(executable_path="C:/Users/ras73/Desktop/chromedriver_win32/chromedriver.exe")
    driver.get("http://www.ioncudos.com/nmamit_parent/login")





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
