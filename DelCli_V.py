import psycopg2
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import os
import psycopg2
import MenuADU



class DelAll:

    def __init__(self, master):
        self.master = master
        master.title("Eliminar")
        master.geometry("600x600")
        master.configure(background='green')
     
        txt_nif = StringVar()
        
        self.labelc = Label(master, text="Nif:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.nif = Entry(master, textvariable=txt_nif  , width = 600)
        self.nif.pack()

        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.other_button = Button(master, text="Eliminar" ,command=lambda: self.dell(txt_nif), height = 2, width = 600)
        self.other_button.pack()
        
        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.other_button = Button(master, text="Voltar",command=lambda: self.new_window4() , height = 2, width = 600)
        self.other_button.pack(side= BOTTOM)

      
    def new_window4(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = MenuADU.MenuCli(self.master) 
        self.master.mainloop()
    
    def dell(self , txt_nif):

        
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()
       
        curs.execute("select deleteCliente('"+txt_nif.get()+"')")

        connection.commit()
        curs.close()
        connection.close()
        self.labeld = Label( text="eliminada" , height = 1, width = 600)
        self.labeld.pack()
        self.labeld.configure(  background='green')
        
             

 
   
       

       

    
      