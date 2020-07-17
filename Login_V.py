import psycopg2
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import os
import psycopg2
import Index_Ger_V
class Login:

    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.geometry("600x240")
        master.configure(background='green')
        

        #
        v = []
      
       
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")
        curs = connection.cursor()

        curs.execute("select * from Listar_Restaurantes")
        resta = curs.fetchall()  
        i=0
        for item in resta :
         v.append(item[0])
        
         i+1
        curs.close()
        connection.close()

        #
        self.labelR = Label(master, text="Restaurante" , height = 2, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')

        
        self.combo = Combobox(master,values=v ,  width = 600)
        self.combo.pack()
        self.combo.bind('<<ComboboxSelected>>', self.combo.get())

        self.other_button = Button(master, text="refresh funcionarios", command=lambda: self.refresh(self.combo.get()), height = 1, width = 100)
        self.other_button.pack()


        self.comboid = Combobox(master,  width = 600)
        self.comboid.pack()
        self.comboid.bind('<<ComboboxSelected>>', self.combo.get())

        
        self.labelR = Label(master, text="Password" , height = 2, width = 600)
        self.labelR.pack()
        self.labelR.configure(  background='green')
        
        
        self.passw = Entry(master,  show='*' ,  width = 600)
        self.passw.pack()

        self.btnlogin = Button(master, text="Login", command=lambda: self.Login(self.comboid.get(),self.passw.get()), height = 1, width = 100)
        self.btnlogin.pack()

        

    def refresh(self ,k):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
        a = []
        curs.execute("select * from MostrarFuncionarios('"+k+"')")
        resta = curs.fetchall()  
        i=0
        for item in resta :
         a.append(item[0])
        
         i+1
        curs.close()
        connection.close()
        self.comboid.configure(value=a)

    def Login(self ,k, passs):
        connection = psycopg2.connect(user="postgres",password="Chip0123scp", host="127.0.0.1", port="5432",database="RandR")   
        curs = connection.cursor()
        resta = 0
        curs.execute("select  testa_login ('"+k+"', '"+str(passs)+"')")
        resta = curs.fetchone()  
        print(str(resta))
        if str(resta) == "(1,)" : 
            self.master.destroy() 
            self.master = tk.Tk() 
            self.app = Index_Ger_V.IndexGer(self.master) 
            self.master.mainloop()
        else :
         self.labels = Label( text= "Erro no login" , height = 2, width = 600)
         self.labels.pack()
         self.labels.configure(  background='green')
            
        
        curs.close()
        connection.close()
        

        
        
 
   
       

       

    
      