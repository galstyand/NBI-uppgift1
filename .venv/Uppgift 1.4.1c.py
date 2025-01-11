distance = 470
speed = input("Ange hastighet: ")
time = float(distance / int(speed) * 60)
print(str(time//60) + " timmar och " + str(time%60) + " minuter")