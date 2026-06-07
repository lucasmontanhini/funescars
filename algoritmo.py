import random

# Listas de base para geração aleatória e realista
nomes_masc = ["Adriano", "Bruno", "Carlos", "Daniel", "Eduardo", "Fernando", "Gabriel", "Gustavo", "Heitor", "Igor", 
              "João", "Jorge", "Lucas", "Leonardo", "Marcelo", "Matheus", "Nicolas", "Otavio", "Pedro", "Rafael", 
              "Samuel", "Thiago", "Vitor", "Vinicius", "Yuri", "Arthur", "Caio", "Danilo", "Erick", "Felipe", 
              "Guilherme", "Hugo", "Ian", "Jonas", "Kevin", "Luiz", "Murilo", "Neymar", "Orlando", "Paulo", 
              "Renato", "Silvio", "Tarcisio", "Umberto", "Wagner", "Zeca", "Alexandre", "Marcos", "Rodrigo", "Ricardo"]

nomes_fem = ["Amanda", "Beatriz", "Camila", "Daniela", "Elisa", "Fernanda", "Gabriela", "Giovanna", "Helena", "Isabela", 
             "Julia", "Jessica", "Larissa", "Leticia", "Mariana", "Manuela", "Nicole", "Olívia", "Patricia", "Rafaela", 
             "Sofia", "Tais", "Valentina", "Yasmin", "Alice", "Clara", "Diana", "Ester", "Flavia", "Iara", 
             "Janaína", "Karina", "Luana", "Mirella", "Natalia", "Olivia", "Paola", "Roberta", "Sabrina", "Viviane", 
             "Xuxa", "Letícia", "Bárbara", "Carolina", "Priscila", "Débora", "Juliana", "Aline", "Vanessa", "Bruna"]

sobrenomes = ["Silva", "Costa", "Oliveira", "Santos", "Souza", "Rodrigues", "Almeida", "Pereira", "Lima", "Nascimento", 
              "Alves", "Carvalho", "Ribeiro", "Martins", "Gomes", "Rocha", "Barbosa", "Castro", "Cardoso", "Melo", 
              "Ferreira", "Teixeira", "Pinto", "Cavalcanti", "Correa", "Duarte", "Vieira", "Marques", "Cunha", "Freitas", 
              "Ramos", "Araujo", "Mendes", "Morais", "Nunes", "Peixoto", "Neves", "Cruz", "Miranda", "Farias", 
              "Viana", "Guimarães", "Rezende", "Lopes", "Guedes", "Assis", "Campos", "Pires", "Fonseca", "Meireles", 
              "Sales", "Borges", "Antunes", "Frota", "Paiva", "Massa", "Sayao", "Boulos", "Bruni", "Gloss", 
              "Perisse", "Somer", "Siqueira", "Brother", "Paschoal", "Chris", "Bacchi", "Inacio", "Piovani", "Benicio", 
              "Dill", "Palito", "Ricardo", "Carosella", "Aragao", "Sato", "Meira", "Magnani", "Moura", "Meneghel", "Pagodinho"]

# Garantir reprodutibilidade
random.seed(42)

def gerar_nome_completo():
    n = random.choice(nomes_masc + nomes_fem)
    s1 = random.choice(sobrenomes)
    s2 = random.choice(sobrenomes)
    while s1 == s2:
        s2 = random.choice(sobrenomes)
    return f"{n} {s1} {s2}"

# 1. Unidades (10)
unidades = [
    (1, '(11) 91111-1111', '100', '01001000', 'Avenida Paulista'),
    (2, '(21) 92222-2222', '250', '20040000', 'Avenida Rio Branco'),
    (3, '(31) 93333-3333', '50',  '30140010', 'Rua Bahia'),
    (4, '(41) 94444-4444', '12',  '80010000', 'Rua XV de Novembro'),
    (5, '(51) 95555-5555', '300', '90010000', 'Avenida dos Estados'),
    (6, '(61) 96666-6666', '40',  '70040000', 'Via S1'),
    (7, '(71) 97777-7777', '77',  '40015000', 'Avenida Sete de Setembro'),
    (8, '(81) 98888-8888', '850', '50010000', 'Avenida Agamenon Magalhaes'),
    (9, '(85) 99999-9999', '99',  '60010000', 'Avenida Santos Dumont'),
    (10, '(92) 98111-2222', '10', '69005000', 'Avenida Eduardo Ribeiro')
]

