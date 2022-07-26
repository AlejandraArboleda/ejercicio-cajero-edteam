import validacion as val

def login():
  print("bienvenido")
  usuario=input("digite usuario")
  clave=input("digite contaseña")
  return val.validaUsuario(usuario,clave)

