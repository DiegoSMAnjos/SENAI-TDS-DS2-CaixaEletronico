import mysql.connector


def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="db_caixa_eletronico")
    return conexao
