import customtkinter as ctk 
from tkinter import messagebox
import tkinter as tk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("300x400")
app.title("Agendamento")

label = ctk.CTkLabel(app, text="Hora de agendar! ").pack(pady=5, padx=5)

opção=ctk.IntVar()

ctk.CTkRadioButton(app, text="Exame ", variable=opção, value=1).pack(pady=5)
ctk.CTkRadioButton(app, text="Consulta", variable=opção, value=2).pack(pady=5) 
ctk.CTkRadioButton(app, text="Retorno", variable=opção, value=3).pack(pady=5) 

label = ctk.CTkLabel(app, text="Agora so clicar em agendar e pronto").pack(pady=5, padx=5)

# Função que exibe a messagebox
def mostrar_mensagem():
    messagebox.showinfo(" ", "Seu exame foi marcado")

# Botão que chama a função
botao = ctk.CTkButton(app, text="Agendar", command=mostrar_mensagem)
botao.pack(pady=5)

label = ctk.CTkLabel(app, text="Você pode cancelar seu exame ").pack(pady=5, padx=5)
label = ctk.CTkLabel(app, text="Se você deseja cancelar, clique no botão abaixo").pack(pady=5, padx=5)



# Função para cancelar
def cancelar():
    messagebox.showinfo("Cancelamento", "Seu exame foi cancelado")

botao_cancelar = ctk.CTkButton(app, text="Cancelar", command=cancelar)
botao_cancelar.pack(pady=1)



app.mainloop()