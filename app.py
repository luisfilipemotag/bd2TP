import psycopg2
from tkinter import *
import os
import psycopg2
import Login_V

def Loginface(root):
    my_gui = Login_V.Login(root)



def main():
    for arg in sys.argv[1:]:
       print(arg)
    
    root = Tk()
    Loginface(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
  
