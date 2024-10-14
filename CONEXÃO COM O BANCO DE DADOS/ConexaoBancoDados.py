import oracledb

#função para obter uma conexão com o oracle database 
def get_connection():
    try:
        connection  = oracledb.connect('RM557774/080403@oracle.fiap.com.br:1521/orcl')
        print('Conectado!')
        return connection
    except Exception as e:
        print(f'Erro ao obter uma conexão: {e}!')
        return connection



#função select
def listar():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM TBL_AULA_PYTTHON'
    cursor.execute(sql)


#imprime cada insert da tabela 
    for linha in cursor:
        print(linha)


    #connection.commit()
    cursor.close()
    connection.close()

#função Insert
def inserir():
   connection= get_connection()
   cursor = connection.cursor()
   sql= "INSERT INTO TBL_AULA_PYTTHON VALUES('julio',21,'rua jaci')"
   cursor.execute(sql)
   connection.commit()
   print('Dados Inseridos!')
   cursor.close()
   connection.close()


def inserir_param(nome,numero,endereco):
    connection = get_connection()
    cursor = connection.cursor()
    sql= "SELECT * FROM TBL_AULA_PYTTHON(nome,numero,ebderec0) VALUES({nome},{numero},{endereco})"
    data=(nome, numero,sobrenome)
    cursor.execute(sql,data)
    connection.commit()
    print(f'Dados inseridos!')
    cursor.close()
    connection.close()



#principal

connection = get_connection()
print(f'versão{connection.version}')
listar()
inserir()
listar()
#inserir_params('Júlio',21,'rua jaci')