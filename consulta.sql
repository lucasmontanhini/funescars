--Consultas

--1: Lista de clientes por rua
SELECT i.nome_cliente, i.email_cliente, t.telefone_cliente
FROM fcardb.clientes i
INNER JOIN fcardb.tel_cliente t on i.cpf_cliente = t.cpf_cliente
WHERE rua_endereco_cliente = 'Avenida Paulista'
ORDER BY nome_cliente ASC;

--2: Veiculos por categoria
SELECT placa_veiculo, modelo_veiculo, cor_veiculo, categoria_veiculo, status_veiculo
FROM fcardb.veiculos
WHERE status_veiculo = 'DISPONIVEL'
ORDER BY categoria_veiculo ASC;

--3 Funcionarios com salários altos
SELECT nome_funcionario, cargo_funcionario, sal_funcionario
FROM fcardb.funcionarios
WHERE sal_funcionario > 5000.00
ORDER BY sal_funcionario DESC;

--4 Veículos SUV ou SEDAN a Combustível Elétrico ou Flex
SELECT placa_veiculo, modelo_veiculo, categoria_veiculo, combustivel_veiculo
FROM fcardb.veiculos
WHERE categoria_veiculo IN ('SUV', 'SEDAN') 
  AND combustivel_veiculo IN ('ELETRICO', 'GASOLINA')
ORDER BY modelo_veiculo ASC;

--5 Busca por domínio de email
SELECT cpf_cliente, nome_cliente, email_cliente
FROM fcardb.clientes
WHERE email_cliente LIKE '%@exemplo.com'
ORDER BY nome_cliente DESC;

--6 Contratacao recente
SELECT nome_funcionario, cargo_funcionario, contratacao_func
FROM fcardb.funcionarios
WHERE contratacao_func >= '2020-01-01'
ORDER BY contratacao_func DESC;

--7 Locacao de alto valor
SELECT c.id_locacao, c.placa_veiculo, c.valor_locacao, i.nome_cliente
FROM fcardb.locacao c
inner join fcardb.clientes i on c.cpf_cliente = i.cpf_cliente
WHERE valor_locacao BETWEEN 1500.00 AND 4000.00
ORDER BY valor_locacao DESC;

--8 Locacoes ainda nao finalizadas
SELECT id_locacao, cpf_cliente, placa_veiculo, data_inicio, data_fim
FROM fcardb.locacao
WHERE data_fim IS NULL
ORDER BY data_inicio ASC;

--9 Historico de vistorias reprovadas
SELECT i.id_vistoria, i.placa_veiculo, i.data_vistoria, i.laudo_vistoria, v.modelo_veiculo, v.status_veiculo
FROM fcardb.vistoria i
inner join fcardb.veiculos v on i.placa_veiculo = v.placa_veiculo
WHERE laudo_vistoria LIKE '%REPROVADO%'
ORDER BY data_vistoria DESC;

--10 Funcionarios por unidade
SELECT nome_funcionario, cargo_funcionario, sal_funcionario, id_unidade
FROM fcardb.funcionarios
WHERE id_unidade = 1 
  AND cargo_funcionario IN ('Atendente', 'Vendedor')
ORDER BY sal_funcionario ASC;