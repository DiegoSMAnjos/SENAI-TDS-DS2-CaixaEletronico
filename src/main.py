from PyQt5 import uic, QtWidgets
from model.Conexao import *

# Infos do cliente logado = [idCliente, emailCliente, senhaCliente, enderecoCliente, saldoCliente]
clienteSelecionado = [0, "", "", "", 0]

# Carregamento do aplicativo

app = QtWidgets.QApplication([])
telaInicial = uic.loadUi('view/telaInicial.ui')
telaSaqueDeposito = uic.loadUi('view/telaSaqueDeposito.ui')
telaClienteEntrar = uic.loadUi('view/telaClienteEntrar.ui')
telaClienteCadastrar = uic.loadUi('view/telaClienteCadastrar.ui')
telaReposicaoCedulas = uic.loadUi('view/telaReposicaoCedulas.ui')
telaSucessoOperacao = uic.loadUi('view/telaSucessoOperacao.ui')
telaInsucessoOperacao = uic.loadUi('view/telaInsucessoOperacao.ui')

# Conexao com o banco de dados

conn = conectar_banco()


# Definições de Funções
def calcularNotas(valorSaque, qtdNotas5, qtdNotas10, qtdNotas20):
    notas20 = min(valorSaque // 20, qtdNotas20)
    valorSaque -= notas20 * 20

    notas10 = min(valorSaque // 10, qtdNotas10)
    valorSaque -= notas10 * 10

    notas5 = min(valorSaque // 5, qtdNotas5)

    return notas5, notas10, notas20


def validaLogin():
    email = telaClienteEntrar.campoEmail.text()
    senha = telaClienteEntrar.campoSenha.text()
    cursor = conn.cursor()
    sql = "SELECT * FROM cliente WHERE email = %s AND senha = %s"
    entrada = (str(email), str(senha))
    cursor.execute(sql, entrada)
    registros = cursor.fetchall()

    conn.commit()
    if len(registros) == 0:
        telaClienteEntrar.lblMensagem.setText("<html><head/><body><p><span style=\" color:#f06464;\">Cliente não "
                                              "encontrado!</span></p></body></html>")
    else:
        # limpa dados
        telaClienteEntrar.campoEmail.setText("")
        telaClienteEntrar.campoSenha.setText("")
        telaClienteEntrar.lblMensagem.setText("")
        # armazena temporariamente os dados do cliente autenticado
        clienteSelecionado[0] = registros[0][0]  # idCliente
        clienteSelecionado[1] = registros[0][1]  # email
        clienteSelecionado[2] = registros[0][2]  # senha
        clienteSelecionado[3] = registros[0][3]  # endereco
        clienteSelecionado[4] = registros[0][4]  # saldo
        trocaTelas(telaClienteEntrar, telaSaqueDeposito)
        telaSaqueDeposito.label.setText(f"<html><head/><body><p>SALDO ATUAL: <b>{clienteSelecionado[4]}</b></p><p "
                                        f"align=\"center\"><span style=\""
                                        f"font-size:10pt;\">NOTAS DISPONÍVEIS PARA SAQUE:</span></p><p "
                                        f"align=\"center\"><span style=\" font-size:10pt;\">R$ 5,00 | R$ 10,"
                                        f"00 | R$ 20,00</span></p></body></html>")


def efetuaOperacao():
    if telaSaqueDeposito.lineEditValor.text() == "":
        valorOp = 0
    else:
        valorOp = int(telaSaqueDeposito.lineEditValor.text())

    # Tipo = Saque
    if telaSaqueDeposito.rbSaque.isChecked():
        saldoAtual = clienteSelecionado[4]
        if valorOp > saldoAtual:
            telaSaqueDeposito.lineEditValor.setText("")
            telaInsucessoOperacao.lblMenu.setText("Seu saldo é insuficiente para o saque! Deseja tentar novamente?")
            trocaTelas(telaSaqueDeposito, telaInsucessoOperacao)
        else:
            # verifica disponibilidade de notas
            notas5, notas10, notas20 = 0, 0, 0
            cursor = conn.cursor()
            sql = "SELECT * FROM nota;"
            cursor.execute(sql)
            registros = cursor.fetchall()
            for registro in registros:
                if registro[1] == 5.00:
                    notas5 = int(registro[2])
                elif registro[1] == 10.00:
                    notas10 = int(registro[2])
                elif registro[1] == 20.00:
                    notas20 = int(registro[2])
            totalNotas = (notas5 * 5) + (notas10 * 10) + (notas20 * 20)
            if totalNotas < valorOp:
                telaInsucessoOperacao.lblMenu.setText("O caixa não dispõe de notas o suficiente para realizar o "
                                                      "saque. Entre em contato com o administrador. Deseja realizar "
                                                      "outra operação?")
                trocaTelas(telaSaqueDeposito, telaInsucessoOperacao)
            else:
                resultNotas5, resultNotas10, resultNotas20 = calcularNotas(valorOp, notas5, notas10, notas20)
                cursor = conn.cursor()
                sql = "UPDATE nota SET quantidade = %s WHERE valor = %s;"
                entrada = (str(notas5 - resultNotas5), str(5.00))
                cursor.execute(sql, entrada)
                entrada = (str(notas10 - resultNotas10), str(10.00))
                cursor.execute(sql, entrada)
                entrada = (str(notas20 - resultNotas20), str(20.00))
                cursor.execute(sql, entrada)
                conn.commit()
                valorAReceber = (resultNotas5 * 5) + (resultNotas10 * 10) + (resultNotas20 * 20)
                telaSucessoOperacao.lblMenu.setText(
                    f"Saque realizado com sucesso! Você receberá: {resultNotas5} notas de R$ 5.00, {resultNotas10} notas de R$ 10.00 e {resultNotas20} notas de R$ 20.00. Total: R$ {valorAReceber}.00. Deseja realizar outra operação?")
                clienteSelecionado[4] = saldoAtual - valorAReceber
                cursor = conn.cursor()
                sql = "UPDATE cliente SET saldo = %s WHERE id = %s;"
                entrada = (str(clienteSelecionado[4]), str(clienteSelecionado[0]))
                cursor.execute(sql, entrada)
                conn.commit()
                telaSaqueDeposito.label.setText(
                    f"<html><head/><body><p><b>SALDO ATUAL:</b> <b>{clienteSelecionado[4]}</b></p><p "
                    f"align=\"center\"><span style=\""
                    f"font-size:10pt;\">NOTAS DISPONÍVEIS PARA SAQUE:</span></p><p "
                    f"align=\"center\"><span style=\" font-size:10pt;\">R$ 5,00 | R$ 10,"
                    f"00 | R$ 20,00</span></p></body></html>")
                trocaTelas(telaSaqueDeposito, telaSucessoOperacao)


    # Tipo = Depósito
    elif telaSaqueDeposito.rbDeposito.isChecked():
        telaSaqueDeposito.lineEditValor.setText("")
        clienteSelecionado[4] = int(clienteSelecionado[4]) + valorOp
        cursor = conn.cursor()
        sql = "UPDATE cliente SET saldo = %s WHERE id = %s;"
        entrada = (str(clienteSelecionado[4]), str(clienteSelecionado[0]))
        cursor.execute(sql, entrada)
        conn.commit()
        telaSucessoOperacao.lblMenu.setText("Depósito realizado com sucesso! Deseja realizar outra operação?")
        telaSaqueDeposito.label.setText(
            f"<html><head/><body><p><b>SALDO ATUAL:</b> <b>{clienteSelecionado[4]}</b></p><p "
            f"align=\"center\"><span style=\""
            f"font-size:10pt;\">NOTAS DISPONÍVEIS PARA SAQUE:</span></p><p "
            f"align=\"center\"><span style=\" font-size:10pt;\">R$ 5,00 | R$ 10,"
            f"00 | R$ 20,00</span></p></body></html>")
        trocaTelas(telaSaqueDeposito, telaSucessoOperacao)


def insereCliente():
    emailNovoCliente = telaClienteCadastrar.campoEmail.text()
    senhaNovoCliente = telaClienteCadastrar.campoSenha.text()
    repeteSenhaNovoCliente = telaClienteCadastrar.campoSenhaRep.text()
    enderecoNovoCliente = telaClienteCadastrar.campoEndereco.text()

    if emailNovoCliente == "" or senhaNovoCliente == "" or repeteSenhaNovoCliente == "" or enderecoNovoCliente == "":
        telaClienteCadastrar.lblMensagemErro.setText("Insira campos válidos!")
    elif senhaNovoCliente != repeteSenhaNovoCliente:
        telaClienteCadastrar.lblMensagemErro.setText("As senhas não conferem!")
    else:
        # Verifica se cliente já está cadastrado
        cursor = conn.cursor()
        sql = "SELECT email, senha FROM cliente where email = %s;"
        entrada = (str(emailNovoCliente),)
        cursor.execute(sql, entrada)
        registros = cursor.fetchall()
        conn.commit()

        if len(registros) > 0:
            if registros[0][0] == emailNovoCliente:
                telaClienteCadastrar.lblMensagemErro.setText("Este cliente já está cadastrado!")
        # cadastra novo cliente
        else:
            telaClienteCadastrar.lblMensagemErro.setText(f"Cliente {emailNovoCliente} cadastrado!")
            telaClienteCadastrar.campoEmail.setText("")
            telaClienteCadastrar.campoSenha.setText("")
            telaClienteCadastrar.campoSenhaRep.setText("")
            telaClienteCadastrar.campoEndereco.setText("")
            cursor = conn.cursor()
            sql = "INSERT IGNORE INTO cliente (email, senha, endereco, saldo) VALUES (%s,%s,%s,0.00);"
            entrada = (str(emailNovoCliente), str(senhaNovoCliente), str(enderecoNovoCliente))
            cursor.execute(sql, entrada)
            conn.commit()


# exibe para o ADM a quantidade atual de cédulas
def getQtdCedulas():
    notas5, notas10, notas20 = 0, 0, 0
    cursor = conn.cursor()
    sql = "SELECT * FROM nota;"
    cursor.execute(sql)
    registros = cursor.fetchall()
    for registro in registros:
        if registro[1] == 5.00:
            notas5 = int(registro[2])
        elif registro[1] == 10.00:
            notas10 = int(registro[2])
        elif registro[1] == 20.00:
            notas20 = int(registro[2])
    return f"<html><head/><body><p>Quantidade atual</p><p>R$ 5.00 = {notas5}</p><p>R$ 10.00 = {notas10}</p><p>R$ " \
           f"20.00 = {notas20}</p></body></html>"


def repoeCedulas():
    tipoCedula = telaReposicaoCedulas.cbTipoCedula.currentText()
    # caso o campo quantidade não tenha uma entrada válida (ex.: 124nadu9v23):
    try:
        qtdCedulas = int(telaReposicaoCedulas.campoQuantidade.text())
        cursor = conn.cursor()
        sql = "SELECT quantidade FROM nota WHERE valor = %s;"
        entrada = (str(tipoCedula),)
        cursor.execute(sql, entrada)
        registros = cursor.fetchall()
        conn.commit()
        novoValor = int(registros[0][0]) + int(qtdCedulas)
        sql = "UPDATE nota SET quantidade = %s WHERE valor = %s;"
        entrada = (str(novoValor), str(tipoCedula))
        cursor.execute(sql, entrada)
        conn.commit()
        telaReposicaoCedulas.lblMensagem.setText(getQtdCedulas())
    except:
        telaReposicaoCedulas.campoQuantidade.setText("")


def trocaTelas(tela01, tela02):
    tela01.close()
    tela02.show()


def addValor(numero):
    telaSaqueDeposito.lineEditValor.setText(telaSaqueDeposito.lineEditValor.text() + str(numero))


def addValorFixo(numero):
    telaSaqueDeposito.lineEditValor.setText(str(numero))


def removeValor():
    telaSaqueDeposito.lineEditValor.setText(telaSaqueDeposito.lineEditValor.text()[:-1])


# Operações e botões

telaSaqueDeposito.btnNum0.clicked.connect(lambda: addValor(0))
telaSaqueDeposito.btnNum1.clicked.connect(lambda: addValor(1))
telaSaqueDeposito.btnNum2.clicked.connect(lambda: addValor(2))
telaSaqueDeposito.btnNum3.clicked.connect(lambda: addValor(3))
telaSaqueDeposito.btnNum4.clicked.connect(lambda: addValor(4))
telaSaqueDeposito.btnNum5.clicked.connect(lambda: addValor(5))
telaSaqueDeposito.btnNum6.clicked.connect(lambda: addValor(6))
telaSaqueDeposito.btnNum7.clicked.connect(lambda: addValor(7))
telaSaqueDeposito.btnNum8.clicked.connect(lambda: addValor(8))
telaSaqueDeposito.btnNum9.clicked.connect(lambda: addValor(9))
telaSaqueDeposito.btnCorrigir.clicked.connect(lambda: removeValor())
telaSaqueDeposito.btnTouch50.clicked.connect(lambda: addValorFixo(50))
telaSaqueDeposito.btnTouch100.clicked.connect(lambda: addValorFixo(100))
telaSaqueDeposito.btnTouch150.clicked.connect(lambda: addValorFixo(150))
telaClienteEntrar.btnLogin.clicked.connect(lambda: validaLogin())
telaSaqueDeposito.btnEntrar.clicked.connect(lambda: efetuaOperacao())
telaClienteCadastrar.btnCadastrar.clicked.connect(lambda: insereCliente())
telaReposicaoCedulas.lblMensagem.setText(getQtdCedulas())
telaReposicaoCedulas.btnRepor.clicked.connect(lambda: repoeCedulas())

# Navegação entre Telas

telaInicial.btnEntrarCliente.clicked.connect(lambda: trocaTelas(telaInicial, telaClienteEntrar))
telaInicial.btnCadastrarCliente.clicked.connect(lambda: trocaTelas(telaInicial, telaClienteCadastrar))
telaInicial.btnReposicaoCedula.clicked.connect(lambda: trocaTelas(telaInicial, telaReposicaoCedulas))
telaClienteCadastrar.btnMenu.clicked.connect(lambda: trocaTelas(telaClienteCadastrar, telaInicial))
telaClienteEntrar.btnMenu.clicked.connect(lambda: trocaTelas(telaClienteEntrar, telaInicial))
telaReposicaoCedulas.btnMenu.clicked.connect(lambda: trocaTelas(telaReposicaoCedulas, telaInicial))
telaSaqueDeposito.btnCancelar.clicked.connect(lambda: trocaTelas(telaSaqueDeposito, telaInicial))
telaSucessoOperacao.btnSim.clicked.connect(lambda: trocaTelas(telaSucessoOperacao, telaSaqueDeposito))
telaSucessoOperacao.btnNao.clicked.connect(lambda: trocaTelas(telaSucessoOperacao, telaInicial))
telaInsucessoOperacao.btnSim.clicked.connect(lambda: trocaTelas(telaInsucessoOperacao, telaSaqueDeposito))
telaInsucessoOperacao.btnNao.clicked.connect(lambda: trocaTelas(telaInsucessoOperacao, telaInicial))


# Execução do aplicativo
telaInicial.show()

app.exec()
