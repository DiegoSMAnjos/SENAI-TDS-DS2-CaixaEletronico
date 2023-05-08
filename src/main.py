"""
PARTE 1

Para realizar saque otimizado em caixa eletrônico, faça um programa que deverá:

a) mostrar de quais valores são os 3 tipos de cédulas disponíveis no terminal e vigentes na
atualidade.
b) exibir para o usuário três opções de valores pré-definidos, além de permitir que o mesmo
informe o valor desejado.
c) apresentar quantas notas de cada valor serão fornecidas para atender o saque.


PARTE 2

Para manutenção otimizada do saque em caixa eletrônico é necessário tratar reposição de cédulas. Incremente
seu programa para:

a) definir a quantidade de notas de cada célula;
b) notificar a falta de alguma cédula;
c) repor cédula faltante;
d) adicionar cédula de diferente valor.

Dessa vez, especifique os casos de teste.


PARTE 3

A realização de saque em caixa eletrônico deve manter a conformidade com o sacador.
Incremente seu programa para:

a) inserir cliente e seu endereço;
b) autenticar o cliente;
c) atualizar o saldo;

Especifique os casos de testes.


CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO-INCREMENT,


);



"""

from PyQt5 import uic, QtWidgets
from model.Conexao import *


def exibir_tela_01():
    home.btTouch_saque.setVisible(False)
    set_botoes_saque_pre_definidos(False)
    exibir_boas_vindas()
    return


def exibir_boas_vindas():
    home.label_frame_principal.setText("<html><head/><body><p>Olá! Seja bem-vindo(a)!</p>" +
                                       "<p>Escolha a opção desejada abaixo:</p></body></html>")
    home.btTouch_saque.setVisible(True)


def exibir_menu_saque():
    home.btTouch_saque.setVisible(False)
    set_botoes_saque_pre_definidos(True)
    home.label_frame_principal.setText("<html><head/><body><p>Escolha um valor definido ao lado</p>" +
                                       "<p>Ou digite um valor específico no teclado numérico: </p></body></html>")


def set_botoes_saque_pre_definidos(ativo):
    home.btTouch_50.setVisible(ativo)
    home.btTouch_100.setVisible(ativo)
    home.btTouch_150.setVisible(ativo)
    home.btTouch_200.setVisible(ativo)


app = QtWidgets.QApplication([])
home = uic.loadUi("view/home-saque.ui")
# conexao = conectar_banco()

home.show()
exibir_tela_01()

home.btTouch_saque.clicked.connect(exibir_menu_saque)

app.exec()

'''
def cadastrar():
    nome = home.le_nome.text()
    idade = home.le_idade.text()
    genero = home.le_genero.currentText()
    turno = ""
    if home.radioMat.isChecked():
        turno = "Matutino"
    elif home.radioVesp.isChecked():
        turno = "Vespertino"
    elif home.radioNot.isChecked():
        turno = "Noturno"

    cursor = conexao.cursor()
    sql = "insert into tb_voluntario2 (nome, idade, genero, turno) values (%s, %s, %s, %s)"
    entrada = (str(nome), str(idade), str(genero), str(turno))
    cursor.execute(sql, entrada)
    conexao.commit()
    sucesso.show()
    limpar()


def limpar():
    home.le_nome.setText("")
    home.le_idade.setText("")


def listar():
    lista.show()
    lista.list_nome.clear()
    lista.list_idade.clear()
    lista.list_genero.clear()
    cursor = conexao.cursor()
    # sql = "SELECT * FROM tb_voluntario"
    # sql = "SELECT * FROM tb_voluntario ORDER BY nome ASC, idade DESC"
    sql = "SELECT * FROM tb_voluntario2"
    cursor.execute(sql)
    registros = cursor.fetchall()
    # print(registros)
    for linha in registros:
        lista.list_nome.addItem(str(linha[1]))
        lista.list_idade.addItem(str(linha[2]))
        lista.list_genero.addItem(str(linha[3]))
        lista.list_turno.addItem(str(linha[4]))
    conexao.commit()




home.pb_enviar.clicked.connect(cadastrar)
home.pb_lista.clicked.connect(listar)
home.pb_limpar.clicked.connect(limpar)
'''
