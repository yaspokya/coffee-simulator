cont = "y"
while cont == "y":  
   #coffee
    Kopi = input("Masukkan nama kopi:")
    while Kopi != "Latte" and Kopi != "Americano" and Kopi != "Mocha":
        Kopi = input("Masukkan nama kopi:")
    Kuantiti = int(input("Masukkan kuantiti kopi: "))
    if Kopi == "Latte" :
        harga = Kuantiti * 9.9 
        print("You bought",Kuantiti,"Latte")
        print("Your total is RM",harga)
    elif Kopi == "Americano" :
        harga = Kuantiti * 8.9
        print("You bought",Kuantiti,"Americano")
        print("Your total is RM",harga)
    elif Kopi == "Mocha" :
        harga = Kuantiti * 11.2
        print("You bought",Kuantiti,"Mocha")
        print("Your total is RM",harga)

    cont = input("do you want to continue?: ")




        








