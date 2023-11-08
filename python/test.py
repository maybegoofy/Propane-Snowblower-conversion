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
            print(f'found {molecule} at index {start}:{end}')
            if (reactants[i] == ' '):
                fuelMolecule = molecule
            else:
                while True:
                    n += 1
                    if (n > i):
                        break
                    else:
                        print(reactants[i-n:end])
                        if (i >= n and reactants[i-n] == ' '):
                            fuelMolecule = f' {reactants[i-n:end]} '
                            if (len(fuelMolecule) < len(reactants)):
                                if (i-n > 0):
                                    sepa = ' + '
                                else: 
                                    sepa = ''
                                otherReactants = f'" {reactants[:i-n]}{sepa}{reactants[end+3:]}"'
                            else:
                                otherReactants = '  '
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



#define available fuel types
fuels = {
    'Propane':{
        'Name':'Propane',
        'Molecule':'c3h8',
        'Reaction': ['c3h8+5o2','3co2+4h2o'],
        'Ideal Ratio' : 15.1, #to 1
        'Density': 1.97, #in g/L
        'Type':'gas'
    },
    'Petroleum/Gasoline':{
        'Name':'Petroleum/Gasoline',
        'Molecule':'c8h18',
        'Reaction': ['2c8h18+25o2','16co2+18h2o'],
        'Ideal Ratio' : 14.7, #to 1
        'Density': 755, #in g/L
        'Type':'liquid'
    }
}
print(actualAFRCalc(fuels['Propane']))
print(actualAFRCalc(fuels['Petroleum/Gasoline']))