-- Desabilitar as restrições de chave estrangeira temporariamente
ALTER TABLE padaria.venda NOCHECK CONSTRAINT ALL;
ALTER TABLE padaria.produto NOCHECK CONSTRAINT ALL;
ALTER TABLE padaria.funcionario NOCHECK CONSTRAINT ALL;
ALTER TABLE padaria.cliente NOCHECK CONSTRAINT ALL;
ALTER TABLE padaria.fornecedor NOCHECK CONSTRAINT ALL;
ALTER TABLE padaria.endereco NOCHECK CONSTRAINT ALL;

-- Exclusão dos dados da tabela padaria.venda
DELETE FROM padaria.venda;

-- Exclusão dos dados da tabela padaria.produto
DELETE FROM padaria.produto;

-- Exclusão dos dados da tabela padaria.funcionario
DELETE FROM padaria.funcionario;

-- Exclusão dos dados da tabela padaria.cliente
DELETE FROM padaria.cliente;

-- Exclusão dos dados da tabela padaria.fornecedor
DELETE FROM padaria.fornecedor;

-- Exclusão dos dados da tabela padaria.endereco
DELETE FROM padaria.endereco;

-- Habilitar as restrições de chave estrangeira novamente
ALTER TABLE padaria.venda WITH CHECK CHECK CONSTRAINT ALL;
ALTER TABLE padaria.produto WITH CHECK CHECK CONSTRAINT ALL;
ALTER TABLE padaria.funcionario WITH CHECK CHECK CONSTRAINT ALL;
ALTER TABLE padaria.cliente WITH CHECK CHECK CONSTRAINT ALL;
ALTER TABLE padaria.fornecedor WITH CHECK CHECK CONSTRAINT ALL;
ALTER TABLE padaria.endereco WITH CHECK CHECK CONSTRAINT ALL;
