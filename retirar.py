
def retirar(valor,saldo):
  if valor> saldo:
    print ("monto no valido su saldo es: ", saldo)
    return False, saldo
  print("retiro exitoso, su saldo actual es:", saldo-valor)   
  return True, saldo - valor 
    
