import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import sqlite3

janela = ctk.CTk()

class Aplication():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.bgImagem()
        self.frame_login = None  # Frame da página de login
        self.pagina_atual = "login"  # Variável para acompanhar a página atual

        self.login_page()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

    def tela(self):
        janela.title("Sistema de login")
        janela.iconbitmap("img/favicon.ico")
        janela.geometry("500x320")
        janela.resizable(width=FALSE, height=FALSE)

    def bgImagem(self):
        imagem = PhotoImage(file="img/lolo.png")
        label_image = ctk.CTkLabel(master=janela, image=imagem, text=None)
        label_image.place(x=15, y=70)

    def login_page(self):
        if self.frame_login:
            self.frame_login.destroy()  # Destruir o frame da página de cadastro se existir

        self.frame_login = ctk.CTkFrame(
            master=janela, width=275, height=396, fg_color="white")
        self.frame_login.pack(side=RIGHT)

        label = ctk.CTkLabel(master=self.frame_login, text="Sistema de login")
        label.place(x=90, y=40)

        nome = ctk.CTkEntry(
            master=self.frame_login, placeholder_text="Digite o seu nome: ", width=200, height=38)
        nome.place(x=50, y=80)

        senha = ctk.CTkEntry(
            master=self.frame_login, placeholder_text="Digite a sua senha: ", show="*", width=200, height=38)
        senha.place(x=50, y=140)

        checkbox = ctk.CTkCheckBox(
            master=self.frame_login, text="Lembrar mais tarde", border_color="gray", border_width=1)
        checkbox.place(x=70, y=198)

        def logar():
            nome_usuario = nome.get()
            senha_usuario = senha.get()

            conexao = sqlite3.connect("sistema.db")
            cursor = conexao.cursor()

            cursor.execute("SELECT * FROM users WHERE NAME = ? AND PASSWORD = ?",
                           (nome_usuario, senha_usuario))
            resultado = cursor.fetchone()

            if resultado:
                print("Logado")
            else:
                print("Nome de usuário ou senha incorretos")

            conexao.close()

        button = ctk.CTkButton(master=self.frame_login, text="Login",
                               command=logar, width=200)
        button.place(x=50, y=235)

        cd_button = ctk.CTkButton(master=self.frame_login, text="Cadastrar", command=self.cadastrar_page,
                                  fg_color="lightgreen", width=200, hover_color="green", text_color="white")
        cd_button.place(x=50, y=270)

    def cadastrar_page(self):
        if self.frame_login:
            self.frame_login.destroy()  # Destruir o frame da página de login se existir

        self.frame_login = ctk.CTkFrame(master=janela, width=275, height=396, fg_color="white")
        self.frame_login.pack(side=RIGHT)

        label = ctk.CTkLabel(master=self.frame_login, text="Tela de cadastro")
        label.place(x=90, y=40)

        rg_nome = ctk.CTkEntry(
            master=self.frame_login, placeholder_text="Digite o seu nome: ", width=200, height=35)
        rg_nome.place(x=50, y=100)

        rg_senha = ctk.CTkEntry(
            master=self.frame_login, placeholder_text="Digite a sua senha: ", show="*", width=200, height=35)
        rg_senha.place(x=50, y=150)

        checkbox = ctk.CTkCheckBox(master=self.frame_login, text="Aceito os termos de privacidade",
                                   border_color="gray", border_width=2, corner_radius=40, fg_color="green")
        checkbox.place(x=40, y=198)

        def salvar():
            nome_usuario = rg_nome.get()
            senha_usuario = rg_senha.get()

            if nome_usuario and senha_usuario:  # Certificar-se de que ambos os campos estão preenchidos
                conexao = sqlite3.connect("sistema.db")
                cursor = conexao.cursor()

                cursor.execute("INSERT INTO users (NAME, PASSWORD) VALUES (?, ?)",
                               (nome_usuario, senha_usuario))
                conexao.commit()  # Salvar as alterações no banco de dados
                conexao.close()

                msg = messagebox.showinfo(
                    title="Estado de cadastro", message="Parabéns, usuário cadastrado com sucesso!")
            else:
                msg = messagebox.showwarning(
                    title="Erro de cadastro", message="Preencha todos os campos para cadastrar o usuário.")

        save_button = ctk.CTkButton(
            master=self.frame_login, text="Salvar", command=salvar, fg_color="green", width=200, text_color="white")
        save_button.place(x=50, y=240)

Aplication()
