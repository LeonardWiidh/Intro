import os
os.system('cls') #ränsar terminal

amount = int(input("hur många "))  #variabel sträng

for i in range(0, amount):   #används när du vill ha ett exat antal gånger
    print(str(i+1) + " hello world")
 
dinmamma = 1

while True:
    print("amogos")
    dinmamma = dinmamma + 1        # =  ändra
    if dinmamma == 10:      # == kolla
        break


#4. Gör ett program som skriver ut gångertabeller med nästlade for-loopar

for table in range(1, 13):  #tolv tabeller
    print(f"TABELL {table}")
    for y in range(1, 11):  #tio tal i varje
        print(f"{table} * {y} = {str(table * y)}")


"""
#5
w1 = int(input("vilket tal är din bas "))
w2 = int(input("vilket tal är din exponent "))
w3 = 1
for w2 in range(0 , w2):
    print(str(w1 = w1 * w1))
    w3 + 1
    if w3 == w2:
        break
"""