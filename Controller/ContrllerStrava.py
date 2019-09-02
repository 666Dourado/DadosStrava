from Config.Banco import bancoPostgre
from Api.Strava import strava

import pandas as pd

class controllerStrava:

    def __init__(self):
        self.__erro = None

        
    def recuperaDados(self, token):
        stravaAPI = strava()

        dados = stravaAPI.getPedal(token)

        return dados


    def trataDados(self, row):
        lista = []
        
        if(row['manual'] == False):
            average_speed = row['average_speed']
            average_speed = average_speed * 3.6
            average_speed = round(average_speed,2)
            lista.append(average_speed)

            try:

                average_watts = row['average_watts']
                lista.append(average_watts)

            except:

                average_watts = 0
                lista.append(average_watts)

            distance = row['distance']
            distance = distance / 1000
            distance = round(distance, 2)
            lista.append(distance)

            elapsed_time = row['elapsed_time']
            elapsed_time = elapsed_time / 60
            elapsed_time = round(elapsed_time, 2)
            lista.append(elapsed_time)

            elev_high = row['elev_high']
            lista.append(elev_high)

            elev_low = row['elev_low']
            lista.append(elev_low)

            try:
                kilocalories = row['kilojoules']
                kilocalories = kilocalories * 0.2388
                kilocalories = round(kilocalories, 2)
                lista.append(kilocalories)
            except:
                kilocalories = 0
                lista.append(kilocalories)

            max_speed = row['max_speed']
            max_speed = max_speed * 3.6
            max_speed = round(max_speed, 2)
            lista.append(max_speed)

            moving_time = row['moving_time']
            moving_time = moving_time / 60
            moving_time = round(moving_time, 2)
            lista.append(moving_time)

            name = row['name']
            lista.append(name)

            start_date_local = str(row['start_date_local'])
            start_date_local =  start_date_local.replace('T', ' ')
            start_date_local =  start_date_local.replace('Z', '')
            lista.append(start_date_local)
            
            start_latitude = row['start_latitude']
            lista.append(start_latitude)

            start_longitude = row['start_longitude']
            lista.append(start_longitude)

            total_elevation_gain = row['total_elevation_gain']
            lista.append(total_elevation_gain)

            idPedal = row['id']
            lista.append(idPedal)

            manual = 0
            lista.append(manual)

        else:
            average_speed = row['average_speed']
            average_speed = average_speed * 3.6
            average_speed = round(average_speed, 2)
            lista.append(average_speed)


            average_watts = 0
            lista.append(average_watts)

            distance = row['distance']
            distance = distance / 1000
            lista.append(distance)

            elapsed_time = row['elapsed_time']
            elapsed_time = elapsed_time / 60
            lista.append(elapsed_time)

            elev_high = 0
            lista.append(elev_high)

            elev_low = 0
            lista.append(elev_low)


            kilocalories = 0
            lista.append(kilocalories)

            max_speed = row['max_speed']
            max_speed = max_speed * 3.6
            lista.append(max_speed)

            moving_time = row['moving_time']
            moving_time = moving_time / 60
            lista.append(moving_time)

            name = row['name']
            lista.append(name)

            start_date_local = str(row['start_date_local'])
            start_date_local =  start_date_local.replace('T', ' ')
            start_date_local =  start_date_local.replace('Z', '')
            lista.append(start_date_local)
            
            start_latitude = 0
            lista.append(start_latitude)

            start_longitude = 0
            lista.append(start_longitude)

            total_elevation_gain = row['total_elevation_gain']
            lista.append(total_elevation_gain)

            idPedal = row['id']
            lista.append(idPedal)
            
            manual = 1
            lista.append(manual)

        return lista


    def inserirDados(self, dados):
        for row in dados:
            lista = []
            lista = self.trataDados(row)

            verificaId = self.verificaID(lista[14])

            if(verificaId != lista[14]):

                conexao = bancoPostgre()

                con = conexao.getConexao('postgres')
                cur = con.cursor()

                sql = "INSERT INTO tb_strava(average_speed, average_watts, distance, elapsed_time, elev_high, elev_low, kilojoules, max_speed, moving_time, name, start_date_local, start_latitude, start_longitude, total_elevation_gain, id, manual) VALUES(" + str(lista[0]) + "," + str(lista[1]) + "," + str(lista[2]) + "," + str(lista[3]) + "," + str(lista[4]) + "," + str(lista[5]) + "," + str(lista[6]) + "," + str(lista[7]) + "," + str(lista[8]) + ",'" +  lista[9]  + "' ,'" + str(lista[10]) + "'," + str(lista[11]) + "," + str(lista[12]) + "," + str(lista[13]) + "," + str(lista[14]) + "," + str(lista[15]) + ")"

                cur.execute(sql)

                con.commit()
                con.close()
            
            else:
                print('Nenhum dado Encontrado')


    def verificaID(self, idPedal):
        try:    
            conexao = bancoPostgre()
        
            con = conexao.getConexao('postgres')
            cur = con.cursor()
        
            sql = "select id as idStrava from tb_strava where id =" + str(idPedal)
    
            cur.execute(sql)
            retorno = cur.fetchall()
            retorno = retorno[0]
            retorno = retorno[0]
            print(retorno)
        except:
            retorno = 0

        return retorno


    def retornaTokenStrava(self):
        stravaAPI = strava()

        token = stravaAPI.postToken()
        return token