billetes = [100,200,500,1000]
Bancos = (["FDP INVERSMENTS",20000],["Otro",10000])
aux = None
def desglose_FDP_INVERSMENTS():
  global aux,billetes_de_1000,billetes_de_500,billetes_de_200,billetes_de_100
  print("\n-----------------------------------------------\n")
  print("\nHas seleccionado el banco", Bancos[0][0])
  print("  (El limite de retiro 20,000)\n")
  monto = int(input("Ingrese el monto a retirar: "))
  if monto <= Bancos[0][1]:
    if monto % billetes[3] ==0 or monto % billetes[0] == 0:
      if monto >= 19000 and monto <20000:
        billetes_de_1000=(monto-monto%billetes[3])//billetes[3]
        billetes_de_1000 -=1
        monto = monto - 18000
      elif monto == 20000:
        billetes_de_1000=(monto-monto%billetes[3])//billetes[3]
        billetes_de_1000 -=2
        monto = monto - 18000
      else: 
        billetes_de_1000=(monto-monto%billetes[3])//billetes[3]
        monto = monto%1000
      billetes_de_500 = (monto - monto%billetes[2])//billetes[2]
      monto = monto%500
      billetes_de_200 = (monto - monto%billetes[1])//billetes[1]
      monto = monto%200
      billetes_de_100 = (monto - monto%billetes[0])//billetes[0]
    else:
      aux = 0
      if aux == 0:
        print("El monto ingresado no puede ser dispensado, ingrese centenas o unidaddes"
        " de mil")
  else: 
    aux = 1
    if aux == 1:
      print("El monto ingresado es mayor a limite de transferencia")


def desglose_Otros():
  global aux,billetes_de_1000,billetes_de_500,billetes_de_200,billetes_de_100
  print("\n-----------------------------------------------\n")
  print("\nHas seleccionado un banco Ageno (El limite de retiro 10,000)\n")
  monto = int(input("Ingrese el monto a retirar: "))
  if monto <= Bancos[1][1]: 
    if monto % billetes[3] ==0 or monto % billetes[0] == 0:
      billetes_de_1000=(monto-monto%billetes[3])//billetes[3]
      monto = monto%1000
      billetes_de_500 = (monto - monto%billetes[2])//billetes[2]
      monto = monto%500
      billetes_de_200 = (monto - monto%billetes[1])//billetes[1]
      monto = monto%200
      billetes_de_100 = (monto - monto%billetes[0])//billetes[0]
    else:
      aux = 0
      if aux == 0:
        print("El monto ingresado no puede ser dispensado, ingrese centenas o unidaddes"
        " de mil")
  else: 
    aux = 1
    if aux == 1:
      print("El monto ingresado es mayor a limite de transferencia")

def programa():
  #Mensaje de Inicio
  print("Benvenido al cajero del Banco FDP INVERSMENT\n")
  print("1. FDP INVERSMENT\n"
        "2. Otro\n"
        "3. Salir del programa\n")
        
  selec_banco = int(input("Seleccione el Banco que utiliza: "))
  
  while selec_banco != 3:
    if selec_banco == 1:
      desglose_FDP_INVERSMENTS()
      if aux != 0 and aux != 1:
        mostrar_retiro()
        break

    elif selec_banco == 2:
      desglose_Otros()
      if aux != 0 and aux != 1:
        mostrar_retiro()
        break
      
    
def mostrar_retiro():
    print ('\nValor de billetes de 1000: ', billetes_de_1000)
    print ('Valor de billetes de 500: ', billetes_de_500)
    print ('Valor de billetes de 200: ', billetes_de_200)
    print ('Valor de billetes de 100: ', billetes_de_100)
    
#Inicio del programa
programa() 
      
      

  