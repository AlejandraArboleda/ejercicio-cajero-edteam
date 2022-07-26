import retirar as re
import depositar as dep


def menu(saldo):
    opcion = int((input("que opcion desea realizar? 1 depositar 2 retirar ")))
    if opcion == 1:
        valor = int((input("digite el valor a depositar")))
        return dep.depositar(valor, saldo)
    if opcion == 2:
        valor = int((input("diguiete el valor a retirar")))
        return re.retirar(valor, saldo)
    return False, saldo