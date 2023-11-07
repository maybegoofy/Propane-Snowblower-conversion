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
        'Reaction': ['c3h8+5o2','3co2+4h2o']
    }
}

print(actualAFRCalc(fuels['Propane']))
