molecule = 'c8h18'
reactants = ' 2c8h18 + 25o2 '
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
