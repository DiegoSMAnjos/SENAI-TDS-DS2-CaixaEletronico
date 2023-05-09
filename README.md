# Sistema de Caixa Eletrônico com PyQt5 e MySQL - Demo
 


-[ ] TODO  


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
    email VARCHAR(50),
    senha VARCHAR(20),
    saldo FLOAT,
    endereco VARCHAR(50)
);

