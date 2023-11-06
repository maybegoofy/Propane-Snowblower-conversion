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

def actualAFRCalc(fuel):
    fuelName = fuel['Name']
    molecule = fuel['Molecule']
    reaction = fuel['Reaction']
    reactants = reaction[0]
    products = reaction[1]
    H = 1.008 #amu
	C = 12.011 #amu
	O = 15.999 #amu


fuels = {
    'Propane':{
        'Name':'Propane',
        'Molecule':'C3H8',
        'Reaction': ['C3H8+5O2','3CO2+4H2O']
    }
}

print(actualAFRCalc(fuels['Propane']))


#air = literally just air
#fuel = propane

airDensity = 1.225 #g/L
fuelDensity = 1.97 #g/L


actualAFR = 17.2768474726
idealAFR = 15.1


densDiff = fuelDensity / airDensity


volActualAFR = densDiff * actualAFR
volIdealAFR = densDiff * idealAFR

#displacement = input("Displacement in Liters")
displacement = 0.0705 #we're assuming 1/2 of the displacement is for the intake, considering its a 2 stroke


volActualRatio = AFRcalc(volActualAFR , displacement)
volIdealRatio = AFRcalc(volIdealAFR , displacement)


actualFuelMass = volActualRatio[1] * fuelDensity
idealFuelMass = volIdealRatio[1] * fuelDensity



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


