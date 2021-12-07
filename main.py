import os

from colorama import Fore, Back, init
init(autoreset=True)


def menu():
    os.system('clear')
    print("Selecciona una opcion")
    print(Back.CYAN +"\n=========Clientes=========")
    print(Fore.GREEN + "\t3AM")
    print("\t1 - Cenacop;\t2 - Dapromach;\t3 - Disproalza;\t4 - Madeli")
    print("\t5 - Paul_Fl;\t6 - Prooriente;\t7 - Disprovalles;\t8 - Posso_Cueva")
    print(Fore.GREEN + "\t4AM_t1")
    print("\t9 - GarvelProd;\t10 - Almabi;\t11 - Pronaim;\t12 - Grampir")
    print("\t13 - Alsodi;\t14 - Disanahisa;\t15 - Judispro;")
    print(Fore.GREEN + "\t4AM_t2")
    print("\t16 - Dimmia;\t17 - PatricioC;\t18 - Skandinar;\t19 - Pronacnor")
    print("\t20 - H_M;\t21 - Apronam;\t22 - Discarnicos;\t23 - Ecoal")
    print("")
    print("\t24 - Pronaca")
    print("")
    print(Back.CYAN +"\n=====SYNC=======")
    print("\t50 - Por Sincronizar")
    print("")
    print(Back.CYAN +"\n=====Incidencias GDD=======")
    print("\t88 - Consultar Zonales")
    print("")
    
    print("\t9 - salir")


while True:

    menu()

    # solicituamos una opcion al usuario

    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        os.system('python cmaster.py -u CENACOP -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "2":
        os.system('python cmaster.py -u DAPROMACH -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "3":
        os.system('python cmaster.py -u DISPROALZA -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "4":
        os.system('python cmaster.py -u MADELI -c Nuo2021*')
        input("pulsa una tecla para continuar")

  
    elif opcionMenu == "5":
        os.system('python cmaster.py -u PAUL_FLORENCIA -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "6":
        os.system('python cmaster.py -u PROORIENTE -c Nuo2020*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "7":
        os.system('python cmaster.py -u DISPROVALLES -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "8":
        os.system('python cmaster.py -u POSSO_CUEVA -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "9":
        os.system('python cmaster.py -u GARVELPRODUCT -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "10":
        os.system('python cmaster.py -u ALMABI -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "11":
        os.system('python cmaster.py -u PRONAIM -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "12":
        os.system('python cmaster.py -u GRAMPIR -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "13":
        os.system('python cmaster.py -u ALSODI -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "14":
        os.system('python cmaster.py -u DISANAHISA -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "15":
        os.system('python cmaster.py -u JUDISPRO -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "16":
        os.system('python cmaster.py -u DIMMIA -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "17":
        os.system('python cmaster.py -u PATRICIO_CEVALLOS -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "18":
        os.system('python cmaster.py -u SKANDINAR -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "19":
        os.system('python cmaster.py -u PRONACNOR -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "20":
        os.system('python cmaster.py -u H_M -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "21":
        os.system('python cmaster.py -u APRONAM -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "22":
        os.system('python cmaster.py -u DISCARNICOS -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "23":
        os.system('python cmaster.py -u ECOAL -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "24":
        os.system('python cmaster.py -u PRONACA -c Nuo2021*')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "50":
        os.system('python syncf.py')
        input("pulsa una tecla para continuar")

    elif opcionMenu == "88":
        os.system('python ingdd.py')
        input("pulsa una tecla para continuar") 
  


    elif opcionMenu == "300":
        os.system('clear')

    elif opcionMenu == "9":

        break

    else:

        print("")

        input(
            "No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar"
        )
