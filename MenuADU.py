import psycopg2
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
import AddCli_V
import DelCli_V
import Updatecli


class MenuCli(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title("R&R")
        master.geometry("600x600")
        master.configure(background='green')
        

        self.labelc = Label(master, text="Clientes:"  , height = 2, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.btnAddCli = Button(master, text="Adicionar" , command=lambda: self.new_window1(), height = 2, width = 600)
        self.btnAddCli.pack()

        self.btnVercli = Button(master, text="Update Contacto" , command=lambda: self.new_window2(),height = 2, width = 600)
        self.btnVercli.pack()

        self.btnVerEm = Button(master, text="Eliminar" , command=lambda: self.new_window3() , height = 2, width = 600)
        self.btnVerEm.pack()

        self.btnVolta = Button(master, text="Voltar" , command=lambda: self.new_window4() , height = 2, width = 600)
        self.btnVolta.pack()

        

       
   
    def new_window1(self):

        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = AddCli_V.AddUser(self.master) 
        self.master.mainloop()

    def new_window2(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Updatecli.UpUser(self.master) 
        self.master.mainloop()

    def new_window3(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = DelCli_V.DelAll(self.master) 
        self.master.mainloop()

    

    def new_window4(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Index_Ger_V.IndexGer(self.master) 
        self.master.mainloop()
             
    

   
 
   
       

    
    
   