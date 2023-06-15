-- Está em ordem de criação das tabelas e relacionamentos
-- Caso algum cabaço faça merda. NÃO ALTERE A ORDEM DAS TABELAS

-- create schema padaria

create table padaria.endereco
(
    idEndereco int identity(1,1),

    estado char(2),
    cidade varchar(45),
    bairro varchar(50),
    rua varchar(25),
    numero int,
    cep int null,

    PRIMARY KEY (idEndereco)
)

create table padaria.fornecedor
(
    idFornecedor int identity(1,1),

    cnpj int,
    status varchar(50),
    nome varchar(50),
    nomefantasia varchar(50),
    telefone int,
    idEndereco int,
    PRIMARY KEY (idFornecedor),

    FOREIGN KEY (idEndereco) REFERENCES padaria.endereco(idEndereco)
)

create table padaria.cliente
(
    idCliente int identity(1,1),

    nome varchar(25) null,
    sobrenome varchar(35) null,
    cpf int null,
    idEndereco int null,
    PRIMARY KEY (idCliente),

    FOREIGN KEY (idEndereco) REFERENCES padaria.endereco(idEndereco)
)

create table padaria.funcionario
(
    idFuncionario int identity(1,1),

    nome varchar(25),
    sobrenome varchar(35),
    cargo varchar(50),
    telefone int,
    salario decimal(10,2),
    cpf int UNIQUE,
    senha varchar(50),
    idEndereco int,
    senha varchar(50),

    PRIMARY KEY (idFuncionario),

    FOREIGN KEY (idEndereco) REFERENCES padaria.endereco(idEndereco)
)

create table padaria.produto
(
    idProduto int identity(1,1),
    idFornecedor int ,

    nome varchar(25),
    marca varchar(25),
    preco decimal(10,2),
    quantidade int,
    datadeemissao date,
    datadevalidade date,

    PRIMARY KEY (idProduto),

    FOREIGN KEY (idFornecedor) REFERENCES padaria.fornecedor(idFornecedor)
)

create table padaria.venda
(
    idVenda int identity(1,1),
    idCliente int,
    idProduto int,
    idFuncionario int,
    idFornecedor int,

    data date,
    entrega_tipo varchar(50) null,
    forma_pagamento varchar(50),
    valor_total decimal(10,2),

    PRIMARY KEY (idVenda, idCliente, idFuncionario, idProduto),

    FOREIGN KEY (idCliente) REFERENCES padaria.cliente(idCliente),
    FOREIGN KEY (idFuncionario) REFERENCES padaria.funcionario(idFuncionario),
    FOREIGN KEY (idProduto) REFERENCES padaria.produto(idProduto),
    FOREIGN KEY (idFornecedor) REFERENCES padaria.fornecedor(idFornecedor)
)

SELECT CPF FROM padaria.funcionario WHERE CPF = 12345678901