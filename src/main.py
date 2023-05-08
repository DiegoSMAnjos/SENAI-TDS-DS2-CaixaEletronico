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


home = uic.loadUi('src/view/home-saque.ui')

app = QtWidgets.QApplication([])
home.show()
# conexao = conectar_banco()


exibir_tela_01()

home.btTouch_saque.clicked.connect(exibir_menu_saque)

app.exec()
