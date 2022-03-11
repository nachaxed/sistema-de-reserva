from ast import Lambda
from cProfile import label
from calendar import month
from cgitb import grey, text
from distutils.log import info
from logging import root
from msilib import Table
from re import M
from sre_parse import State
from tkinter import *
from tkinter import messagebox
import tkinter
from tokenize import String
from turtle import st, title, width, window_width
from MySQLdb import Time
from tkcalendar import DateEntry
from tkinter import ttk 
from tkinter.messagebox import *
from functools import partial
import os



# Manipulate data from registration fields 
def send_data():
  username_info = username.get()
  fullname_info = fullname.get()
  cal_info = str(cal.get())
  lista_desplegable_info = str(lista_desplegable.get())
  lista_desplegable1_info = str(lista_desplegable1.get())
  duracion_info = str(duracion.get())

  print(username_info,"\t", fullname_info,"\t", cal_info,"\t",lista_desplegable_info,"\t", lista_desplegable1_info,"\t", duracion_info, "\t")
 
#  Open and write data to a file
#en donde dice open colocar la ruta en donde queremos que se graben los texts de reserva

  file = open(r"C:\Users\54261\Desktop\interbrain\reservas\ticket\reserva-" + username_info + ".txt", "a+")
  file.write("Nombre"+ "\t" + username_info)
  file.write("\n")
  file.write("Apellido" + "\t" + fullname_info)
  file.write("\n")
  file.write("Fecha de reserva" + "\t" + cal_info)
  file.write("\n")
  file.write("Sala de reserva" + "\t" +lista_desplegable_info)
  file.write("\n")
  file.write("Hora de reserva" + "\t" + lista_desplegable1_info)
  file.write("\n")
  file.write("Duración de la reserva" + "\t" + duracion_info)
  file.write("\n\n")
  
  file.close()
  messagebox.showinfo(title="Reserva", message=" Su reserva ha sido un exito!  {} {} ,  Por favor, diríjase a la carpeta de ticket para retirar su reserva! MUCHAS GRACIAS".format(username_info, fullname_info))
  
 
#  Delete data from previous event
  username_entry.delete(0, END)
  fullname_entry.delete(0, END)
  cal_entry.delete(0, END)
  lista_desplegable_entry.delete(0, END)
  lista_desplegable1_entry.delete(0, END)
  duracion_entry.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Sistema de reservas")
mywindow.iconbitmap(r'C:\Users\54261\Desktop\interbrain\reservas\photo.ico')

mywindow.resizable(False,False)
mywindow.config(background = "#c679ac")

main_title = Label(text = "Sistema de reserva | InterBrain", font = ("Cambria", 14), bg = "#230A24", fg = "white", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
username_label = Label(text = "Nombre", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
fullname_label = Label(text = "Apellido", bg = "#FFEEDD")
fullname_label.place (x = 22, y = 130)
cal_label = Label(text = "Fecha de reserva", bg="#FFEEDD")  
cal_label.place(x=320, y=75)
lista_desplegable = Label(text= "Sala a reservar", bg="#FFEEDD")
lista_desplegable.place(x= 22, y=200)
lista_desplegable1 = Label(text="Hora de reserva", bg="#FFEEDD")
lista_desplegable1.place(x=320, y=170)
duracion_label = Label(text="Duracion de la reserva", bg="#FFEEDD")
duracion_label.place(x=320, y=240)

# Get and store data from users 
username = StringVar()
fullname = StringVar()
cal = StringVar()
lista_desplegable = StringVar()
lista_desplegable1 = StringVar()
duracion = StringVar()

 
username_entry = Entry(textvariable = username, width = "40")
fullname_entry = Entry(textvariable = fullname, width = "40")
cal_entry = Entry(textvariable = cal, width= "40")
lista_desplegable_entry = Entry( textvariable= "", width= "40")
lista_desplegable1_entry = Entry(textvariable="", width="40")
duracion_entry = Entry(textvariable= duracion , width="40")

username_entry.place(x = 22, y = 100)
fullname_entry.place(x = 22, y = 160)
 
#calendario 

cal = DateEntry(mywindow,width=30,year=2022)

cal.place(x=320, y=118, width=100, height=30)
cal.config(headersbackground='#364c55', foreground='#000', background='#fff', headersforeground ='#fff'  )

#horas seleccionar
lista_desplegable1 = ttk.Combobox(mywindow,width=17, state='readonly')
lista_desplegable1.place(x = 320, y = 200)

#lista de opciones horas
opciones1 = ["07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00", "16:30","17:00","17:30","18:00"]

#obtener los valores horas 
lista_desplegable1['values'] = opciones1

#lista desplegable

lista_desplegable = ttk.Combobox(mywindow,width=17, state='readonly')
lista_desplegable.place(x = 22, y = 235)

#lista de opciones
opciones = ["Sala C#", "Sala Python", "Sala IA"]

#obtener los valores
lista_desplegable['values'] = opciones

#duracion de la reserva

duracion = ttk.Combobox(mywindow, width="17", state='readonly')
duracion.place(x= 320, y = 270)

#lista de duracion

opciones2 = ["01:00 horas", "02:00 horas"]

#obtenemos los datos de duración

duracion['values'] = opciones2

# Submit Button
submit_btn = Button(mywindow,text = "Reservar", width = "30", height = "2", command= (send_data), bg = "#5C4577", fg="white")
submit_btn.place(x = 22, y = 320)


mywindow.mainloop()
