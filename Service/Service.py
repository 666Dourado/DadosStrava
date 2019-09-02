from Controller.ContrllerStrava import controllerStrava

import time

class serviceStrava:

    def __init__(self):
        self.__erro = None

    def monitor(self):
        controller = controllerStrava()

        while True:
            #recupera Token
            token = controller.retornaTokenStrava()

            #recupera dados da API
            dados = controller.recuperaDados(token)

            #salva dados no banco
            controller.inserirDados(dados)

            time.sleep(3600)
