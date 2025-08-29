def change():
    expense = 23.75
    money = 100
    vuelto = int(money - expense)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nvuelto")
    print("\nPesos:")
    print(int(money-expense))
    print("Centavos:")
    print(int(((money-expense)-vuelto)*100))
