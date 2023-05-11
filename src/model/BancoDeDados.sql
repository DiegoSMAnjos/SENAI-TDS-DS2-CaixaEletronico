CREATE database IF NOT EXISTS db_caixa_eletronico;

USE db_caixa_eletronico;

CREATE TABLE IF NOT EXISTS cliente (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50),
    senha VARCHAR(50),
    endereco VARCHAR(100),
    saldo FLOAT
);

CREATE TABLE IF NOT EXISTS nota (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    valor FLOAT,
    quantidade INT
);

INSERT IGNORE INTO nota VALUES (1,5.00,20);
INSERT IGNORE INTO nota VALUES (2,10.00,20);
INSERT IGNORE INTO nota VALUES (3,20.00,20);
INSERT IGNORE INTO cliente VALUES (1,"diegoanjos@gmail.com","1234","Rua ABC, 123", 50.00);
INSERT IGNORE INTO cliente VALUES (2,"grasi.rda@gmail.com","1234","Rua DEF, 456", 100.00);