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



#define available fuel types
fuels = {
    'Propane':{
        'Name':'Propane',
        'Molecule':'c3h8',
        'Reaction': ['c3h8+5o2','3co2+4h2o'],
        'Ideal Ratio' : 15.1,
        'Density': 1.97
    }
}


#choosing fuel type
availFuels = list(fuels.keys())
defFuel = 1

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
            print('not a number, to use Default value, press ENTER')
            fuelNum = fuelChoice
        if (type(fuelNum) == type(1)):
            try:
                availFuels[fuelNum-1]
            except:
                print('Choice not in index, to use Default value, press ENTER')
            else:
                break

fuelNum = fuelNum - 1

fuel = availFuels[fuelNum]
#fuel = 'Propane'

#choosing displacement
disp = 70.5#cc #we're assuming 1/2 of the displacement is for the intake, considering its a 2 stroke

while True:
    displacement = input("Displacement in cc(numbers only, Default is 70.5cc)")
    if (displacement == ''):
        displacement = disp
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
                print('Displacement must be greater than 0cc, to use Default value, press ENTER')

displacement = displace/1000 #convert cc to L

#defining engine RPMs
idle = 2200
max = 3800

while True:
    idleCh = input("Idle RPM (numbers only, Default is 3800 RPM)")
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
                print('Idle RPM must be greater than 0 RPM, to use Default value, press ENTER')

while True:
    maxCh = input("Max RPM (numbers only, Default is 2200 RPM)")
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
                print('Max RPM must be greater than 0 RPM, to use Default value, press ENTER')

#defining altitude
alt = 0
while True:
    altCh = input("Altitude in feet (numbers only, Default is 0 feet a.k.a. sealevel)")
    if (altCh == ''):
        altFT = alt
        break
    else:
        try:
            altInt = int(eval(alt))
            altFT = altInt
        except:
            print('not a interger, to use Default value, press ENTER')
            altFT = altCh
        if (type(altFT) == type(1)):
            break


altM = altFT
#https://en.wikipedia.org/wiki/Barometric_formula 
SLpressure = 1 #pressure at sea level in Atmospheres

ATMpa = 101325 * SLpressure #reference pressure 
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

SLMairDensity = 1.225 #g/L
ATMairDensity = 1.225 #g/L

boost = 0

boostATM = boost/14.7
intakePressure = ATMpressure + boostATM #in atmospheres, 1 ATM is air pressure at sealevel
airDensity = ATMairDensity * intakePressure

airDensity = ATMairDensity
fuelDensity = fuels[fuel]['Density']

#define AFRs
actualAFR = actualAFRCalc(fuels[fuel])
idealAFR = fuels[fuel]['Ideal Ratio']

#define the difference between the fuel and air density
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

print(f'Real AFR({ratioType}, lambda: {lambo}): To run a {displacement}L({displacement*1000}cc) engine at idle({idleRPM} RPM), one would have to supply {fuelUseIdle} gpm of fuel, and to max out the engine({maxRPM} RPM), it would need {fuelUseMax} gpm of fuel\n')

fuelUseIdle = idleRPM * idealFuelMass
fuelUseMax = maxRPM * idealFuelMass

print(f'Ideal AFR(Stoicheometric, lambda: 1): To run a {displacement}L({displacement*1000}cc) engine at idle({idleRPM} RPM), one would have to supply {fuelUseIdle} gpm of fuel, and to max out the engine({maxRPM} RPM), it would need {fuelUseMax} gpm of fuel\n')
