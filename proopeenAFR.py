'''
Program Name: proopeenAFR.py
Program Purpose: to calculate the volume of air and the volume of propane needed for a given volume at the actual AFR of 17.2768474726:1
Programmer: GoodpastureR
Date: 11/6/2023
'''

def AFRcalc(afr,amt): 
    #afr is the air:fuel ratio(assuming "fuel" is 1) 
    #amt is the amount of "stuff" (volume or mass) available
    x = afr + 1 
    fuel = amt/x
    air = fuel * afr
    return([air,fuel])

#air = literally just air
#fuel = propane

airDensity = 1.225 #g/L
fuelDensity = 1.97 #g/L

actualAFR = 17.2768474726
idealAFR = 15.1

densDiff = airDensity / fuelDensity

volActualAFR = densDiff * actualAFR
volIdealAFR = densDiff * idealAFR


#displacement = input("Displacement in Liters")

displacement = 0.0705 #we're assuming 1/2 of the displacement is for the intake, considering its a 2 stroke

ratio = AFRcalc(volActualAFR , displacement)
print(ratio)
ratio = AFRcalc(volIdealAFR , displacement)
print(ratio)


##finding actual ratio
"""
Chemistry:

Propane combustion equation:
	C3H8+5O2→3CO2+4H2O

Atomic weights:
	Hydrogen= 1.008 amu
	Carbon= 12.011 amu
	Oxygen= 15.999 amu

Propane Mass:
	3(12.011) + 8(1.008)
	36.033    + 8.064
	44.097

Oxygen Mass:
	5(2(15.999))
	5(31.998)
	159.99

Assuming air is 21% oxygen by mass
	100/21 * 159.99
	4.76190476 * 159.99
	761.857143

Actual AFR
	761.857143/44.097:1
	17.2768474726:1

    lambda AFR
		        AFRactual
	lambda =   -----------
		        AFRideal

		      17.2768474726
	lambda = ---------------
		          15.1

	lambda = 1.1441620843

lambda meanings:
	lambda < 1:
		Rich
	lambda > 1:
		Lean
	lambda = 1:
		ideal
"""


