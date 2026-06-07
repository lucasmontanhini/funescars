# Funescars

<p align="center">
  <img width="100%" alt="Funescars Banner" src="https://github.com/user-attachments/assets/5c9b8ea5-a138-45b4-9f48-6d81be768cfd" style="border-radius: 8px;" />
</p>

> **Cenário de Banco de Dados** desenvolvido para a disciplina de Banco de Dados.<br>
> **Instituição:** Faculdade de Tecnologia do Estado de São Paulo (FATEC)<br>
> **Estudante:** Lucas Montanhini

---

## Cenário Proposto

A rede de locadoras FUNES CARS, que opera desde 1987, deseja desenvolver um sistema para modernizar o fluxo de locação de veículos, sendo necessário criar um banco de dados unificado para todas as suas unidades. A rede possui diversas unidades, e cada unidade é identificada por um código único, além de possuir endereço e telefone próprios. Cada unidade mantém um conjunto de funcionários vinculados exclusivamente a ela. Os funcionários possuem nome, CPF, telefone, e-mail, cargo, data de contratação e salário. Cada unidade também possui sua própria frota de veículos. Os veículos são identificados pela placa e possuem modelo, cor, status, categoria (SUV, Hatch ou Sedan), data da última revisão e tipo de combustível. Os clientes devem realizar um cadastro contendo nome completo, CPF, endereço, telefone para contato e e-mail. Um cliente pode realizar diversas locações ao longo do tempo. As locações registram a data de início, a data de devolução prevista ou efetiva e o valor da locação. Cada locação está associada a exatamente um cliente e a exatamente um veículo, enquanto um cliente e um veículo podem participar de várias locações ao longo do tempo. Além disso, cada unidade possui um mecânico terceirizado responsável pelas vistorias dos veículos. Cada mecânico está alocado em apenas uma unidade, e toda unidade deve possuir obrigatoriamente um mecânico vinculado. Um mecânico pode realizar vistorias em diversos veículos, e um mesmo veículo pode passar por várias vistorias ao longo de sua vida útil. Para fins de controle operacional, o sistema também deverá permitir identificar o tempo de serviço de cada funcionário, calculado a partir de sua data de contratação, além disso, o sistema deve armazenar a unidade em que o cliente se cadastrou para fins de histórico e controle.

---

## Modelagem Conceitual

A primeira etapa do projeto consistiu no desenvolvimento do **Diagrama Entidade-Relacionamento (DER)**, seguindo o modelo clássico de *Peter Chen*, garantindo a identificação precisa de entidades, atributos e relacionamentos.

<p align="center">
  <img width="85%" alt="Diagrama Conceitual" src="https://github.com/user-attachments/assets/5f8311cc-1a0c-4d5f-b68a-95265548b42b" style="border-radius: 8px;" />
</p>

---

## Modelagem Lógica

Com a estrutura conceitual validada, os dados foram mapeados para o **Modelo Lógico**, definindo chaves primárias (PK), estrangeiras (FK) e a cardinalidade das tabelas.

<p align="center">
  <img width="90%" alt="Modelagem Lógica" src="https://github.com/user-attachments/assets/b9efb456-04bc-4b23-8c0e-e0ec2c78e683" style="border-radius: 8px;" />
</p>

---

## Modelagem Física

> *O script completo de criação das tabelas está disponível neste repositório sob o nome `schema.sql`.*

As tabelas foram geradas no SGBD seguindo estritamente o planejamento lógico:

<p align="center">
  <img width="90%" alt="Modelagem Física" src="https://github.com/user-attachments/assets/005249e5-0892-4a62-bf40-ebc054bbb5d6" style="border-radius: 8px;" />
</p>

