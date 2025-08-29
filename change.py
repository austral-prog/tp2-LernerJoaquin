def change():
    expense = 23.75
    money = 100
    vuelto = int(money - expense)
    centavos = int(((money - expense)-vuelto)*100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
   
    print("\nVuelto\n")
    
    print("Pesos:")
    print(vuelto)
    print("centavos:")
    print(centavos)
