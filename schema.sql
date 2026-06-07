create schema if not exists fcardb;

CREATE TABLE fcardb.unidade (
    id_unidade       SERIAL PRIMARY KEY,
    telefone_unidade VARCHAR(15),
    numero_endereco  VARCHAR(5),
    cep_endereco     CHAR(8),
    rua_endereco     VARCHAR(50)
);

CREATE TABLE fcardb.clientes (
    cpf_cliente          CHAR(11)    NOT NULL PRIMARY KEY,
    nome_cliente         VARCHAR(50) NOT NULL,
    email_cliente        VARCHAR(50),
    num_endereco_cliente VARCHAR(5)  NOT NULL,
    cep_endereco_cliente CHAR(8)     NOT NULL,
    rua_endereco_cliente VARCHAR(40) NOT NULL
);

CREATE TABLE fcardb.tel_cliente (
    cpf_cliente      CHAR(11)    NOT NULL,
    telefone_cliente VARCHAR(15) NOT NULL,
    PRIMARY KEY (cpf_cliente, telefone_cliente),
    FOREIGN KEY (cpf_cliente) REFERENCES fcardb.clientes(cpf_cliente)
);

CREATE TABLE fcardb.funcionarios (
    cpf_funcionario   CHAR(11)      NOT NULL PRIMARY KEY,
    nome_funcionario  VARCHAR(50)   NOT NULL,
    email_funcionario VARCHAR(50)   NOT NULL,
    cargo_funcionario VARCHAR(20)   NOT NULL,
    sal_funcionario   DECIMAL(7,2)  NOT NULL,
    contratacao_func  DATE DEFAULT CURRENT_DATE,
    id_unidade        INTEGER NOT NULL,
    FOREIGN KEY (id_unidade) REFERENCES fcardb.unidade(id_unidade)
);

CREATE TABLE fcardb.tel_funcionarios (
    cpf_funcionario      CHAR(11)    NOT NULL,
    telefone_funcionario VARCHAR(15) NOT NULL,
    PRIMARY KEY (cpf_funcionario, telefone_funcionario),
    FOREIGN KEY (cpf_funcionario) REFERENCES fcardb.funcionarios(cpf_funcionario)
);

CREATE TABLE fcardb.mecanicos (
    cpf_mecanico      CHAR(11)    NOT NULL PRIMARY KEY,
    nome_mecanico     VARCHAR(50) NOT NULL,
    telefone_mecanico VARCHAR(15) NOT NULL,
    empresa_mecanico  VARCHAR(40) NOT NULL,
    id_unidade        INTEGER NOT NULL,
    FOREIGN KEY (id_unidade) REFERENCES fcardb.unidade(id_unidade)
);

CREATE TABLE fcardb.veiculos (
    placa_veiculo       CHAR(7)     NOT NULL PRIMARY KEY,
    id_unidade          INTEGER     NOT NULL,
    modelo_veiculo      VARCHAR(50) NOT NULL,
    cor_veiculo         VARCHAR(10) NOT NULL,
    status_veiculo      VARCHAR(15) NOT NULL CHECK (status_veiculo IN ('MANUTENCAO','LOCADO','DISPONIVEL','RESERVADO')),
    categoria_veiculo   VARCHAR(20) NOT NULL CHECK (categoria_veiculo IN ('SUV','HATCH','SEDAN','MOTO')),
    combustivel_veiculo VARCHAR(10) NOT NULL CHECK (combustivel_veiculo IN ('ALCOOL','DIESEL','GASOLINA','ELETRICO')),
    FOREIGN KEY (id_unidade) REFERENCES fcardb.unidade(id_unidade)
);

CREATE TABLE fcardb.vistoria (
    id_vistoria    SERIAL PRIMARY KEY,
    cpf_mecanico   CHAR(11) NOT NULL,
    placa_veiculo  CHAR(7)  NOT NULL,
    data_vistoria  DATE DEFAULT CURRENT_DATE,
    laudo_vistoria VARCHAR(400) NOT NULL,
    FOREIGN KEY (cpf_mecanico) REFERENCES fcardb.mecanicos(cpf_mecanico),
    FOREIGN KEY (placa_veiculo) REFERENCES fcardb.veiculos(placa_veiculo)
);

CREATE TABLE fcardb.locacao (
    id_locacao      SERIAL PRIMARY KEY,
    cpf_cliente     CHAR(11) NOT NULL,
    cpf_funcionario CHAR(11) NOT NULL,
    placa_veiculo   CHAR(7)  NOT NULL,
    valor_locacao   DECIMAL(7,2) NOT NULL,
    data_inicio     DATE DEFAULT CURRENT_DATE,
    data_fim        DATE,
    ativo           BOOLEAN DEFAULT true,
    FOREIGN KEY (cpf_cliente) REFERENCES fcardb.clientes(cpf_cliente),
    FOREIGN KEY (cpf_funcionario) REFERENCES fcardb.funcionarios(cpf_funcionario),
    FOREIGN KEY (placa_veiculo) REFERENCES fcardb.veiculos(placa_veiculo)
);