import customtkinter

customtkinter.set_appearance_mode("dark")

janela = customtkinter.CTk()

janela.geometry("300x300")


def clique():
    print("Fazer login do usuário!")

texto = customtkinter.CTkLabel(janela, text="Fazer logn")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
