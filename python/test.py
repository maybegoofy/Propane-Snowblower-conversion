import math



#defining other world factors, edit 'boost' if running boost
boost = 0 #boost pressure in PSI
ATMpressure = 1 #atmospheric pressure in atmospheres

#calculating air pressure at altitude
#https://www.omnicalculator.com/physics/air-pressure-at-altitude
'''
ATMpa = 101325 * ATMpressure
g = 9.80665
MM = 0.0289644
tempK = 300
psn = g * MM * altM
psd = 8.31432 * tempK 
pss = psn/psd
altPressure = ATMpa * math.e * pss

print(altPressure)
'''
#https://en.wikipedia.org/wiki/Barometric_formula 

altM = 300

ATMpa = 101325 * ATMpressure #reference pressure 
g = 9.80665 #gravity
M = 0.0289644 #molar mass of earth air kg/mol
R = 8.31432 #universal gas constant J/(mol*K)
tempK = 300
psn = -1 * g * M * altM
psd = R * tempK 
pss = psn/psd
ATMx = math.e ** pss
altPa = ATMpa * ATMx
altPressure = altPa/101325
print(altPressure)
