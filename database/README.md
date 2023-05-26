# PADARIA: - Bakery

Explicando como vai funcionar a nossa padaria, basicamente ela vai ter um sistema curto para registro de caixa eletronico, além de outro sistema que ira funcionar caso foi algo relacionado a entregas.

> Para isso foi criado essas tabelas a baixo a seguir

## Tabela de Venda

Na tabela de vendas vai ter o registro de todas as vendas que foram feitas na padaria, com o nome do cliente, o produto que foi comprado, a quantidade, o valor total da compra, a data e o horario que foi feito a compra.

| idVenda | idCliente | idProduto | idfuncionario | idfornecedor | quantidade | valor_total | data_venda | hora_venda |

## Tabela de Cliente

Na tabela de cliente vai ter o registro de todos os clientes que compraram na padaria, com o nome, o cpf, o telefone, o endereço e o email.

| idCliente | nome | sobrenome | cpf_cliente | telefone_cliente | idEndereco

## Tabela de Produto

Na tabela de produto vai ter o registro de todos os produtos que foram vendidos na padaria, com o nome do produto, a quantidade, o valor unitario, o valor total, a data e o horario que foi feito a compra.

| idProduto | nome_produto | quantidade | valor_unitario | valor_total | data_compra | hora_compra |

## Tabela de Funcionario

Na tabela de funcionario vai ter o registro de todos os funcionarios que trabalham na padaria, com o nome, o cpf, o telefone, o endereço e o email.

| idFuncionario | nome | sobrenome | cpf_funcionario | telefone_funcionario | idEndereco |

## Tabela de Fornecedor

Na tabela de fornecedor vai ter o registro de todos os fornecedores que fornecem produtos para a padaria, com o nome, o cpf, o telefone, o endereço e o email.

| idFornecedor | nome | sobrenome | cpf_fornecedor | telefone_fornecedor | idEndereco |

## Tabela de Endereço

Na tabela de endereço vai ter o registro de todos os endereços que foram cadastrados na padaria, com o nome da rua, o numero da casa, o bairro, a cidade, o estado e o cep.

| idEndereco | rua | numero | bairro | cidade | estado | cep |

# 🤝 Colaboradores

Participação dos alunos dentro do Projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/RMCSa">
        <img src="https://avatars.githubusercontent.com/u/125597354?v=4" width="100px;" alt="Foto do Rafael Moreira no GitHub"/><br>
        <sub>
          <b>Rafael Moreira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Polabiel">
        <img src="https://avatars.githubusercontent.com/u/40695127?v=4" width="100px;" alt="Foto do Gabriel Oliveira"/><br>
        <sub>
          <b>Gabriel Oliveira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/PEDRO160126">
        <img src="https://avatars.githubusercontent.com/u/125505087?v=4" width="100px;" alt="Foto do Pedro Henrique"/><br>
        <sub>
          <b>Pedro Henrique</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LucasSiq12">
        <img src="https://avatars.githubusercontent.com/u/125694952?v=4" width="100px;" alt="Foto do Lucas Siqueira"/><br>
        <sub>
          <b>Lucas Siqueira</b>
        </sub>
      </a>
    </td>
  </tr>
</table>