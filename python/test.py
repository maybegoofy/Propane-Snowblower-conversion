def strFormat(str):
    strx = str.replace('+',' + ')
    return(f' {strx} ')

def atmMass(chem):
    Hmass = 1.008 #amu
    Cmass = 12.011 #amu
    Omass = 15.999 #amu
    start = eval(chem[1])
    end = len(chem) - 1
    if(type(start) == type(0)):
        chemMult = eval(chem[1])
        chem = chem[2:end]
    else:
        chemMult = 1
        chem = chem[1:end]
    tmp = []
    for l in range(len(chem)):
        if(chem[l] == 'h'):
            tmp.append(Hmass)
            if (type(eval(chem[l+1])) == type(0)):
                tmp.append(1)
        elif(chem[l] == 'c'):
            tmp.append(Cmass)
            if (type(eval(chem[l+1])) == type(0)):
                tmp.append(1)
        elif(chem[l] == 'o'):
            tmp.append(Omass)
            if (type(eval(chem[l+1])) == type(0)):
                tmp.append(1)
        else:
            tmp.append(eval(chem[l]))
    chem = tmp
    print(chem)


def actualAFRCalc(fuel):
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
    
    #


    


fuels = {
    'Propane':{
        'Name':'Propane',
        'Molecule':'c3h8',
        'Reaction': ['c3h8+5o2','3co2+4h2o']
    }
}

print(actualAFRCalc(fuels['Propane']))

atmMass(' 5o2h4c ')
#weh = ' 5o2 '
#print(weh[:2])
