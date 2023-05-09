from PyQt5 import uic

from src.main import telaInicial, telaSaque


def abrirTelaSaque():
    telaInicial.close()
    telaSaque.show()


def abrirTelaInicial():
    telaSaque.close()
    telaInicial.show()