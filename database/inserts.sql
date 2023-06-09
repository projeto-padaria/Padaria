-- Endereços 
-- *Para a integridade do banco de dados, realize a inserção de Dados na tabela de Endereço e Funcionário diretamente pelo sistema ou insira um endereço por vez acompanhado da inserção de um funcionário devido ao uso do Trigger. Por enquanto não trabalharemos com a conexeão de endereços com clientes e fornecedores pois não será necessária.

insert into padaria.endereco
VALUES
('Red. Vida Nova II', 'Rua A', 123, 'Vinhedo', 'SP', '01234567'),
('Centro', 'Avenida B', 456, 'Rio de Janeiro', 'RJ', '12345678'),
('Savassi', 'Rua C', 789, 'Belo Horizonte', 'MG', '98765432'),
('Moinhos de Vento', 'Avenida D', 101, 'Porto Alegre', 'RS', '54321876'),

-- Funcionario

insert into padaria.funcionario values
('admin', 'Rafael', 'Moreira Cavalcante de Souza', 'admin', 'Desenvolvedor', 0, '19984586252', NULL),
('3456789012', 'Pedro', 'Ferreira', 'senha789', 'Desenvolvedor', 4000.00, '3456789012', NULL),
('45678901234', 'Ana', 'Oliveira', 'senhaabc', 'Secretária', 2500.00, '4567890123', NULL),
('56789012345', 'Carlos', 'Souza', 'senhaxyz', 'Vendedor', 3000.00, '5678901234', NULL);

-- Fornecedor
insert into padaria.fornecedor VALUES
('1234567891234','Ativo','CotucaInBunda','1234567890',NULL),
('4321987654321','Ativo','Nutrivan','56789101415',NULL),
('12345678901234', 'Ativo', 'Empresa A', '1234567890',NULL),
('98765432109876', 'Inativo', 'Empresa B', '9876543210',NULL),
('56789012345678', 'Ativo', 'Empresa C', '5678901234',NULL),
('90123456789012', 'Ativo', 'Empresa F', '9012345678',NULL),
('34567890123456', 'Inativo', 'Empresa G', '3456789012',NULL);

-- Cliente

insert into padaria.cliente VALUES
('João', 'Silva', '12345678901',NULL),
('Maria', 'Santos', '23456789012',NULL),
('Pedro', 'Ferreira', '34567890123',NULL),
('Ana', 'Oliveira', '45678901234',NULL),
('Carlos', 'Souza', '56789012345',NULL),
('Julia', 'Costa', '67890123456',NULL),
('Lucas', 'Gomes', '78901234567',NULL);

-- Produto

insert into padaria.produto VALUES
(1,'Produto A', 'Marca A', 10.00, 100, '2023-05-29', '2024-05-29'),
(1,'Produto B', 'Marca B', 15.50, 50, '2023-05-29', '2024-05-29'),
(2,'Produto C', 'Marca C', 20.99, 80, '2023-05-29', '2024-05-29'),
(2,'Produto D', 'Marca D', 5.99, 200, '2023-05-29', '2024-05-29'),
(3,'Produto E', 'Marca E', 8.75, 150, '2023-05-29', '2024-05-29'),
(4,'Produto F', 'Marca F', 12.49, 120, '2023-05-29', '2024-05-29'),
(7,'Produto G', 'Marca G', 18.00, 90, '2023-05-29', '2024-05-29');

-- Venda - As Vendas devem ser realizadas diretamente pelo sistema.





