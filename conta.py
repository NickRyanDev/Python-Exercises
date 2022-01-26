class Conta:

    def __init__(self, number, owner, balance, limit):
        print(f"Criando conta {self}")
        self.__numero = number
        self.__titular = owner
        self.__saldo = balance
        self.__limite = limit

    def extract(self):
        """shows balance and owner of account"""
        print(f"Saldo de {self.__balance} do titular {self.__owner}")

    def deposit(self, value):
        """do deposit of value in an account"""
        self.__balance += value

    def __check_cash_out(self, value_to_cash_out):
        """check withdrawal availability"""
        value_to_cash_out = self.__balance + self.__limit
        return valor_a_sacar <= valor_disponivel_a_sacar

    def cash_out(self, value):
        if(self.__check_cash_out(value)):
            self.__balance -= value
        else:
            print(f"O valor {value} passou o limite")

    def transfer(self, valor, destino):
        """performs the transfer of values between two accounts"""
        self.cash_out(value)
        destino.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def get_limite(self):
        return self.__limite

    @self.limit.setter
    def limit(self, limit):
        self.__limit = limit
