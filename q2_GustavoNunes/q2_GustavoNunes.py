users = {
  "gustavo": "020603",
  "caio": "060611"
}

usuario = lambda: input("Qual seu nome? ")
senha = lambda: input("Qual sua senha? ")
negado = lambda: print("FRACASSO")
aceito = lambda: print("SUCESSO")

# Função lambda para escrever no arquivo
escrever_no_arquivo = lambda f, texto: [f.write("\n" + nline) for nline in texto]

#----------------------------------
nome = lambda user: users[user]
processo = lambda user, lsenha: not users.get(user) == lsenha
nome_usuario = usuario()
senha_usuario = senha()
#----------------------------------
path = "./q2_GustavoNunes/q2_GustavoNunes.txt" 

# Texto para ser escrito no arquivo em caso de sucesso e em caso de falha
texto_sucesso = [f"Nome:{nome_usuario}", f"Senha:{senha_usuario}", "Login feito com sucesso"]
texto_falha = [f"Nome:{nome_usuario}", f"Senha:{senha_usuario}", "Falha ao fazer o login!"]

# Função lambda para realizar o login
login = lambda users, lpessoa, lsenha, negado, aceito, escrever_fn, sucesso, falha: (negado() or escrever_fn(open(path, "a"), falha) or users.get(lpessoa)) if processo(lpessoa, lsenha) else (aceito() or escrever_fn(open(path, "a"), sucesso))

usuario_logado = login(users, nome_usuario, senha_usuario, negado, aceito, escrever_no_arquivo, texto_sucesso, texto_falha)
