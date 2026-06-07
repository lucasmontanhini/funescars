<h1 style="font-weight: bold;">Funescars</h1>
Data Base scenario for database grade on Technology University of Saint Paul (FATEC-SP)<br>
STUDENT: LUCAS MONTANHINI<br>
<br>
<h2>CENÁRIO PROSPOSTO</h2>
  A rede de locadoras FUNES CARS, que opera desde 1987, deseja desenvolver um sistema para modernizar o fluxo de locação de veículos, sendo necessário criar um banco de dados unificado para todas as suas unidades. A rede possui diversas unidades, e cada unidade é identificada por um código único, além de possuir endereço e telefone próprios. Cada unidade mantém um conjunto de funcionários vinculados exclusivamente a ela. Os funcionários possuem nome, CPF, telefone, e-mail, cargo, data de contratação e salário. Cada unidade também possui sua própria frota de veículos. Os veículos são identificados pela placa e possuem modelo, cor, status, categoria (SUV, Hatch ou Sedan), data da última revisão e tipo de combustível. Os clientes devem realizar um cadastro contendo nome completo, CPF, endereço, telefone para contato e e-mail. Um cliente pode realizar diversas locações ao longo do tempo.	As locações registram a data de início, a data de devolução prevista ou efetiva e o valor da locação. Cada locação está associada a exatamente um cliente e a exatamente um veículo, enquanto um cliente e um veículo podem participar de várias locações ao longo do tempo. Além disso, cada unidade possui um mecânico terceirizado responsável pelas vistorias dos veículos. Cada mecânico está alocado em apenas uma unidade, e toda unidade deve possuir obrigatoriamente um mecânico vinculado. Um mecânico pode realizar vistorias em diversos veículos, e um mesmo veículo pode passar por várias vistorias ao longo de sua vida útil. Para fins de controle operacional, o sistema também deverá permitir identificar o tempo de serviço de cada funcionário, calculado a partir de sua data de contratação, além disso, o sistema deve armazenar a unidade em que o cliente se cadastrou para fins de histórico e controle.
<br>
<h1 style="font-weight: bold;">MODELAGEM CONCEITUAL</h1>
  A primeira etapa efetiva do trabalho foi desenvolver o DIAGRAMA ENTIDADE-RELACIONAMENTO, seguindo os moldes cunhados por PETER CHEN

<img width="2321" height="1550" alt="diagrama" src="https://github.com/user-attachments/assets/5f8311cc-1a0c-4d5f-b68a-95265548b42b" />
Contendo descrição a identificação certeira das entidades, relacionamentos e atributos.
<br>
Após essa etapa,
<h1 style="font-weight: bold;">MODELAGEM LÓGICA</h1>
Elaboração das tabelas perante modelo lógico:

<img width="3501" height="2025" alt="Modelagem lógica" src="https://github.com/user-attachments/assets/b9efb456-04bc-4b23-8c0e-e0ec2c78e683" />
Tendo construído essa estrutura, é chegada a hora da verdade, botando a mão na massa.
<br>
Após essa etapa,
<h1 style="font-weight: bold;">MODELAGEM FÍSICA</h1>

(O script de criação das tabelas está disponivel neste repositório, acima e com o nome "schema.sql")
<img width="1919" height="1042" alt="Captura de tela 2026-06-07 142153" src="https://github.com/user-attachments/assets/005249e5-0892-4a62-bf40-ebc054bbb5d6" />

As tabelas foram geradas seguindo a estrutura que havíamos almejado.
Foram criadas algumas tabelas associativas:
- Como os telefones eram atributos compostos, criamos uma tabela para armazenar os telefones, relacionando o identificador utilizado (no nosso caso o CPF) com o telefone do usuário.
- Locações são relacionadas na tabela "locacao", que armazena o cliente, tem seu ID próprio para registro no sistema (com serial para gerar automaticamente os IDs), armazena o funcionário que realizou a locação, datas, valor e possui uma boolean para marcar se está ativa ou não, facilitando as consultas posteriorees.
- Vistorias também têm sua tabelas associativa, relacionando o mecânico que executou a vistoria com o veículo e o laudo técnico.

