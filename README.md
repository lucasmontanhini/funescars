# Funescars

<p align="center">
  <img width="100%" alt="Funescars Banner" src="https://github.com/user-attachments/assets/5c9b8ea5-a138-45b4-9f48-6d81be768cfd" style="border-radius: 8px;" />
</p>

> **Cenário de Banco de Dados** desenvolvido para a disciplina de Banco de Dados.
> **Instituição:** Faculdade de Tecnologia do Estado de São Paulo (FATEC)
> **Estudante:** Lucas Montanhini

---

## Cenário Proposto

  A rede de locadoras FUNES CARS, que opera desde 1987, deseja desenvolver um sistema para modernizar o fluxo de locação de veículos, sendo necessário criar um banco de dados unificado para todas as suas unidades. A rede possui diversas unidades, e cada unidade é identificada por um código único, além de possuir endereço e telefone próprios. Cada unidade mantém um conjunto de funcionários vinculados exclusivamente a ela. Os funcionários possuem nome, CPF, telefone, e-mail, cargo, data de contratação e salário. Cada unidade também possui sua própria frota de veículos. Os veículos são identificados pela placa e possuem modelo, cor, status, categoria (SUV, Hatch ou Sedan), data da última revisão e tipo de combustível. Os clientes devem realizar um cadastro contendo nome completo, CPF, endereço, telefone para contato e e-mail. Um cliente pode realizar diversas locações ao longo do tempo. As locações registram a data de início, a data de devolução prevista ou efetiva e o valor da locação. Cada locação está associada a exatamente um cliente e a exatamente um veículo, enquanto um cliente e um veículo podem participar de várias locações ao longo do tempo. Além disso, cada unidade possui um mecânico terceirizado responsável pelas vistorias dos veículos. Cada mecânico está alocado em apenas uma unidade, e toda unidade deve possuir obrigatoriamente um mecânico vinculado. Um mecânico pode realizar vistorias em diversos veículos, e um mesmo veículo pode passar por várias vistorias ao longo de sua vida útil. Para fins de controle operacional, o sistema também deverá permitir identificar o tempo de serviço de cada funcionário, calculated a partir de sua data de contratação, além disso, o sistema deve armazenar a unidade em que o cliente se cadastrou para fins de histórico e controle.

---

## Modelagem Conceitual

A primeira etapa do projeto consistiu no desenvolvimento do **Diagrama Entidade-Relacionamento (DER)**, seguindo o modelo clássico de *Peter Chen*, garantindo a identificação precisa de entidades, atributos e relacionamentos.

<p align="center">
  <img width="85%" alt="Diagrama Conceitual" src="https://github.com/user-attachments/assets/5f8311cc-1a0c-4d5f-b68a-95265548b42b" style="border-radius: 8px;" />
</p>

---

## Modelagem Lógica

Com a estrutura conceitual validada, os dados foram mapeados para o **Modelo Lógico**, definindo chaves primárias (PK), chaves estrangeiras (FK) e a respectiva cardinalidade das tabelas relacionais.

<p align="center">
  <img width="90%" alt="Modelagem Lógica" src="https://github.com/user-attachments/assets/b9efb456-04bc-4b23-8c0e-e0ec2c78e683" style="border-radius: 8px;" />
</p>

---

## Modelagem Física

> **Nota técnica:** O script completo de criação de tabelas DDL está disponível neste repositório sob o nome `schema.sql`.

As tabelas foram geradas no SGBD seguindo estritamente a arquitetura planejada:

<p align="center">
  <img width="90%" alt="Modelagem Física" src="https://github.com/user-attachments/assets/005249e5-0892-4a62-bf40-ebc054bbb5d6" style="border-radius: 8px;" />
</p>

### Destaques da Implementação:
* **Atributos Multivalorados:** Como os telefones configuravam atributos compostos, isolou-se a estrutura em uma tabela independente relacionando o identificador (CPF) ao número correspondente, garantindo a Primeira Forma Normal (1FN).
* **Tabela Associativa de Locações:** A tabela `locacao` centraliza a operação. Ela armazena o cliente, o veículo, o funcionário responsável, valores, períodos e possui um campo lógico (`BOOLEAN`) para sinalizar locações ativas, simplificando auditorias futuras.
* **Vistorias:** Uma tabela associativa robusta conecta o mecânico alocado à inspeção técnica do veículo e ao respectivo laudo emitido.
* **Integridade de Dados:** Tipagem estrita aplicada a todos os campos (`VARCHAR`, `INT`, `DATE`, `BOOLEAN`), mitigando inconsistências no armazenamento.

