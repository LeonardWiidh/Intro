import os 
os.system('cls')



"""
if är villkor. tänk på if såhär: om (det här händer) gör (såhär)
"""
"""
import random
run_game = True
secret_number = random.randint(1, 100)

print("secret number", secret_number)

print("ayy gissa nummret")
while True:
    try:
        number = int(input("enter number: (0 = quit) "))
    except:
        print("nah uh")
    if number > secret_number:
        print("AYYY sänk farten")
    if number < secret_number:
        print("nah för långt")
    if number == secret_number:
        print('''
        ================
        abow du har rätt
        ================
        ''')
        break
"""
lgh = float(input("hur lång är du i meter "))
if lgh < 1.40:   #minst 1.40
        print("nah du för kort")
if lgh >= 1.40 and lgh <= 1.68:
        print("aaaah, du är kort men du får komma in ")
if lgh == 1.69:
        print("nice")
if lgh >= 1.70:
        print("abow")