import psycopg2
from tkinter import *

from tkinter.ttk import Combobox
import os
import psycopg2
import MenuIA
import tkinter as tk
class AddAlergia:

    def __init__(self, master):
        self.master = master
        master.title("Add tipo de Alergias")
        master.geometry("600x600")
        master.configure(background='green')
     
        txt_des = StringVar()
        
        self.labelc = Label(master, text="Designacao:" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.des = Entry(master, textvariable=txt_des  , width = 600)
        self.des.pack()

        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.other_button = Button(master, text="Adiconar tipo de alergia" ,command=lambda: self.Add(txt_des), height = 2, width = 600)
        self.other_button.pack()
        
        self.labelc = Label(master, text="" , height = 1, width = 600)
        self.labelc.pack()
        self.labelc.configure(  background='green')
      
        self.other_button = Button(master, text="Voltar",command=lambda: self.new_window4() , height = 2, width = 600)
        self.other_button.pack()

    
    def Add(self , txt_des):
     if len(self.des.get()) != " ": 
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()
       
        curs.execute("call insertAlergias('"+txt_des.get()+"');")

        connection.commit()
        curs.close()
        connection.close()
        self.labeld = Label( text="Inserida" , height = 1, width = 600)
        self.labeld.pack()
        self.labeld.configure(  background='green')
        
             
    def new_window4(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = MenuIA.MenuIA(self.master) 
        self.master.mainloop()
 
   
       

       

    
      