# 2. Clientes (Pelo menos 300)
clientes = []
cpfs_clientes = set()
while len(clientes) < 320:
    cpf = f"{random.randint(10000000000, 99999999999)}"
    if cpf not in cpfs_clientes:
        cpfs_clientes.add(cpf)
        nome = gerar_nome_completo()
        email = f"{nome.lower().replace(' ', '')[:15]}@exemplo.com"
        num = str(random.randint(1, 2000))
        u_ref = random.choice(unidades)
        cep = u_ref[3]
        rua = f"Rua Gerada {random.randint(1, 100)}"
        clientes.append((cpf, nome, email, num, cep, rua))

# 3. Funcionários (8 por unidade -> 80 funcionários)
funcionarios = []
cpfs_funcionarios = set()
cargos = ["Atendente", "Vendedor", "Supervisor", "Gerente", "Assistente"]
salarios = {"Atendente": 2800.00, "Vendedor": 3500.00, "Supervisor": 5200.00, "Gerente": 8500.00, "Assistente": 2300.00}

for id_u in range(1, 11):
    # 1 gerente por unidade obrigatório
    for f_idx in range(8):
        while True:
            cpf = f"{random.randint(10000000000, 99999999999)}"
            if cpf not in cpfs_clientes and cpf not in cpfs_funcionarios:
                cpfs_funcionarios.add(cpf)
                break
        nome = gerar_nome_completo()
        email = f"{nome.lower().replace(' ', '')[:12]}@fcar.com"
        cargo = "Gerente" if f_idx == 0 else random.choice(["Atendente", "Vendedor", "Assistente", "Supervisor"])
        sal = salarios[cargo] + random.randint(0, 400)
        data_contratacao = f"2023-0{random.randint(1,9)}-{random.randint(10,28)}"
        funcionarios.append((cpf, nome, email, cargo, f"{sal:.2f}", data_contratacao, id_u))

# 4. Mecânicos (10 mecânicos)
mecanicos = []
cpfs_mecanicos = set()
empresas = ["Oficina Express S.A.", "FixCar Soluções", "TechAuto Centro Automotivo", "PitStop Geral", "Mecânica Unificada"]
for id_u in range(1, 11):
    while True:
        cpf = f"{random.randint(10000000000, 99999999999)}"
        if cpf not in cpfs_clientes and cpf not in cpfs_funcionarios and cpf not in cpfs_mecanicos:
            cpfs_mecanicos.add(cpf)
            break
    nome = f"Mecânico Técnico {id_u}"
    tel = f"({random.randint(11, 99)}) 95555-{random.randint(1000, 9999)}"
    empresa = random.choice(empresas)
    mecanicos.append((cpf, nome, tel, empresa, id_u))

# 5. Veículos (40 por unidade -> 400 veículos)
modelos_pool = [
    ('Jeep Compass T270', 'SUV', 'GASOLINA'), ('Hyundai Creta Ultimate', 'SUV', 'GASOLINA'),
    ('Chevrolet Onix Turbo', 'HATCH', 'ALCOOL'), ('Volkswagen Polo TSI', 'HATCH', 'GASOLINA'),
    ('Toyota Corolla XEI', 'SEDAN', 'GASOLINA'), ('Honda Civic Touring', 'SEDAN', 'GASOLINA'),
    ('Honda CB 300F Twister', 'MOTO', 'GASOLINA'), ('Yamaha Fazer FZ25', 'MOTO', 'GASOLINA'),
    ('BYD King Dolphin', 'SEDAN', 'ELETRICO'), ('Toyota Hilux SRX', 'SUV', 'DIESEL'),
    ('Fiat Uno Mille', 'HATCH', 'ALCOOL'), ('Volvo XC40 Recharge', 'SUV', 'ELETRICO'),
    ('Renault Kwid Intense', 'HATCH', 'GASOLINA'), ('Fiat Fastback Impend', 'SUV', 'GASOLINA'),
    ('Nissan Versa Exclusive', 'SEDAN', 'GASOLINA'), ('BMW 320i M Sport', 'SEDAN', 'GASOLINA'),
    ('Yamaha XMAX 250', 'MOTO', 'GASOLINA'), ('Honda Biz 125', 'MOTO', 'GASOLINA'),
    ('Chevrolet Tracker Premier', 'SUV', 'GASOLINA'), ('Volkswagen T-Cross High', 'SUV', 'GASOLINA')
]
cores = ['Preto', 'Branco', 'Prata', 'Cinza', 'Vermelho', 'Azul']
status_lista = ['DISPONIVEL', 'LOCADO', 'MANUTENCAO', 'RESERVADO']

