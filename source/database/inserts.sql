-- Endereços

insert into padaria.endereco VALUES 
('BA','Jaguaquara','Rua Doutor Gilberto Rebouças','Muritiba',156,'45345000'),
('SP','Campinas','Vida Boa','Rua Alcides Nogueira'
,88,'45345000'),
('SP','Vinhedo','Capela','Rua do Café',96,'75846958'),
('SP','Campinas','Centro','Rua Culto à Ciência',45,'13020060'),
('SP','Campinas','Centro','Praca Comendador Soares',141,'13015030'),
('SP','Vinhedo','Capela','Rua Nossa Sra. de Lourdes',87,'13280000'),
('SP','Campinas','Jardim Chapadão','Av. Andrade Neves',448,'13070000');

INSERT INTO padaria.endereco
VALUES 
('SP', 'São Paulo', 'Centro', 'Rua A', 123, '01234547'),
('RJ', 'Rio de Janeiro', 'Copacabana', 'Avenida B', 456, '12345678'),
('MG', 'Belo Horizonte', 'Savassi', 'Rua C', 789, '98765432'),
('RS', 'Porto Alegre', 'Moinhos de Vento', 'Avenida D', 101, '54321876'),
('PR', 'Curitiba', 'Batel', 'Rua E', 222, '76543210'),
('SC', 'Florianópolis', 'Centro', 'Avenida F', 333, '45678901'),
('BA', 'Salvador', 'Barra', 'Rua G', 444, '23456789'),
('PE', 'Recife', 'Boa Viagem', 'Avenida H', 555, '65432109'),
('CE', 'Fortaleza', 'Meireles', 'Rua I', 666, '34567890'),
('AM', 'Manaus', 'Adrianópolis', 'Avenida J', 777, '87654321'),
('GO', 'Goiânia', 'Setor Bueno', 'Rua K', 888, '56789012'),
('MT', 'Cuiabá', 'Centro Sul', 'Avenida L', 999, '54321098'),
('ES', 'Vitória', 'Jardim Camburi', 'Rua M', 111, NULL),
('BA', 'Salvador', 'Pelourinho', 'Rua N', 222, NULL);

select * from padaria.endereco

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
('João', 'Silva', 'Gerente', '1234567890', 5000.00, '12345678901',15),
('Maria', 'Santos', 'Analista', '2345678901', 3500.00, '23456789012',16),
('Pedro', 'Ferreira', 'Desenvolvedor', '3456789012', 4000.00, '34567890123',17),
('Ana', 'Oliveira', 'Secretária', '4567890123', 2500.00, '45678901234',18),
('Carlos', 'Souza', 'Vendedor', '5678901234', 3000.00, '56789012345',19),
('Julia', 'Costa', 'Assistente', '6789012345', 2800.00, '67890123456',20),
('Lucas', 'Gomes', 'Estagiário', '7890123456', 2000.00, '78901234567',21);
 
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




