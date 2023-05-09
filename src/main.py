from PyQt5 import uic, QtWidgets
from model.Conexao import *
from src.model.Funcoes import *

# Carregamento do aplicativo
app = QtWidgets.QApplication([])
telaInicial = uic.loadUi('src/view/telaInicial.ui')
telaSaque = uic.loadUi('src/view/telaSaque.ui')
telaClienteEntrar = uic.loadUi('src/view/telaClienteEntrar.ui')
telaClienteCadastrar = uic.loadUi('src/view/telaClienteCadastrar.ui')
telaReposicaoCedulas = uic.loadUi('src/view/telaReposicaoCedulas.ui')

# Conexao com o banco de dados
conn = conectar_banco()

telaInicial.show()

# Navegação entre Telas

telaInicial.btMenuSaque.clicked.connect(abrirTelaSaque)
telaInicial.btMenuSaque.clicked.connect(abrirTelaSaque)
telaSaque.btnCancelar.clicked.connect(abrirTelaInicial)

# Execução do aplicativo
app.exec()
