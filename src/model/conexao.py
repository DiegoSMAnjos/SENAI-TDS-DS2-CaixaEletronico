import mysql.connector


def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="2wNk#kYWFH@$2D3RcV5!",
        database="db_caixa_eletronico")
    return conexao
