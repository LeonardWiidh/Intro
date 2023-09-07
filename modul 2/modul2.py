#1. Kommentarer i Python (använd # för en enskild kommentar eller ‘‘‘ för flera rader av kommentarer)
"""
hej johan
#2. Skriv ut enkla beräkningar
"""
print(10*3.2)
#3. Bygg vidare på välkomstprogrammet med att be om deras ålder
name = input("vad heter du ")
age = input("hur gammal är du ")
land = input("vart kommer du ifrån ")
print("hej " + name + " du är " + age + " år gammal och kommer ifrån " + land)

#4. Gör en miniräknare som multiplicerar två olika tal som användaren matar in
y = int(input("ditt första tal "))
x = int(input("ditt andra tal "))
print(x * y)

#5. BMI-kalkylator
a = float(input("hur mycket väger du i kilo "))
b = float(input("hur lång är du i m "))
print("det här är din BMI" , a//(b**2))

#6. ”Livet i veckor”
a1 = int(input("hur gamma är du "))
print("du är " , a1 * 52 , " veckor gamla")

#7. Vikträknare (från kg till lbs)
c1 = float(input("hur många kilo "))
(print("så är många är det ungefär i lbs " , c1 * 2.20462262))