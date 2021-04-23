###############################################
# Forfattare: Jennifer Huang
# Uppgift 3
###############################################
import math
#Beräknar area för en rektangel, samt returnerar arean
def rektangelarea(bredd, höjd):
   return bredd * höjd
 
#Beräknar cirkelns area
def cirkelarea(radie):
   return (radie * radie) * 3.14
 
#Beräknar hypotenusa i en rätvinklig triangel, samt returnerar hypotenusan
def hypotenusa(katet1, katet2):
   return math.sqrt((katet1 * katet1) + (katet2 * katet2))
 
#Funktion som returnerar true om heltal är primtal, annars false
def ärPrimtal():
    heltal = int(input("Ange ett heltal: "))
    delare = 2
    if(heltal < 2):
        print(str(heltal) + " är inte ett primtal")
        return 
    while(delare < heltal):
        if(heltal % delare == 0):
            print(str(heltal) + " är inte ett primtal")
            return
        delare += 1   
    print(str(heltal) + " är ett primtal")
 
#skriver ut informationen 
print(str(rektangelarea(10, 5)))
print(str(cirkelarea(5)))
print(str(hypotenusa(8,6)))

ärPrimtal()