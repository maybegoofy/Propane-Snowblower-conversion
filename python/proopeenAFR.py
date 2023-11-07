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
    
def strFormat(str):
    strx = str.replace('+',' + ')
    return(f' {strx} ')

def atmMass(chem):
    Hmass = 1.008 #amu
    Cmass = 12.011 #amu
    Omass = 15.999 #amu

    if(chem[1] != 'h' and chem[1] != 'c' and chem[1] != 'o'):
        chemMult = eval(chem[1])
        chem = chem[2:]
    else:
        chemMult = 1
        chem = chem[1:]
    
    tmp = []
    for l in range(len(chem)):
        if(chem[l] == 'h'):
            tmp.append(Hmass)
            if(chem[l+1] == 'h' or chem[l+1] == 'c' or chem[l+1] == 'o' or chem[l+1] == ' '):
                tmp.append(1)
        elif(chem[l] == 'c'):
            tmp.append(Cmass)
            if(chem[l+1] == 'h' or chem[l+1] == 'c' or chem[l+1] == 'o' or chem[l+1] == ' '):
                tmp.append(1)
        elif(chem[l] == 'o'):
            tmp.append(Omass)
            if(chem[l+1] == 'h' or chem[l+1] == 'c' or chem[l+1] == 'o' or chem[l+1] == ' '):
                tmp.append(1)
        else:
            if (chem[l] != ' '):
                tmp.append(eval(chem[l]))
    tmp2 = []
    
    for t in range(int(len(tmp)/2)):
        x = t * 2
        tmp2.append(tmp[x] * tmp[x+1])

    mass = 0
    for n in range(len(tmp2)):
        mass += tmp2[n]
    mass = mass * chemMult
    return(mass)

def actualAFRCalc(fuel):
    o2percent = 21
    oxyperc = 100/o2percent
    fuelName = fuel['Name']
    molecule = strFormat(fuel['Molecule'])
    reaction = fuel['Reaction']
    reactants = strFormat(reaction[0])
    products = strFormat(reaction[1])

    otherReactantsLen = len(reactants) - len(molecule)

    for i in range(otherReactantsLen):
        start = i
        end = i + len(molecule)
        end1 = end + 1

        if(i > 0):
            noot = ' + '
            start1 = start - 1
        else:
            noot = ''
            start1 = start
        
        if(molecule == reactants[start:end]):
            otherReactants = f'{reactants[:start1]}{noot}{reactants[end1:]}'
    
    fuelMass = atmMass(molecule)
    otherReactantsMass = 0
    otherReactantsSplit = otherReactants.split('+')
    for x in range(len(otherReactantsSplit)):
        otherReactantsMass += atmMass(otherReactantsSplit[x])
    airMass = oxyperc * otherReactantsMass
    ratio = airMass/fuelMass
    return(ratio)




fuels = {
    'Propane':{
        'Name':'Propane',
        'Molecule':'c3h8',
        'Reaction': ['c3h8+5o2','3co2+4h2o'],
        'Ideal Ratio' : 15.1,
        'Density': 1.97
    }
}


#air = literally just air
#fuel = propane

airDensity = 1.225 #g/L
fuelDensity = fuels['Propane']['Density']
#displacement = input("Displacement in Liters")
displacement = 0.0705 #we're assuming 1/2 of the displacement is for the intake, considering its a 2 stroke
idleRPM = 2200
maxRPM = 3800


actualAFR = actualAFRCalc(fuels['Propane'])
idealAFR = fuels['Propane']['Ideal Ratio']


densDiff = fuelDensity / airDensity


volActualAFR = densDiff * actualAFR
volIdealAFR = densDiff * idealAFR


volActualRatio = AFRcalc(volActualAFR , displacement)
volIdealRatio = AFRcalc(volIdealAFR , displacement)


actualFuelMass = volActualRatio[1] * fuelDensity
idealFuelMass = volIdealRatio[1] * fuelDensity

lambo = idealFuelMass/actualFuelMass
if(lambo == 1):
    ratioType = 'Stoicheometric'
elif(lambo > 1):
    ratioType = 'Lean'
else:
    ratioType = 'Rich'

fuelUseIdle = idleRPM * actualFuelMass
fuelUseMax = maxRPM * actualFuelMass

print(f'To run a {displacement}L({displacement*1000}cc) engine at idle({idleRPM} RPM), one would have to supply {fuelUseIdle} gpm of fuel, and to max out the engine({maxRPM} RPM), it would need {fuelUseMax} gpm of fuel')



