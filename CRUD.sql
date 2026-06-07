--CRUD

--CREATE
INSERT INTO fcardb.clientes (
    cpf_cliente, 
    nome_cliente, 
    email_cliente, 
    num_endereco_cliente, 
    cep_endereco_cliente, 
    rua_endereco_cliente
) VALUES ('99988877711','Carlos Eduardo Souza','cadu.souza@email.com','150','01001000','Avenida Paulista');

INSERT INTO fcardb.tel_cliente (cpf_cliente, telefone_cliente) 
VALUES ('99988877711', '(11) 99999-1234');


--READ
SELECT cpf_cliente, nome_cliente, email_cliente 
FROM fcardb.clientes;

SELECT c.nome_cliente, c.email_cliente, t.telefone_cliente
FROM fcardb.clientes c
INNER JOIN fcardb.tel_cliente t ON c.cpf_cliente = t.cpf_cliente;

--UPDATE
UPDATE fcardb.clientes
SET email_cliente = 'joao@novissimoemail.com',
    num_endereco_cliente = 'OUTRO'
WHERE cpf_cliente = '12642900640';

--DELETE
DELETE FROM fcardb.tel_cliente
WHERE cpf_cliente = '12642900640';

DELETE FROM fcardb.clientes
WHERE cpf_cliente = '12642900640';
