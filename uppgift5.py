# HITTA PRIMTAL - Orange
def hittaPrimtal(heltal):
   delare = 2
   if(heltal < 2):
       return False
   while(delare < heltal):
       if(heltal % delare == 0):
           return False
       delare += 1 
   return True


# KASTA FYRA TÄRNIGNAR - Gul
def kastaTärning():
    import random
    antal = 0
    antal_kast = int(input("Hur många tärningskast vill du göra?"))

    for i in range(antal_kast):
        t1 = random.randint(1,6)
        t2 = random.randint(1,6)
        t3 = random.randint(1,6)
        t4 = random.randint(1,6)
        t5 = random.randint(1,6)
        
        summa = t1 + t2 + t3 + t4 + t5

        if summa == 25:
            antal += 1

    andel = round(((antal / antal_kast) * 100), 1)
    print("Andel kast med summa 25: " + str(andel))

kastaTärning()


# MAXIMAL ERSÄTTNING - Grå
def maximalErsättning():
antal_stora = 0 #stora lådor
antal_små = 0 #små lådor
EMax = 0 #maximal ersättning

# Stora
for x in range(41):
    # Små
    for y in range(1, 86):
        stor_volym = x * 200
        stor_vikt = x * 5

        liten_volymn = y * 50
        liten_vikt = y * 20

        V = stor_volym + liten_volymn
        m = stor_vikt + liten_vikt



        if V <= 8000 and m <= 1700:
            E = (x * 40) + (y * 25)
            # Möjlig kombination
            print("Ersättning för " + str(x) + " stora och " + str(y) + " små ger " + str(E) + " i ersättning")
            if E > EMax:
                EMax = E
                antal_små = y
                antal_stora = x

print("Tony ska lasta " + str(antal_stora) + " stora och " + str(antal_små) + " små lådor för att få maximal ersättning. Totala fraktersättningen blir: " + str(EMax))
