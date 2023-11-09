'''
Program Name: proopeenAFR.py
Program Purpose: to calculate the volume of air and the volume of propane needed for a given volume at the actual AFR of 17.2768474726:1
Programmer: GoodpastureR
Date: 11/6/2023
'''
import math
#calculates how much of each can fit in a given 'amt' at given ratio 'afr'
def AFRcalc(afr,amt): 
    #afr is the air:fuel ratio(assuming "fuel" is 1) 
    #amt is the amount of "stuff" (volume or mass) available
    x = afr + 1 
    fuel = amt/x
    air = fuel * afr
    return([air,fuel])

#formats chemical formulas for calculating
def strFormat(str):
    strx = str.replace('+',' + ')
    stry = strx.lower()
    return(f' {stry} ')

#calculates the mass of a molecule/reactant/set of molecules

def atmMass(chem):
    Hmass = 1.008 #amu
    Cmass = 12.011 #amu
    Omass = 15.999 #amu

    if(chem[1] != 'h' and chem[1] != 'c' and chem[1] != 'o'):
        if(chem[2] != 'h' and chem[2] != 'c' and chem[2] != 'o'):
            if(chem[3] != 'h' and chem[3] != 'c' and chem[3] != 'o'):
                chemMult = eval(chem[1:4])
                chem = chem[4:]
            else:
                chemMult = eval(chem[1:3])
                chem = chem[3:]
        else:
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

#calculates real AFR by chemistry
def actualAFRCalc(fuel):
    o2percent = 21
    oxyperc = 100/o2percent
    fuelName = fuel['Name']
    molecule = fuel['Molecule'].lower()
    reaction = fuel['Reaction']
    reactants = strFormat(reaction[0])
    products = strFormat(reaction[1])

    otherReactantsLen = len(reactants) - len(molecule)

    for i in range(otherReactantsLen):
        n = 0
        start = i+1
        end = start + len(molecule)
        if (reactants[start:end+1] == f'{molecule} '):
            #print(f'found {molecule} at index {start}:{end}')
            if (reactants[i] == ' '):
                fuelMolecule = f' {molecule} '
                if (i > 0):
                    sepa = ' + '
                else: 
                    sepa = ''
                otherReactants = f' {reactants[:i]}{sepa}{reactants[end+3:]}'
            else:
                while True:
                    n += 1
                    if (n > i):
                        break
                    else:
                        #print(reactants[i-n:end])
                        if (i >= n and reactants[i-n] == ' '):
                            #print(fuelMolecule)
                            fuelMolecule = f' {reactants[i-n:end]} '
                            if (len(fuelMolecule) < len(reactants)):
                                if (i-n > 0):
                                    sepa = ' + '
                                else: 
                                    sepa = ''
                                otherReactants = f' {reactants[:i-n]}{sepa}{reactants[end+3:]}'
                            else:
                                otherReactants = ''
                            break
                        else:
                            print(reactants[i-n])

    fuelMass = atmMass(fuelMolecule)
    otherReactantsMass = 0
    otherReactantsSplit = otherReactants.split('+')
    for x in range(len(otherReactantsSplit)):
        otherReactantsMass += atmMass(otherReactantsSplit[x])
    airMass = oxyperc * otherReactantsMass
    ratio = airMass/fuelMass
    return(ratio)

def mixFuels(lst, f):
    density = 0
    fuelMassS = 0
    airMassS = 0
    fIdealR = f['Ideal Ratio']
    mix = f['mix'][1:]
    ratios = mix[:int(len(mix)/2)]
    fs = mix[int(len(mix)/2):]
    for d in range(2):
        #mixin: lst[fs[x]]
        o2percent = 21
        oxyperc = 100/o2percent
        fuelName = lst[fs[d]]['Name']
        molecule = lst[fs[d]]['Molecule'].lower()
        reaction = lst[fs[d]]['Reaction']
        reactants = strFormat(reaction[0])
        products = strFormat(reaction[1])

        otherReactantsLen = len(reactants) - len(molecule)

        for i in range(otherReactantsLen):
            n = 0
            start = i+1
            end = start + len(molecule)
            if (reactants[start:end+1] == f'{molecule} '):
                #print(f'found {molecule} at index {start}:{end}')
                if (reactants[i] == ' '):
                    fuelMolecule = f' {molecule} '
                    if (i > 0):
                        sepa = ' + '
                    else: 
                        sepa = ''
                    otherReactants = f' {reactants[:i]}{sepa}{reactants[end+3:]}'
                else:
                    while True:
                        n += 1
                        if (n > i):
                            break
                        else:
                            #print(reactants[i-n:end])
                            if (i >= n and reactants[i-n] == ' '):
                                #print(fuelMolecule)
                                fuelMolecule = f' {reactants[i-n:end]} '
                                if (len(fuelMolecule) < len(reactants)):
                                    if (i-n > 0):
                                        sepa = ' + '
                                    else: 
                                        sepa = ''
                                    otherReactants = f' {reactants[:i-n]}{sepa}{reactants[end+3:]}'
                                else:
                                    otherReactants = ''
                                break
                            else:
                                print(reactants[i-n])

        fuelMass = atmMass(fuelMolecule)
        otherReactantsMass = 0
        otherReactantsSplit = otherReactants.split('+')
        for x in range(len(otherReactantsSplit)):
            otherReactantsMass += atmMass(otherReactantsSplit[x])
        airMass = oxyperc * otherReactantsMass
        fuelMass = fuelMass * ratios[d]
        fuelMassS += fuelMass
        airMass = airMass * ratios[d]
        airMassS += airMass
        desity = lst[fs[d]]['Density'] * ratios[d]
        density += desity
    print(density)
    ratio = airMassS/fuelMassS
    return(ratio, density) 