Embora não seja o melhor em uso corporativo, utilizamos os CPFs como identificadores únicos dentro do sistema, assim cada funcionário é identificável e cada mecânico também.
Veículos têm o campo de status, onde é possível consultar em qual STATUS o veículo se encontra.

<img width="1914" height="1039" alt="image" src="https://github.com/user-attachments/assets/26646735-43fa-43ff-af89-3cb53e1371c6" />
Armazenamos os dados conforme o tipo correto, sem complicação.
<br>
Após essa etapa,
<h1 style="font-weight: bold;">CRUD</h1>
CRUD, sigla do inglês, significa CREATE, READ, UPDATE and DELETE, eu creio que possamos ler em português como CLAR (CRIAR, LER, ATUALIZAR e DELETAR) — nome bem bonito e corporativo.<br>
Mas indo direto ao ponto, o DB da FunesCars executa perfeitamente todos os ofícios do CRUD:<br>

CREATE:<br>
Para popular o banco de dados, utilizei um algoritmo (disponível no repositório) que me gerou as entradas necessárias (popular.sql)
<img width="1918" height="1042" alt="Captura de tela 2026-06-07 142230" src="https://github.com/user-attachments/assets/202ac5a6-bcdd-4bb0-bb72-d940cbe6a4bd" />

No entanto, como não só de tecnologia vive o homem, eis a inserção manual de dados, funcionando corretamente:
<img width="1527" height="791" alt="image" src="https://github.com/user-attachments/assets/9bff9bdf-16b5-44bd-8e5d-f62ba0485573" />
Executado com sucesso!
<img width="1540" height="102" alt="image" src="https://github.com/user-attachments/assets/d5e1ecd5-07af-4bdf-8c8a-0354349ed834" />

READ:<br>
A leitura é uma dádiva do ser humano, eis aqui a dádiva em prática:
<img width="860" height="861" alt="Captura de tela 2026-06-07 142401" src="https://github.com/user-attachments/assets/84503aab-4bac-4f70-bdff-b8ba7f5daf65" />

Usufruindo do INNER JOIN
<img width="853" height="863" alt="Captura de tela 2026-06-07 142546" src="https://github.com/user-attachments/assets/6d8f0293-760f-4887-8638-346b9a74fb07" />

UPDATE:<br>
UPDATE é importantíssimo, nada nessa vida é imutável:<br>
<img width="1094" height="698" alt="Captura de tela 2026-06-07 142845" src="https://github.com/user-attachments/assets/6d3f86c3-9fa4-4d55-a7e8-dc94c84c6645" />

Antes:<br>
<img width="1470" height="213" alt="Captura de tela 2026-06-07 142800" src="https://github.com/user-attachments/assets/81436ff6-3f9a-464d-95cd-48b3a9087026" />

Posteriormente:<br>
<img width="1269" height="525" alt="Captura de tela 2026-06-07 142901" src="https://github.com/user-attachments/assets/8f0b6745-eeea-4774-b5e1-a2ac1c2aff75" />

UPDATE está updateando corretamente.<br>

DELETE:<br>
Excluir informações depreciadas:<br>
<img width="418" height="181" alt="Captura de tela 2026-06-07 142948" src="https://github.com/user-attachments/assets/ad87ff13-bc1a-4995-8898-34b76f0a1d52" />

ANTES:<br>
<img width="850" height="478" alt="Captura de tela 2026-06-07 143004" src="https://github.com/user-attachments/assets/db3a986f-837f-4106-8599-6d184f8b1509" />
<img width="1086" height="669" alt="Captura de tela 2026-06-07 143024" src="https://github.com/user-attachments/assets/8c3a5b8e-e945-478d-8528-349869460540" />
<img width="850" height="540" alt="Captura de tela 2026-06-07 143114" src="https://github.com/user-attachments/assets/470292e7-5175-4ffa-8685-a8121966f852" /><br>
Não sobrou nada.
