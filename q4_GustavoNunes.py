import mysql.connector

# Função para conectar ao banco de dados MySQL
conectar_bd = lambda: mysql.connector.connect(
    host="localhost",
    user="hoot",
    password="020603"
)

# Função para inserir um registro em uma tabela
inserir_registro = lambda tabela, valores: (
    lambda conn: (
        lambda cursor: (
            cursor.execute(f"INSERT INTO {tabela} VALUES ({', '.join(['%s'] * len(valores))})", valores),
            conn.commit()
        )
    )(conn.cursor())
)

# Função para remover um registro de uma tabela
remover_registro = lambda tabela, id: (
    lambda conn: (
        lambda cursor: (
            cursor.execute(f"DELETE FROM {tabela} WHERE id = %s", (id,)),
            conn.commit()
        )
    )(conn.cursor())
)

# Função para consultar registros de uma tabela
consultar_registros = lambda tabela: (
    lambda conn: (
        lambda cursor: (
            cursor.execute(f"SELECT * FROM {tabela}"),
            cursor.fetchall()
        )
    )(conn.cursor())
)

# Função lambda para executar o código
executar_programa = lambda conexao: (
    # Inserir um usuário
    inserir_registro("USUARIOS", (1, "gustavo", "PS5"))(conexao),

    # Inserir um jogo
    inserir_registro("JOGOS", (1, "rainbow six siege", "2023-10-16"))(conexao),

    # Consultar todos os usuários
    resultados_usuarios = consultar_registros("USUARIOS")(conexao)
    print("Usuários:")
    for resultado in resultados_usuarios:
        print(resultado),

    # Consultar todos os jogos
    resultados_jogos = consultar_registros("JOGOS")(conexao)
    print("Jogos:")
    for resultado in resultados_jogos:
        print(resultado),

    # Remover um usuário
    remover_registro("USUARIOS", 1)(conexao),

    # Remover um jogo
    remover_registro("JOGOS", 1)(conexao)
)

# Chamar a função diretamente
conexao = conectar_bd()
executar_programa(conexao)
conexao.close()
