class CuentaDigital:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto

    def mostrar_saldo(self):
        return self.__saldo

c = CuentaDigital("Laura", 100000)
c.depositar(50000)
c.retirar(30000)
print(c.mostrar_saldo())