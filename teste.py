import mysql.connector
from mysql.connector import Error

def testar_conexao():
    try:
        # Tentando conectar ao banco de dados
        banco = mysql.connector.connect(
            host='localhost',
            port='3307',
            user='root',
            password='12345678',
            database='appjunina'
        )

        if banco.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")
            # Aqui você pode realizar outras ações, como consultar ou manipular dados
            banco.close()  # Não se esqueça de fechar a conexão ao final
        else:
            print("Falha na conexão ao banco de dados!")

    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# Chamar a função para testar a conexão
testar_conexao()
