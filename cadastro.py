import customtkinter as ctk 
import subprocess as spr

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("400x750")
app.title("TecMED")

# função que abre a janela de login
def abrir_login():
    spr.Popen(["python", "Login.py"])

# Texto perguntando se o usuário tem conta
label = ctk.CTkLabel(app, text="Você já possui uma conta?")
label.pack(pady=20)
label = ctk.CTkLabel(app, text="se sim, clique em login ")
label.pack(pady=20)

# Botão de login com função associada
ctk.CTkButton(app, text="Login", command=abrir_login).pack(pady=1, padx=1)

# Texto sugerindo cadastro
label = ctk.CTkLabel(app, text="Se você não possui, faça uma agora")
label.pack(pady=5, padx=5)

label = ctk.CTkLabel(app, text="Nome").pack(pady=5, padx=5)
ctk.CTkEntry(app).pack(pady=5)
label = ctk.CTkLabel(app, text="CPF").pack(pady=5, padx=5)
ctk.CTkEntry(app).pack(pady=5)
label = ctk.CTkLabel(app, text="Data de nascimento").pack(pady=5, padx=5)
ctk.CTkEntry(app).pack(pady=5)
label = ctk.CTkLabel(app, text="Numero de contato").pack(pady=5, padx=5)
ctk.CTkEntry(app).pack(pady=5)
label = ctk.CTkLabel(app, text="Genero: ").pack(pady=5, padx=5)

opção=ctk.IntVar()

ctk.CTkRadioButton(app, text="Masculino", variable=opção, value=1).pack(pady=5)
ctk.CTkRadioButton(app, text="Feminino", variable=opção, value=2).pack(pady=5) 

label = ctk.CTkLabel(app, text="Crie uma senha").pack(pady=5, padx=5)
ctk.CTkEntry(app, show="*").pack(pady=5)

# função do continuar
def abrir_login():
    spr.Popen(["python", "Login.py"])


# botao continuar
ctk.CTkButton(app, text="Continuar", command=abrir_login).pack(pady=5, padx=5)



app.mainloop()