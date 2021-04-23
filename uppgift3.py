###############################################
# Forfattare: Jennifer Huang
# Uppgift 3
###############################################

tal = []

while (len(tal) < 10):
    tal_to_add = input("Ange tal nr " + str(len(tal) + 1) + ": ")
    tal.append(int(tal_to_add))

def summeraTal(tal):
    summa = 0
    for nummer in tal:
        summa += nummer 
    return summa

def störstaTal(tal):
    största = None
    for nummer in tal:
        if (största is None):
            största = nummer
        if (största < nummer):
            största = nummer
    return största    

def minstaTal(tal):
    minsta = None
    for nummer in tal:
        if (minsta is None):
            minsta = nummer
        if (nummer < minsta):
            minsta = nummer
    return minsta

def medelvärdet(tal):
    return float(summeraTal(tal) / len(tal))

print("Summa: " + str(summeraTal(tal)))
print("Medelvärdet: " + str(medelvärdet(tal)))
print("Största tal: " + str(störstaTal(tal)))
print("Minsta tal: " + str(minstaTal(tal)))