<p align="center">
  <img width="90%" alt="Tipos de Dados" src="https://github.com/user-attachments/assets/26646735-43fa-43ff-af89-3cb53e1371c6" style="border-radius: 8px;" />
</p>

---

## Operações CRUD

O ecossistema FunesCars executa nativamente todas as rotinas do ciclo **CRUD** (*Create, Read, Update, Delete*), garantindo a persistência e a consistência das entidades.

### CREATE (Inserção)
A população inicial do banco de dados foi estruturada via algoritmo em Python (`algoritmo.py`), que gerou o script de carga em massa (`popular.sql`). Inserções manuais via blocos `INSERT INTO` também foram homologadas:

<p align="center">
  <img width="85%" alt="Insert Manual" src="https://github.com/user-attachments/assets/9bff9bdf-16b5-44bd-8e5d-f62ba0485573" /><br>
  <img width="85%" alt="Sucesso Insert" src="https://github.com/user-attachments/assets/d5e1ecd5-07af-4bdf-8c8a-0354349ed834" />
</p>

---

### READ (Consulta)
As leituras de dados abrangem desde projeções simples até manipulações relacionais complexas utilizando junções (`INNER JOIN`) para consolidação de relatórios.

<p align="center">
  <img width="45%" alt="Consulta Simples" src="https://github.com/user-attachments/assets/84503aab-4bac-4f70-bdff-b8ba7f5daf65" />
  <img width="45%" alt="Consulta Join" src="https://github.com/user-attachments/assets/6d8f0293-760f-4887-8638-346b9a74fb07" />
</p>

#### Atributos Derivados (Views)
Para suprir o requisito operacional de "tempo de serviço", foi implementada uma `VIEW` que calcula dinamicamente o período trabalhado a partir da data atual, utilizando máscaras de formatação (`ALIAS`) para otimizar a visualização final:

<p align="center">
  <img width="85%" alt="Criação da View" src="https://github.com/user-attachments/assets/9367a243-589e-4c12-8115-39fa1b739848" /><br>
  <img width="85%" alt="Resultado View" src="https://github.com/user-attachments/assets/50a0ee1b-4a39-4827-b202-715e9d240912" />
</p>

---

### UPDATE (Atualização)
A manutenção do estado dos dados foi validada por meio de instruções de modificação (`UPDATE`), assegurando o dinamismo do banco.

* **Estado anterior do registro:**
<p align="center"><img width="85%" alt="Antes Update" src="https://github.com/user-attachments/assets/81436ff6-3f9a-464d-95cd-48b3a9087026" /></p>

* **Estado modificado pós-execução:**
<p align="center"><img width="85%" alt="Depois Update" src="https://github.com/user-attachments/assets/8f0b6745-eeea-4774-b5e1-a2ac1c2aff75" /></p>

---

### DELETE (Exclusão)
Remoção controlada de registros depreciados aplicando a cláusula `DELETE` combinada a restrições via `WHERE` para evitar a perda involuntária de dados.

<p align="center">
  <img width="85%" alt="Comando Delete" src="https://github.com/user-attachments/assets/ad87ff13-bc1a-4995-8898-34b76f0a1d52" /><br>
  <img width="85%" alt="Resultado Delete" src="https://github.com/user-attachments/assets/470292e7-5175-4ffa-8685-a8121966f852" />
</p>

---

## Consultas Avançadas e Relatórios

Abaixo constam as principais consultas de inteligência de negócios implementadas para a extração de dados e suporte às tomadas de decisão da gerência da FunesCars.

### 📋 Consulta 1: Localização de Clientes por Logradouro específico
Filtro avançado de clientes localizados em vias específicas (exemplo: Avenida Paulista).
<p align="center">
  <img width="75%" alt="Consulta 1" src="https://github.com/user-attachments/assets/b3f511ed-44f7-4961-8295-650e0575e6cf" />