### Destaques da Implementação:
* **Atributos Multivalorados:** Como os telefones eram atributos compostos/multivalorados, isolamos a estrutura em uma tabela própria para garantir a Primeira Forma Normal (1FN).
* **Tabela Associativa de Locações:** A tabela `locacao` centraliza o relacionamento, utilizando chaves estrangeiras, controle de valores, datas e uma flag booleana para marcar locações ativas, otimizando futuras consultas.
* **Vistorias:** Uma tabela associativa robusta que conecta o mecânico responsável ao veículo inspecionado, armazenando o respectivo laudo técnico.
* **Garantia de Tipagem:** Dados armazenados estritamente com seus tipos correspondentes (`VARCHAR`, `INT`, `DATE`, `BOOLEAN`), garantindo a integridade referencial.

<p align="center">
  <img width="90%" alt="Tipos de Dados" src="https://github.com/user-attachments/assets/26646735-43fa-43ff-af89-3cb53e1371c6" style="border-radius: 8px;" />
</p>

---

## Operações CRUD

O banco de dados da FunesCars executa perfeitamente todas as operações do ciclo **CRUD** *(Create, Read, Update, Delete)* — ou, em um bom português corporativo: **CLAR** *(Criar, Ler, Atualizar e Deletar)*.

### CREATE (Inserção)
Para popular inicialmente o banco de dados, foi utilizado um algoritmo (`algoritmo.py`) para gerar o script (`popular.sql`). No entanto, as inserções manuais via comandos `INSERT INTO` também foram validadas com sucesso:

<p align="center">
  <img width="85%" alt="Insert Manual" src="https://github.com/user-attachments/assets/9bff9bdf-16b5-44bd-8e5d-f62ba0485573" />
  <img width="85%" alt="Sucesso Insert" src="https://github.com/user-attachments/assets/d5e1ecd5-07af-4bdf-8c8a-0354349ed834" />
</p>

---

### READ (Consulta)
As consultas foram estruturadas desde seleções simples até junções complexas utilizando `INNER JOIN` para consolidar dados de múltiplas tabelas relacionais.

<p align="center">
  <img width="45%" alt="Consulta Simples" src="https://github.com/user-attachments/assets/84503aab-4bac-4f70-bdff-b8ba7f5daf65" />
  <img width="45%" alt="Consulta Join" src="https://github.com/user-attachments/assets/6d8f0293-760f-4887-8638-346b9a74fb07" />
</p>

#### Atributos Derivados (Views)
Para resolver o requisito do "tempo de serviço" (atributo derivado), criamos uma `VIEW` que calcula dinamicamente o tempo com base na data atual, utilizando `ALIAS` para refinar a legibilidade do relatório:

<p align="center">
  <img width="85%" alt="Criação da View" src="https://github.com/user-attachments/assets/9367a243-589e-4c12-8115-39fa1b739848" />
  <img width="85%" alt="Resultado View" src="https://github.com/user-attachments/assets/50a0ee1b-4a39-4827-b202-715e9d240912" />
</p>

---

### UPDATE (Atualização)
A mutabilidade dos dados foi testada através de comandos `UPDATE`, garantindo que modificações pontuais reflitam instantaneamente no estado atual do banco.

* **Antes da alteração:**
<p align="center"><img width="85%" alt="Antes Update" src="https://github.com/user-attachments/assets/81436ff6-3f9a-464d-95cd-48b3a9087026" /></p>

* **Execução e Resultado:**
<p align="center"><img width="85%" alt="Depois Update" src="https://github.com/user-attachments/assets/8f0b6745-eeea-4774-b5e1-a2ac1c2aff75" /></p>

---

### DELETE (Exclusão)
Remoção segura de registros e dados depreciados utilizando a cláusula `DELETE` acompanhada de filtros restritivos (`WHERE`).

<p align="center">
  <img width="85%" alt="Comando Delete" src="https://github.com/user-attachments/assets/ad87ff13-bc1a-4995-8898-34b76f0a1d52" />
  <img width="85%" alt="Resultado Delete" src="https://github.com/user-attachments/assets/470292e7-5175-4ffa-8685-a8121966f852" />
</p>

---

## Consultas Avançadas e Relatórios

Abaixo estão descritas as consultas de inteligência de negócio elaboradas para extração de relatórios operacionais:
