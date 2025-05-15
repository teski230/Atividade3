import customtkinter as ctk
import subprocess as spr

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("400x400")
app.title("Confirmar Dados")

label = ctk.CTkLabel(app, text="Informe seu nome : ").pack(pady=5, padx=5)
ctk.CTkEntry(app).pack(pady=5)
label = ctk.CTkLabel(app, text="Digite sua senha ").pack(pady=5, padx=5)
ctk.CTkEntry(app, show="*").pack(pady=5)


def abrir_agendamento():
    spr.Popen(["python", "agendamento.py"])


ctk.CTkButton(app, text="Continuar", command=abrir_agendamento).pack(pady=5, padx=5)



app.mainloop()