veiculos = []
placas = set()
letras_p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for id_u in range(1, 11):
    for v_idx in range(40):
        while True:
            # Gerar placa Mercosul fake (ex: ABC1C23)
            l = [random.choice(letras_p) for _ in range(4)]
            n = [str(random.randint(0, 9)) for _ in range(3)]
            placa = f"{l[0]}{l[1]}{l[2]}{n[0]}{l[3]}{n[1]}{n[2]}"
            if placa not in placas:
                placas.add(placa)
                break
        modelo, cat, comb = random.choice(modelos_pool)
        cor = random.choice(cores)
        status = random.choice(status_lista)
        veiculos.append((placa, id_u, modelo, cor, status, cat, comb))

# 6. Vistorias (Gerar pelo menos 150 vistorias espalhadas)
vistorias = []
laudos = [
    "Vistoria periódica em conformidade. Nível de óleo correto, pneus em bom estado de conservação.",
    "Aprovado integralmente para locação de curta e longa distância. Sem avarias ou observações.",
    "REPROVADO temporariamente. Necessita de substituição imediata das pastilhas de freio dianteiras.",
    "Vistoria de rotina preventiva executada sem inconformidades técnicas ou mecânicas detectadas.",
    "Aprovado. Componentes elétricos inspecionados individualmente, bateria em perfeito estado de carga.",
    "Alinhamento e balanceamento preventivo recomendados para a próxima parada técnica na oficina."
]
for i in range(160):
    v = random.choice(veiculos)
    mec = random.choice(mecanicos)
    data = f"2026-05-{random.randint(10, 28):02d}"
    laudo = "REPROVADO. Sistema de suspensão avariado ou pneus desgastados." if v[4] == 'MANUTENCAO' else random.choice(laudos)
    vistorias.append((mec[0], v[0], data, laudo))

# 7. Locações (Pelo menos 150 para enriquecer o banco)
locacoes = []
for i in range(180):
    cli = random.choice(clientes)
    func = random.choice(funcionarios)
    v = random.choice(veiculos)
    
    valor = random.uniform(350.00, 3800.00)
    data_ini = f"2026-04-{random.randint(10, 28):02d}"
    
    # Manter consistência: se o veículo está com status LOCADO hoje, o término deve ser nulo
    if v[4] == 'LOCADO' and random.random() > 0.3:
        data_fim = "NULL"
    else:
        data_fim = f"'2026-05-{random.randint(10, 28):02d}'"
        
    locacoes.append((cli[0], func[0], v[0], f"{valor:.2f}", data_ini, data_fim))