#define available fuel types
fuels = {
    'Propane':{
        'Name':'Propane',
        'Molecule':'c3h8',
        'Reaction': ['c3h8+5o2','3co2+4h2o'],
        'Ideal Ratio' : 15.1, #to 1
        'Density': 1.97, #in g/L
        'Type':'gas',
        'mix':[1]
    },
    'Petrol':{
        'Name':'Petrol',
        'Molecule':'c8h18',
        'Reaction': ['2c8h18+25o2','16co2+18h2o'],
        'Ideal Ratio' : 14.7, #to 1
        'Density': 755, #in g/L
        'Type':'liquid',
        'mix':[1]
    },
    'Petrol E10':{
        'Name':'Petrol E10',
        'Ideal Ratio' : 14.08, #to 1
        'Type':'liquid',
        'mix':[2,.90,.10,'Petrol','Ethanol']
    },
    'Petrol E85':{
        'Name':'Petrol E85',
        'Ideal Ratio' : 9.7, #to 1
        'Type':'liquid',
        'mix':[2,.15,.85,'Petrol','Ethanol']
    },
    'Ethanol':{
        'Name':'Ethanol',
        'Molecule':'c2h6o',
        'Reaction': ['c2h6o+3o2','2co2+3h2o'],
        'Ideal Ratio' : 9, #to 1
        'Density': 789.45, #in g/L
        'Type':'liquid',
        'mix':[1]
    }
}


#choosing fuel type
availFuels = list(fuels.keys())
defFuel = 1
print('')
while True:
    print('Fuel choices(what the program has included):')
    for y in range(len(availFuels)):
        print(f'{y+1}. {availFuels[y]}')
    fuelChoice = input('Which fuel would you like to use?(Number from index above please. Default is index 1.)')
    if (fuelChoice == ''):
        fuelNum = defFuel
        break
    else:
        try:
            fuelNum = int(eval(fuelChoice))
        except:
            print('\nnot a number, to use Default value, press ENTER')
            fuelNum = fuelChoice
        if (type(fuelNum) == type(1)):
            try:
                availFuels[fuelNum-1]
            except:
                print('\nChoice not in index, to use Default value, press ENTER')
            else:
                break

fuelNum = fuelNum - 1

fuelCh = availFuels[fuelNum]
fuel = fuels[fuelCh]
#fuel = 'Propane'

#choosing displacement
disp = 141#cc #we're assuming 1/2 of the displacement is for the intake, considering its a 2 stroke

print('')
while True:
    displacement = input(f"Displacement in cc(numbers only, Default is {disp}cc/2, bc we assume 2 stroke)")
    if (displacement == ''):
        displace = disp/2
        break
    else:
        try:
            displace = float(eval(displacement))
        except:
            print('not a number, to use Default value, press ENTER')
            displace = displacement
        if (type(displace) == type(1.5)):
            if (displace > 0.0):
                break
            else:
                print('\nDisplacement must be greater than 0cc, to use Default value, press ENTER')

displacement = displace/1000 #convert cc to L

#defining engine RPMs
idle = 2200
max = 3800

print('')
while True:
    idleCh = input("Idle RPM (numbers only, Default is 2200 RPM)")
    if (idleCh == ''):
        idleRPM = idle
        break
    else:
        try:
            idleInt = int(eval(idleCh))
            idleRPM = idleInt
        except:
            print('not a interger, to use Default value, press ENTER')
            idleRPM = idleCh
        if (type(idleRPM) == type(1)):
            if (idleRPM > 0):
                break
            else:
                print('\nIdle RPM must be greater than 0 RPM, to use Default value, press ENTER')

print('')
while True:
    maxCh = input("Max RPM (numbers only, Default is 3800 RPM)")
    if (maxCh == ''):
        maxRPM = max
        break
    else:
        try:
            maxInt = int(eval(maxCh))
            maxRPM = maxInt
        except:
            print('not a interger, to use Default value, press ENTER')
            maxRPM = maxCh
        if (type(maxRPM) == type(1)):
            if (maxRPM > 0):
                break
            else:
                print('\nMax RPM must be greater than 0 RPM, to use Default value, press ENTER')

