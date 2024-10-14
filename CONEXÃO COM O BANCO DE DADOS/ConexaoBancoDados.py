import oracledb

#função para obter uma conexão com o oracle database 
def get_connection():
    try:
        connection  = oracledb.connect('RM557774/080403@oracle.fiap.com.br:1521/orcl
        print('Conectado!')')
        return connection
    except Exception as e:
        print(f'Erro ao obter uma conexão: {e}!')
        return connection



#função select
def listar():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM <TBL_AULA_PYTTHON>'
    cursor.execute(sql)


#imprime cada insert da tabela 
    for linha in cursor
        print(linha)


    #connection.commit()
    cursor.close()
    connection.close()