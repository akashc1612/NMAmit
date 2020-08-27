from selenium import webdriver
from selenium.webdriver.common.keys import *
import os
def fun():
    print("WELCOME TO NMAMIT:")
    print("1. NMAMIT official site")
    print("2. Moodle")
    print("3. Parents Login")
    a = input("Please enter one of the above options.")
    try:
        if int(a) == 1:
            driver = webdriver.Chrome(executable_path="C:/Users/path/to/chromedriver.exe")
            driver.get("https://www.nmamit.nitte.edu.in/")
        elif int(a) == 2:
            driver = webdriver.Chrome(executable_path="C:/Users/path/to/chromedriver.exe")
            driver.get("http://guru.nmamit.in/login/index.php")
        elif int(a) == 3:
            driver = webdriver.Chrome(executable_path="C:/Users/path/to/chromedriver.exe")
            driver.get("http://www.ioncudos.com/nmamit_parent/login")
        else:
            clear = lambda: os.system('cls')
            clear()
            print("please enter a correct option")
            fun()
    except:
        clear = lambda: os.system('cls')
        clear()
        print("please enter a correct option")
        fun()
fun()
