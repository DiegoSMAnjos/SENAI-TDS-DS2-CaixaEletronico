CREATE database db_caixa_eletronico;

USE db_caixa_eletronico;

create table tabela_parte01 (
	id int not null auto_increment primary key,
    data_transacao date,
    valor float
);