# Escrevendo no super arquivo SQL
filename = "super_popular_banco_fcardb.sql"
with open(filename, "w", encoding="utf-8") as f:
    f.write("-- =====================================================\n")
    f.write("-- SCRIPT EM LARGA ESCALA PARA O BANCO FCARDB\n")
    f.write("-- ESTRUTURA COERENTE E TOTALMENTE POPULADA\n")
    f.write(f"-- RESUMO: 10 UNIDADES | {len(clientes)} CLIENTES | {len(funcionarios)} FUNCIONÁRIOS\n")
    f.write(f"--         {len(mecanicos)} MECÂNICOS | {len(veiculos)} VEÍCULOS | {len(vistorias)} VISTORIAS | {len(locacoes)} LOCAÇÕES\n")
    f.write("-- =====================================================\n\n")
    f.write("BEGIN;\n\n")
    
    # 1. Unidades
    f.write("-- 1. INSERINDO UNIDADES (10)\n")
    f.write("INSERT INTO fcardb.unidade (id_unidade, telefone_unidade, numero_endereco, cep_endereco, rua_endereco) VALUES\n")
    f.write(",\n".join([f"({id_u}, '{tel}', '{num}', '{cep}', '{rua}')" for id_u, tel, num, cep, rua in unidades]))
    f.write(";\n\nALTER SEQUENCE fcardb.unidade_id_unidade_seq RESTART WITH 11;\n\n")
    
    # 2. Clientes
    f.write("-- 2. INSERINDO CLIENTES (300+)\n")
    f.write("INSERT INTO fcardb.clientes (cpf_cliente, nome_cliente, email_cliente, num_endereco_cliente, cep_endereco_cliente, rua_endereco_cliente) VALUES\n")
    f.write(",\n".join([f"('{cpf}', '{nome}', '{email}', '{num}', '{cep}', '{rua}')" for cpf, nome, email, num, cep, rua in clientes]))
    f.write(";\n\n")
    
    # 3. Telefones Clientes
    f.write("-- 3. INSERINDO TELEFONES DOS CLIENTES\n")
    f.write("INSERT INTO fcardb.tel_cliente (cpf_cliente, telefone_cliente) VALUES\n")
    tel_clientes_rows = [f"('{c[0]}', '(11) 99{random.randint(1000000, 9999999)}')" for c in clientes]
    f.write(",\n".join(tel_clientes_rows))
    f.write(";\n\n")
    
    # 4. Funcionarios
    f.write("-- 4. INSERINDO FUNCIONÁRIOS (8 POR UNIDADE = 80)\n")
    f.write("INSERT INTO fcardb.funcionarios (cpf_funcionario, nome_funcionario, email_funcionario, cargo_funcionario, sal_funcionario, contratacao_func, id_unidade) VALUES\n")
    f.write(",\n".join([f"('{cpf}', '{nome}', '{email}', '{cargo}', {sal}, '{data}', {id_u})" for cpf, nome, email, cargo, sal, data, id_u in funcionarios]))
    f.write(";\n\n")
    
    # 5. Telefones Funcionarios
    f.write("-- 5. INSERINDO TELEFONES DOS FUNCIONÁRIOS\n")
    f.write("INSERT INTO fcardb.tel_funcionarios (cpf_funcionario, telefone_funcionario) VALUES\n")
    tel_func_rows = [f"('{f_row[0]}', '(11) 97{random.randint(1000000, 9999999)}')" for f_row in funcionarios]
    f.write(",\n".join(tel_func_rows))
    f.write(";\n\n")
    
    # 6. Mecanicos
    f.write("-- 6. INSERINDO MECÂNICOS (10)\n")
    f.write("INSERT INTO fcardb.mecanicos (cpf_mecanico, nome_mecanico, telefone_mecanico, empresa_mecanico, id_unidade) VALUES\n")
    f.write(",\n".join([f"('{cpf}', '{nome}', '{tel}', '{emp}', {id_u})" for cpf, nome, tel, emp, id_u in mecanicos]))
    f.write(";\n\n")
    
    # 7. Veiculos
    f.write("-- 7. INSERINDO VEÍCULOS (40 POR UNIDADE = 400)\n")
    f.write("INSERT INTO fcardb.veiculos (placa_veiculo, id_unidade, modelo_veiculo, cor_veiculo, status_veiculo, categoria_veiculo, combustivel_veiculo) VALUES\n")
    f.write(",\n".join([f"('{placa}', {id_u}, '{mod}', '{cor}', '{stat}', '{cat}', '{comb}')" for placa, id_u, mod, cor, stat, cat, comb in veiculos]))
    f.write(";\n\n")
    
    # 8. Vistorias
    f.write("-- 8. INSERINDO HISTÓRICO DE VISTORIAS\n")
    f.write("INSERT INTO fcardb.vistoria (cpf_mecanico, placa_veiculo, data_vistoria, laudo_vistoria) VALUES\n")
    f.write(",\n".join([f"('{cpf_m}', '{placa}', '{data}', '{laudo}')" for cpf_m, placa, data, laudo in vistorias]))
    f.write(";\n\n")
    
    # 9. Locacoes
    f.write("-- 9. INSERINDO HISTÓRICO DE LOCAÇÕES\n")
    f.write("INSERT INTO fcardb.locacao (cpf_cliente, cpf_funcionario, placa_veiculo, valor_locacao, data_inicio, data_fim) VALUES\n")
    loc_rows = []
    for cpf_c, cpf_f, placa, valor, d_ini, d_fim in locacoes:
        loc_rows.append(f"('{cpf_c}', '{cpf_f}', '{placa}', {valor}, '{d_ini}', {d_fim})")
    f.write(",\n".join(loc_rows))
    f.write(";\n\n")
    
    f.write("COMMIT;\n")

print("Super arquivo em larga escala gerado com sucesso!")