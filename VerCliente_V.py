import psycopg2
import tkinter as tk
from tkinter import * 
from tkinter.ttk import Combobox
import os
import psycopg2

import Index_Ger_V


class Vcliente(tk.Frame):
    def __init__(self, master):
     
        self.master = master
        
        master.title("Clientes")
        master.geometry("600x600")
        master.configure(background='green')
        
        password = StringVar()
        self.passw = Entry(master, textvariable=password ,  width = 200)
        self.passw.pack()
        
        self.other_button = Button(master, text="pesquisar" ,command=lambda: self.ins(password),  height = 2, width = 600)
        self.other_button.pack()
        self.other_button = Button(master, text="mostrar todos" ,command=lambda: self.show(),  height = 2, width = 600)
        self.other_button.pack()
        self.Lb1 = Listbox()
        self.other_button = Button(master, text="voltar" , command=lambda:self.new_window() , height = 2, width = 600)
        self.other_button.pack(side=BOTTOM)
       
    
  
    def ins(self , password):

        
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("select * from MostrarCliente('"+password.get()+"')")
        clientes = curs.fetchall() 
        
        
        self.Lb1.delete(0,END)
        self.Lb1.pack(side="left",fill="both", expand=True)
        
        i=0
        for item in clientes :
           self.Lb1.insert(i ,"Nome:    "+item[0] ,"Nif:  "+item[1] ,"Contacto:   "+item[2] )
           i+1
        
        
        self.Lb1.pack()
        curs.close()
        connection.close()
             
    def show(self):

        
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("select * from listarclientes()")
        clientes = curs.fetchall() 
        
        
        self.Lb1.delete(0,END)
        self.Lb1.pack(side="left",fill="both", expand=True)
        
        i=0
        for item in clientes :
           self.Lb1.insert(i ,"Nome:    "+item[0] ,"Nif:  "+item[1] ,"Contacto:   "+item[2] )
           i+1
        
        
        self.Lb1.pack()
        curs.close()
        connection.close()
      

    def new_window(self):

        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Index_Ger_V.IndexGer(self.master) 
        self.master.mainloop()
    


      