-- Endereços

insert into padaria.endereco
VALUES
('Copacabana', 'Avenida B', 456, 'Rio de Janeiro', 'RJ', '12345678'),
('Savassi', 'Rua C', 789, 'Belo Horizonte', 'MG', '98765432'),
('Moinhos de Vento', 'Avenida D', 101, 'Porto Alegre', 'RS', '54321876'),
('Batel', 'Rua E', 222, 'Curitiba', 'PR', '76543210'); 

SELECT * from padaria.funcionario F, padaria.endereco E where F.idEndereco = E.idEndereco;
SELECT F.cpf,F.nome,F.sobrenome,F.senha,F.cargo,F.salario,F.telefone,E.bairro,E.rua,E.numero,E.cidade,E.UF,E.cep FROM padaria.funcionario F,padaria.endereco E WHERE F.idEndereco = E.idEndereco;


select * from padaria.endereco;
select max(idEndereco) from padaria.endereco;


-- Fornecdor
insert into padaria.fornecedor VALUES
('1234567891234','Ativo','CotucaInBunda','1234567890',1),
('4321987654321','Ativo','Nutrivan','56789101415',2),
('12345678901234', 'Ativo', 'Empresa A', '1234567890',3),
('98765432109876', 'Inativo', 'Empresa B', '9876543210',4),
('56789012345678', 'Ativo', 'Empresa C', '5678901234',5),
('90123456789012', 'Ativo', 'Empresa F', '9012345678',6),
('34567890123456', 'Inativo', 'Empresa G', '3456789012',7);

-- Cliente

insert into padaria.cliente VALUES
('João', 'Silva', '12345678901',7),
('Maria', 'Santos', '23456789012',9),
('Pedro', 'Ferreira', '34567890123',10),
('Ana', 'Oliveira', '45678901234',11),
('Carlos', 'Souza', '56789012345',12),
('Julia', 'Costa', '67890123456',13),
('Lucas', 'Gomes', '78901234567',14);

-- Funcionario

insert into padaria.funcionario values
('23456789012', 'Maria', 'Santos', 'senha456', 'Analista', 3500.00, '2345678901', NULL),
('34567890123', 'Pedro', 'Ferreira', 'senha789', 'Desenvolvedor', 4000.00, '3456789012', NULL),
('45678901234', 'Ana', 'Oliveira', 'senhaabc', 'Secretária', 2500.00, '4567890123', NULL),
('56789012345', 'Carlos', 'Souza', 'senhaxyz', 'Vendedor', 3000.00, '5678901234', NULL);

SELECT cpf,senha from padaria.funcionario

SELECT cpf,senha from padaria.funcionario where cpf = '12345678901' and senha = 'senha1243'

select F.cpf+F.idEndereco from padaria.Funcionario F where nome = 'João'
 
-- Produto

insert into padaria.produto VALUES
(1,'Produto A', 'Marca A', 10.00, 100, '2023-05-29', '2024-05-29'),
(1,'Produto B', 'Marca B', 15.50, 50, '2023-05-29', '2024-05-29'),
(2,'Produto C', 'Marca C', 20.99, 80, '2023-05-29', '2024-05-29'),
(2,'Produto D', 'Marca D', 5.99, 200, '2023-05-29', '2024-05-29'),
(3,'Produto E', 'Marca E', 8.75, 150, '2023-05-29', '2024-05-29'),
(4,'Produto F', 'Marca F', 12.49, 120, '2023-05-29', '2024-05-29'),
(7,'Produto G', 'Marca G', 18.00, 90, '2023-05-29', '2024-05-29');

-- Venda

insert into padaria.venda VALUES
(),



