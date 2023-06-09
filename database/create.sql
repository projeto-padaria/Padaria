-- Está em ordem de criação das tabelas e relacionamentos

create schema padaria;

create table padaria.endereco
(
    idEndereco int identity(1,1),
    bairro varchar(100)  null,
    rua varchar(100)  null,
    numero int  null,
    cidade varchar(50)  null,
    UF char(2)  null,
    cep varchar(8)  null,
    PRIMARY KEY (idEndereco)
);


create table  padaria.fornecedor
(
    idFornecedor int identity(1,1),

    cnpj varchar(14),
    status varchar(50),
    nome varchar(50),
    telefone char(11),
    idEndereco int null,
    UNIQUE(cnpj),
    PRIMARY KEY (idFornecedor),

    FOREIGN KEY (idEndereco) REFERENCES padaria.endereco(idEndereco) on update CASCADE
);

create table  padaria.cliente
(
    idCliente int identity(1,1),

    nome varchar(50),
    sobrenome varchar(50),
    cpf varchar(11),
    idEndereco int  null,
    UNIQUE(cpf),
    PRIMARY KEY (idCliente),

    FOREIGN KEY (idEndereco) REFERENCES padaria.endereco(idEndereco) on update CASCADE
);

create table  padaria.funcionario
(
    idFuncionario int identity(1,1),

    cpf varchar(11),
    nome varchar(50),
    sobrenome varchar(50),
    senha varchar(40),
    cargo varchar(50),
    salario decimal(10,2),
    telefone varchar(11),
    idEndereco int null,
    UNIQUE(cpf),

    PRIMARY KEY (idFuncionario),

    FOREIGN KEY (idEndereco) REFERENCES padaria.endereco(idEndereco) on update CASCADE
);

create table  padaria.produto
(
    idProduto int identity(1,1),
    idFornecedor int ,

    nome varchar(50),
    marca varchar(50),
    preco decimal(10,2),
    quantidade int,
    datadeemissao date,
    datadevalidade date,
    UNIQUE(nome),

    PRIMARY KEY (idProduto),

    FOREIGN KEY (idFornecedor) REFERENCES padaria.fornecedor(idFornecedor) on update CASCADE
);

create table  padaria.venda
(
    idVenda int,
    idCliente int,
    idProduto int,
    idFuncionario int,

    quantidade int,
    data datetime,  

    PRIMARY KEY (idVenda, idCliente, idFuncionario, idProduto,data),

    FOREIGN KEY (idCliente) REFERENCES padaria.cliente(idCliente) on update CASCADE,

    FOREIGN KEY (idFuncionario) REFERENCES padaria.funcionario(idFuncionario) on update NO ACTION,
    
    FOREIGN KEY (idProduto) REFERENCES padaria.produto(idProduto) on update NO ACTION,

)

--  >Dever ser criado após a criação das outras tabelas<
-- Sempre que um valor for adicionado na Tabela funcionario, o seu endereço será linkado com o último endereço registrado na tabela endereço.
CREATE TRIGGER padaria.AtualizarUltimoValorEndereco ON padaria.funcionario
AFTER INSERT
AS
BEGIN
    DECLARE @UltimoValor VARCHAR(50);
    
    SELECT @UltimoValor = idEndereco
    FROM padaria.endereco
    WHERE idEndereco = (SELECT MAX(idEndereco) FROM padaria.endereco);
    
    UPDATE padaria.funcionario
    SET idEndereco = @UltimoValor
    FROM inserted
    WHERE padaria.funcionario.idFuncionario = inserted.idFuncionario;
END
