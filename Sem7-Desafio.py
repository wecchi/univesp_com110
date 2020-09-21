'''
    Fórum Temático - Vetores e Matrizes - COM110 - Turma010
    Retomando o Desafio proposto no início da semana: como você implementaria um programa que precisa armazenar X notas de Y alunos?
    E que além das notas, seu programa precisa armazenar a quantidade de faltas que o aluno teve mensalmente ao longo de todo ano?
    E que, para cada aluno, nome, RG e data de nascimento também precisam ser guardados?

    Dados a serem armazenados:
    por aluno: nome, RG e data de nascimento
    por aluno/disciplina: nota e quantidade de faltas
'''

# Importando o módulo de acesso ao SQLite
import sqlite3

# Reemove o arquivo com o banco de dados SQLite (caso exista)
import os
os.remove("desafio_sem7.db") if os.path.exists("desafio_sem7.db") else None

# Se o banco de dados não existir, ele é criado neste momento.
con = sqlite3.connect('desafio_sem7.db')

# Criando um cursor (Um cursor permite percorrer todos os registros em um conjunto de dados)
cur = con.cursor()
    
# Criando o Banco de Dados
'''
    Criação das tabelas para um Banco de Dados no SQL Lite para armazenamento dos dados
'''

# Cria uma instrução sql para criação das tabelas
sql_create_disciplina = 'create table disciplina (id integer primary key AUTOINCREMENT NOT NULL, '\
                        'sigla varchar(6) NOT NULL, nome nvarchar(100), categoria nvarchar(50))'

sql_create_aluno = 'create table aluno (id integer primary key AUTOINCREMENT NOT NULL, '\
                   'nome nvarchar(120) NOT NULL, RG varchar(12), Nascimento datetime)'

sql_create_notas = 'create table notas (id integer primary key AUTOINCREMENT NOT NULL , '\
                   'id_aluno integer, id_disciplina integer, anoLetivo integer, nota float, faltas integer,'\
                   'FOREIGN KEY(id_aluno) REFERENCES aluno, FOREIGN KEY(id_disciplina) REFERENCES disciplina)'

# Executando a instrução para criação das tabelas
cur.execute(sql_create_disciplina)
cur.execute(sql_create_aluno)
cur.execute(sql_create_notas)

# Salvando a estrutura das tabelas
con.commit()

def DataInsert(cur, con, ListaDados, sqlInsert):
    # Inserindo os valores na tabela
    for i in ListaDados:
        cur.execute(sqlInsert,i)
    # Salvando
    con.commit()
    
print('\n' + str('>>> Fórum Temático - Vetores e Matrizes - COM110 - Turma010 <<<').center(80,'-') )

# Definindo uma lista de discliplinas e a instrução para inserção de dados
ListaDisciplina = [('COM110', 'ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES I', 'Ciclo básico'),
                   ('COM140', 'INTRODUÇÃO A CONCEITOS DE COMPUTAÇÃO', 'Ciclo básico'),
                   ('MCA501','CÁLCULO I','Ciclo básico')]
sqlInsertDisciplina = 'insert into disciplina (sigla, nome, categoria) values (?, ?, ?)'

# Definindo uma lista de alunos e a instrução para inserção de dados
ListaAluno = [('Adriana da Silva', '1991-10-20', '65.958.660-8'),
              ('Ana Maria Aparecida', '1981-05-06', '85.118.120-0'),
              ('Antônio Carlos Ferreira dos Santos', '2000-01-08', '90.450.111-4'),
              ('João Francisco Araújo', '1999-08-01', '48.777.665-3'),
              ('Afonso Soarez', '1995-04-04', '55.500.005-5'),
              ('Camila Cristina dos Anjos', '1981-07-12', '23.023.230-8')]
sqlInsertAluno = 'insert into aluno (nome, nascimento, RG) values (?, ?, ?)'

# Definindo uma lista aproveitamento dos alunos (notas e faltas) e a instrução para inserção de dados
ListaNotas = [(1, 1, 2020, 7.9, 0), (1, 2, 2020, 8.9, 1), (1, 3, 2020, 9.9, 0),
              (2, 1, 2020, 7.0, 2), (2, 2, 2020, 5.9, 0), (2, 3, 2020, 8.2, 4),
              (3, 1, 2020, 9.0, 0), (3, 2, 2020, 6.7, 4), (3, 3, 2020, 7.5, 1),
              (4, 1, 2020, 6.0, 5), (4, 2, 2020, 6.2, 8), (4, 3, 2020, 5.5, 4),
              (5, 1, 2020, 10.0, 2),(5, 2, 2020, 8.0, 1), (5, 3, 2020, 8.1, 2),
              (6, 1, 2020, 7.7, 3), (6, 2, 2020, 8.6, 2), (6, 3, 2020, 6.5, 0)]
sqlInsertNotas = 'insert into notas (id_aluno, id_disciplina, anoLetivo, nota, faltas) values (?, ?, ?, ?, ?)'

# Inserindo dos dados no Banco de dados:
DataInsert(cur, con, ListaDisciplina, sqlInsertDisciplina)
DataInsert(cur, con, ListaAluno, sqlInsertAluno)
DataInsert(cur, con, ListaNotas, sqlInsertNotas)


# Fazendo uma consulta ao banco de dados:
sqlConsulta = 'SELECT n.anoLetivo Ano, a.nome Aluno, d.nome Disciplina, n.nota Nota, n.faltas Faltas '\
              'FROM aluno a INNER JOIN notas n ON a.id = n.id_aluno '\
              'INNER JOIN disciplina d ON n.id_disciplina = d.id'

print('\n','  EXEMPLO DE RETORNO DE DADOS FICTÍCIOS  '.center(80,'#'),"\n",'Ano letivo    , Aluno     , Disciplina     , Nota    , Quantidade de Faltas')
cur.execute(sqlConsulta)
for linha in cur.fetchall():
    print(linha) 

# Fechando a conexão
cur.close()
con.close()
