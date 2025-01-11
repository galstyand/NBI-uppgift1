price = 2000
discount = input("Skriv in procentsats: ")
toPay = price - price * int(discount) / 100
print("Belopp att betala: " + str(toPay))