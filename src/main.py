from PyQt5 import uic, QtWidgets
from model.Conexao import *

# Carregamento do aplicativo

app = QtWidgets.QApplication([])
telaInicial = uic.loadUi('src/view/telaInicial.ui')
telaSaque = uic.loadUi('src/view/telaSaque.ui')
telaClienteEntrar = uic.loadUi('src/view/telaClienteEntrar.ui')
telaClienteCadastrar = uic.loadUi('src/view/telaClienteCadastrar.ui')
telaReposicaoCedulas = uic.loadUi('src/view/telaReposicaoCedulas.ui')

# Conexao com o banco de dados

conn = conectar_banco()


# Definições de Funções


def trocaTelas(tela01, tela02):
    tela01.close()
    tela02.show()
    return


def addValor(numero):
    temp = telaSaque.lineEditValor.text() + str(numero)
    telaSaque.lineEditValor.setText(temp)

def removeValor():
    temp = telaSaque.lineEditValor.text()[:-1]
    telaSaque.lineEditValor.setText(temp)

def botoesNumericos():
    telaSaque.btnNum0.clicked.connect(lambda: addValor(0))
    telaSaque.btnNum1.clicked.connect(lambda: addValor(1))
    telaSaque.btnNum2.clicked.connect(lambda: addValor(2))
    telaSaque.btnNum3.clicked.connect(lambda: addValor(3))
    telaSaque.btnNum4.clicked.connect(lambda: addValor(4))
    telaSaque.btnNum5.clicked.connect(lambda: addValor(5))
    telaSaque.btnNum6.clicked.connect(lambda: addValor(6))
    telaSaque.btnNum7.clicked.connect(lambda: addValor(7))
    telaSaque.btnNum8.clicked.connect(lambda: addValor(8))
    telaSaque.btnNum9.clicked.connect(lambda: addValor(9))
    telaSaque.btnCorrigir.clicked.connect(lambda: removeValor())


# Navegação entre Telas

telaInicial.btnEntrarCliente.clicked.connect(lambda: trocaTelas(telaInicial, telaClienteEntrar))
telaInicial.btnCadastrarCliente.clicked.connect(lambda: trocaTelas(telaInicial, telaClienteCadastrar))
telaInicial.btnReposicaoCedula.clicked.connect(lambda: trocaTelas(telaInicial, telaReposicaoCedulas))
telaClienteCadastrar.btnMenu.clicked.connect(lambda: trocaTelas(telaClienteCadastrar, telaInicial))
telaClienteEntrar.btnMenu.clicked.connect(lambda: trocaTelas(telaClienteEntrar, telaInicial))
telaReposicaoCedulas.btnMenu.clicked.connect(lambda: trocaTelas(telaReposicaoCedulas, telaInicial))
telaSaque.btnCancelar.clicked.connect(lambda: trocaTelas(telaSaque, telaInicial))
botoesNumericos()

"""
<html><head/><body><p><span style=" color:#6fff91;">Notas inseridas com sucesso!</span></p></body></html>
"""

# Execução do aplicativo
telaInicial.show()
telaSaque.show()

app.exec()
