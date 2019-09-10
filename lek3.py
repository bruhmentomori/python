print("Välkommen till mitt räkneprogram")
operator = input("Välj räknesätt +, -, *, /:")



try:
    tal1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    tal1 = 0


try:
    tal2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra: ")
    tal2 = 0

if operator == "+":
    summa = tal1 + tal2
elif operator == "-":
    summa = tal1 - tal2
elif operator == "*":
    summa = tal1 * tal2
elif operator == "/":
    try:
       summa = tal1 / tal2
    except(ZeroDivisionError):
        print("Det går ej att dividera med 0")
        summa = str(" say sike right now")


else:
    print("FEL")


print("Summan är:" + str(summa))
