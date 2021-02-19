#---------------------------------------------------------------------------
#Variables

billetes = [100,200,500,1000]
Bancos = (["FDP INVERSMENTS",20000],["Otro",10000])
aux = None
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#Desglose de billetes para el Banco [FDP INVERSMENTS]
#---------------------------------------------------------------------------
def desglose_FDP_INVERSMENTS():
  global aux,billetes_1000,billetes_500,billetes_200,billetes_100
  
  monto = int(input("Ingrese el monto a retirar: "))
  if monto <= Bancos[0][1]:
    if monto % billetes[3] == 0 or monto % billetes[0] == 0:
      if monto >= 18000:
        billetes_1000 = 18 
        monto -= 1800019
      else: 
        billetes_1000=(monto-monto % billetes[3])//billetes[3]
        monto = monto % 1000
      billetes_500 = (monto - monto % billetes[2])//billetes[2]
      monto = monto % 500
      billetes_200 = (monto - monto % billetes[1])//billetes[1]
      monto = monto % 200
      billetes_100 = (monto - monto % billetes[0])//billetes[0]
      mostrar_retiro()
    else:
      aux = 0
      if aux == 0:
        print("\n!!!!El monto ingresado no puede ser dispensado, ingrese centenas o unidaddes"
        " de mil!!!!")
  else: 
    aux = 1
    if aux == 1:
      print("\n!!!!El monto ingresado es mayor a limite de transferencia!!!!")
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
#Desglose de billetes para Banco [Otros]
#---------------------------------------------------------------------------
def desglose_Otros():
  global aux,billetes_1000,billetes_500,billetes_200,billetes_100
  
  monto = int(input("Ingrese el monto a retirar: "))
  if monto <= Bancos[1][1]: 
    if monto % billetes[3] == 0 or monto % billetes[0] == 0:
      billetes_1000=(monto-monto%billetes[3])//billetes[3]
      monto = monto%1000
      billetes_500 = (monto - monto%billetes[2])//billetes[2]
      monto = monto%500
      billetes_200 = (monto - monto%billetes[1])//billetes[1]
      monto = monto%200
      billetes_100 = (monto - monto%billetes[0])//billetes[0]
      mostrar_retiro()
      
    else:
      aux = 0
      if aux == 0:
        print("\n!!!!El monto ingresado no puede ser dispensado, ingrese centenas o unidaddes"
        " de mil!!!!")
  else: 
    aux = 1
    if aux == 1:
      print("\n!!!!El monto ingresado es mayor a limite de transferencia!!!!")

#---------------------------------------------------------------------------
# Mostrar resultados del retiro
#---------------------------------------------------------------------------
def mostrar_retiro():
    global billetes_1000
    print ('\nValor de billetes de 1000: '+ repr(billetes_1000))
    print ('Valor de billetes de 500: ' + repr(billetes_500) )
    print ('Valor de billetes de 200: ' + repr(billetes_200) )
    print ('Valor de billetes de 100: ' + repr(billetes_100) )
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#Estructura del programa
#---------------------------------------------------------------------------
def programa():
  #Mensaje de Inicio
  print("\n_________________________________________________________________\n")
  print("Benvenido al cajero del Banco FDP INVERSMENT\n")
  print("\n-----------------------------------------------------------------\n")
  print("1. FDP INVERSMENT\n"
        "2. Otro banco\n"
        "3. Cancelar transferencia\n")
        
  selec_banco = int(input("Seleccione el Banco que utiliza: "))
  
  while selec_banco != 3:
    if selec_banco == 1:
      print("\n-----------------------------------------------\n")
      print("[ Has seleccionado el banco", Bancos[0][0],"]")
      print("  (El limite de retiro 20,000)\n")
      desglose_FDP_INVERSMENTS()
      if aux != 0 and aux !=1:
        break
    elif selec_banco == 2:
      print("\n-----------------------------------------------\n")
      print("[Has seleccionado un banco diferente (El limite de retiro 10,000)]\n")
      desglose_Otros()
      if aux != 0 and aux !=1:
        break
    elif selec_banco > 3 or selec_banco < 1: 
      print("\n_________________________________________________________________\n")
      print("\!!!El numero ingresado no corresponde a una opción, elija una de las mostradas en pantalla!!!")
      programa()
  else:
    print("Usted ha cancelado la transferencia")       
#----------------------------------------------------------------------    


#---------------------------------------------------------------------------
# Ejecución del programa
#---------------------------------------------------------------------------
programa() 
      
      
'''
PROFESOR POR FAVOR LEA EL ARCHIVO "readme.md"
'''
  