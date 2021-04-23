###############################################
# Forfattare: Jennifer Huang
# Uppgift 4
###############################################

# Program 1
import random

def program1():
    index = 0
    while index < 20:
        tal = random.randint(1, 50)
        talÄrPrimtal = ärPrimtal(tal)
        output = str(tal) + " <--"

        if tal % 2 == 0:
            output += " jämnt"
        if talÄrPrimtal:
            output += " primtal"
        if tal % 2 != 0 and talÄrPrimtal is not True:
            output += " udda"
        print(output)
        index += 1

def ärPrimtal(heltal):
   delare = 2
   if(heltal < 2):
       return False
   while(delare < heltal):
       if(heltal % delare == 0):
           return False
       delare += 1   
   return True


# Program 3
import random
import matplotlib.pyplot as plt

antal_punkter = 80
X=[]
Y=[] 

antal = 0

for i in range(antal_punkter):
    xCord = random.randint(-20, 20)
    yCord = random.randint(-20, 20)

    # Räkna alla som hamnar i tredje kvadraten (bottom-left)
    if(xCord <= 0 and yCord <= 0):
        antal += 1
    X.append(xCord)
    Y.append(yCord)

print("Antal bollar i tredje kvadraten: " + str(antal))

ax = plt.figure().add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')     
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.axis([-25,25,-25,25])                          
plt.plot(X, Y, 'o')                                      
plt.savefig('program3.png')
plt.show()
#############################################

program1()