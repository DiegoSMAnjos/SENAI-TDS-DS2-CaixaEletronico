CREATE database db_caixa_eletronico;

USE db_caixa_eletronico;

create table tb_voluntario2(
	id int not null auto_increment primary key,
    nome varchar(30),
    idade int,
    genero varchar(100),
    turno varchar(10)
);

describe tb_voluntario2;
select * from tb_voluntario2;
insert into tb_voluntario2 (nome, idade) values ("Maria", 30);
