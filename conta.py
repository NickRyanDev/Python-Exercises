class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Criando conta {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        """mostra o daldo e o titular da conta"""
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        """executa o deposito de um valor na conta"""
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        """verificar se há disponibilidade de saque"""
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def transfere(self, valor, destino):
        """executa a transferencia de valores entre duas contas"""
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def get_limite(self):
        return self.__limite

    @self.limite.setter
    def limite(self, limite):
        self.__limite = limite