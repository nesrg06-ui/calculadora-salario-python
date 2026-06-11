Horast = input("ingrese las horas que trabajo: ")
H = float(Horast)
tarifaH = input("ingrese la tarifa por hora: ")
T = float(tarifaH)

pago_total = 0.0

if H <= 40:
    pago_total = H * T 
else:
    pago_total = (40 * T) + ((H - 40) * (T * 1.5))

print(pago_total)