#defining altitude
print('')
alt = 0
while True:
    altCh = input("Altitude in feet (numbers only, Default is 0 feet a.k.a. sealevel)")

    if (altCh == ''):
        altFT = alt
        break
    else:
        try:
            altInt = eval(altCh)
            altFT = altInt
        except:
            print('\nNot a interger, to use Default value, press ENTER')
            altFT = altCh
        else:
            break
'''
#2 or 4 stroke engine type
print('')
strokeDef = 2
while True:
    strokeCh = input("Engine stroke type(2 or 4 only, numbers only please, Default is 2-stroke)\nNote: will half Displacement(per stroke) for 2-strokes, assuming only half of each down stroke is intake.")

    if (strokeCh == ''):
        stroke = strokeDef
        break
    else:
        try:
            stroke = int(eval(strokeCh))
        except:
            print('\nNot a interger, to use Default value, press ENTER')
            stroke = strokeCh
        else:
            if (stroke == 2 or stroke == 4):
                strokeRPM = int(stroke/2)
                break
            else:
                print('\nMust be either 2-stroke or 4-stroke')
'''


altM = altFT/3.28084
#https://en.wikipedia.org/wiki/Barometric_formula 
SLpressure = 1 #pressure at sea level in Atmospheres

ATMpa = 101325 * SLpressure #reference pressure in pascals
g = 9.80665 #gravity
M = 0.0289644 #molar mass of earth air kg/mol
R = 8.31432 #universal gas constant J/(mol*K)
tempK = 300 #temperature in Kelvin
psn = -1 * g * M * altM
psd = R * tempK 
pss = psn/psd
ATMx = math.e ** pss
altPa = ATMpa * ATMx
altPressure = altPa/101325

SLairDensity = 1.225 #g/L air density at sea level
ATMairDensity = SLairDensity * altPressure #g/L air density at elevation
boost = 0 #psi

boostATM = boost/14.7 #convert boost psi to atmospheres
intakePressure = SLpressure + boostATM #in atmospheres, 1 ATM is air pressure at sealevel
airDensity = ATMairDensity * intakePressure

if (fuel['mix'][0] > 1):
    newFuel = mixFuels(fuels,fuel)


else:
    fuelDensitySL = fuel['Density']

    if(fuel['Type'] == 'gas'):
        fuelDensity = fuelDensitySL * altPressure * intakePressure
    else:
        fuelDensity = fuelDensitySL


    #define AFRs
    actualAFR = actualAFRCalc(fuel)
    idealAFR = fuel['Ideal Ratio']

#define the difference between the fuel and air density
densDiff = fuelDensity / airDensity

#calculate volumetric AFR
volActualAFR = densDiff * actualAFR
volIdealAFR = densDiff * idealAFR

'''
if (stroke == 2):
    displace = displacement/2
else:
    displace = displacement
'''
displace = displacement

volActualRatio = AFRcalc(volActualAFR , displace)
volIdealRatio = AFRcalc(volIdealAFR , displace)
volley = volActualRatio[0]/volActualRatio[1]

actualFuelMass = volActualRatio[1] * fuelDensity
idealFuelMass = volIdealRatio[1] * fuelDensity

lambo = idealFuelMass/actualFuelMass
if(lambo == 1):
    ratioType = 'Stoicheometric'
elif(lambo > 1):
    ratioType = 'Lean'
else:
    ratioType = 'Rich'

'''
if (stroke == 2):
    fuelUseIdle = idleRPM * actualFuelMass
    fuelUseMax = maxRPM * actualFuelMass
else:
    fuelUseI = idleRPM * actualFuelMass
    fuelUseM = maxRPM * actualFuelMass
    fuelUseIdle = fuelUseI/strokeRPM
    fuelUseMax = fuelUseM/strokeRPM
'''
fuelUseIdle = idleRPM * actualFuelMass
fuelUseMax = maxRPM * actualFuelMass

print('\nResults:')

print(f'\nReal AFR({ratioType}, lambda: {lambo}): To run a {displacement}L({displacement*1000}cc) 2-stroke engine at idle({idleRPM} RPM), one would have to supply {fuelUseIdle} gpm of fuel, and to max out the engine({maxRPM} RPM), it would need {fuelUseMax} gpm of fuel.\n')
'''
if (stroke == 2):
    fuelUseIdle = idleRPM * actualFuelMass
    fuelUseMax = maxRPM * actualFuelMass
else:
    fuelUseI = idleRPM * actualFuelMass
    fuelUseM = maxRPM * actualFuelMass
    fuelUseIdle = fuelUseI/strokeRPM
    fuelUseMax = fuelUseM/strokeRPM
'''
fuelUseIdle = idleRPM * idealFuelMass
fuelUseMax = maxRPM * idealFuelMass

print(f'Ideal AFR(Stoicheometric, lambda: 1): To run a {displacement}L({displacement*1000}cc) 2-stroke engine at idle({idleRPM} RPM), one would have to supply {fuelUseIdle} gpm of fuel, and to max out the engine({maxRPM} RPM), it would need {fuelUseMax} gpm of fuel.\n')