</p>

### 🚗 Consulta 2: Monitoramento de Frota Disponível
Relatório para listagem imediata de todos os veículos cujo status operacional atual consta como 'Disponível'.
<p align="center">
  <img width="75%" alt="Consulta 2" src="https://github.com/user-attachments/assets/d9a0905c-f3af-4b31-86d4-2d3bc0cab489" />
</p>

### 💰 Consulta 3: Auditoria de Folha de Pagamento de Alto Escalão
Filtro estratégico identificando funcionários com remuneração superior ao teto de corte de R$ 5.000,00.
<p align="center">
  <img width="75%" alt="Consulta 3" src="https://github.com/user-attachments/assets/10a02e93-7f2d-4692-bb34-90c628d660a0" />
</p>

### 🔋 Consulta 4: Segmentação de Frota Avançada (Categorias e Combustível)
Seleção cruzada que localiza veículos das categorias SUV e Sedan movidos exclusivamente a propulsão Elétrica ou a Gasolina.
<p align="center">
  <img width="75%" alt="Consulta 4" src="https://github.com/user-attachments/assets/70d84f83-47eb-4c8b-adeb-d5efef3033fb" />
</p>

### 📧 Consulta 5: Auditoria de Domínio de Contatos
Uso de operadores de correspondência parcial (`LIKE`) para identificar a distribuição corporativa de clientes sob domínios de e-mail específicos (`@exemplo.com`).
<p align="center">
  <img width="75%" alt="Consulta 5" src="https://github.com/user-attachments/assets/d54112ae-4fe7-4958-93f2-9a6c355d84d0" />
</p>

### 📅 Consulta 6: Análise Temporal de Admissões (Pós-2024)
Consulta cronológica mapeando contratações realizadas a partir do ano de 2024 (retornando conjunto vazio devido à ausência de registros que cumpram a condicional no dataset atual).
<p align="center">
  <img width="75%" alt="Consulta 6" src="https://github.com/user-attachments/assets/3479f820-7fc7-4fe0-824f-ff68ec776c98" />
</p>

### 💵 Consulta 7: Faturamento de Locações por Faixa de Valor
Mapeamento de contratos com receita gerada entre R$ 1.500,00 e R$ 4.000,00, expondo de forma clara a identidade dos clientes associados.
<p align="center">
  <img width="75%" alt="Consulta 7" src="https://github.com/user-attachments/assets/f013c668-b567-46b4-b98a-5f7f96111ea1" />
</p>

### 🔓 Consulta 8: Rastreamento de Contratos de Locação em Aberto
Identificação de locações vigentes cuja data final de devolução consta como nula (`NULL`), indicando processos ativos no pátio.
<p align="center">
  <img width="75%" alt="Consulta 8" src="https://github.com/user-attachments/assets/9af126b4-f3b0-4387-99f4-e336c786377e" />
</p>

### 🛠️ Consulta 9: Cruzamento de Histórico de Vistorias e Estado do Veículo
Junção composta via `INNER JOIN` cruzando os dados de laudos emitidos pela oficina terceirizada com o estado em tempo real da frota automotiva.
<p align="center">
  <img width="85%" alt="Consulta 9" src="https://github.com/user-attachments/assets/f47aa7df-4f98-4d42-9929-492778fd1930" />
</p>

### 🏢 Consulta 10: Dimensionamento de Recursos Humanos por Filial
Filtro departamental que expõe exclusivamente os cargos operacionais de linha de frente ('Atendente' e 'Vendedor') alocados na Unidade Central (ID 1).
<p align="center">
  <img width="65%" alt="Consulta 10" src="https://github.com/user-attachments/assets/04eb2f59-7966-426f-b984-8fe7ca08f709" />
</p>

---

## Conclusão

Com a homologação das estruturas relacionais e validação das rotinas operacionais, o projeto cumpre com excelência os requisitos de modelagem, deixando a infraestrutura tecnológica da **FUNESCARS** perfeitamente apta para gerenciar e escalar sua operação de locação de veículos com integridade e performance.
