import psycopg2
import pandas as pd

class bancoPostgre:

    def __init__ (self):
        self.__errCon = None

    def getConexao(self,usuario):
        try:
            if usuario in 'postgres':
                host = 'localhost'
                database = 'TesteDevmedia'
                username = 'postgres'
                password = 'postgres'
            else:
                print('funcao_nao_encontrada')

            con = psycopg2.connect(host=host, database=database,user=username, password=password)  

        except ValueError as e:
            self.__errCon = str(e)
         
        return(con)
    
    def getError(self):
        return self.__errCon









