import mysql.connector

def conn():
    conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "1234",
                database = "db_caixaelet")
    return conexao
