"""validar usuario, contraseña, de ser correctos puede depositar , retirar dinero;para depositar aumento al saldo, para retirar debo veridicar que no vaya a retirar mas de lo que hay."""
import login as log
import menu 

saldo=1000
i=True
while i==True:
  if log.login():  
    continuar="s"
    while continuar=="s":
      boleano, saldo=menu.menu (saldo)
      continuar=input('deseas realizar otra transaccion?s/n')
  else:
    print("usuario o contraseña incorrectos")
  

  
   

