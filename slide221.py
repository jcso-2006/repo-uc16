def criar_banco_dados(nome_banco):
    try:
        # Conectar ao servidor MySQL
        conexao = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",
            password="sua_senha"
        )

        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Criar o banco de dados
        cursor.execute("CREATE DATABASE {}".format(nome_banco))

        print("Banco de dados", nome_banco, "criado com sucesso!")
    except mysql.connector.Error as e:
        print("Erro ao criar o banco de dados:", e)
    finally:
        if conexao:
            conexao.close()

def main():
    print("Bem-vindo! Este programa irá criar um novo banco de dados no MySQL.")
    nome_banco = input("Por favor, digite o nome do banco de dados que deseja criar: ")

    criar_banco_dados(nome_banco)

if __name__ == "__main__":
    main()

