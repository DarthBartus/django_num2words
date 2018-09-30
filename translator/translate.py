numdict = {0: '', 1: 'jeden ', 2: 'dwa ', 3: 'trzy ', 4: 'cztery ', 5: 'pięć ', 6: 'sześć ', 7: 'siedem ', 8: 'osiem ', 9: 'dziewięć ', 10: 'dziesięć ',
           11: 'jedenaście ', 12: 'dwanaście ', 13: 'trzynaście ', 14: 'czternaście ', 15: 'piętnaście ', 16: 'szesnaście ', 17: 'siedemnaście ',
           18: 'osiemnaście ', 19: 'dziewiętnaście ', 20: 'dwadzieścia ', 30: 'trzydzieści ', 40: 'czterdzieści ', 50: 'pięćdziesiąt ',
           60: 'sześćdziesiąt ', 70: 'siedemdziesiąt ', 80: 'osiemdziesiąt ', 90: 'dziewięćdziesiąt ', 100: 'sto ', 200: 'dwieście ',
           300: 'trzysta ', 400: 'czterysta ', 500: 'pięćset ', 600: 'sześćset ', 700: 'siedemset ', 800: 'osiemset ', 900: 'dziewięćset '}

orderDict = {0: ['', '', ''], 1: ['tysiąc ', 'tysiące ', 'tysięcy '], 2: ['milion ', 'miliony ', 'milionów '], 3: ['miliard ', 'miliardy ', 'miliardów ']}


def translate(number):

    numList = (format(number, ',d').split(','))
    fin = []

    for indx, sublist in enumerate(numList):
        if len(sublist) >= 2 and sublist[-2] == '1' and sublist[-1] != 0:
            if len(sublist) == 3:
                fin.append(numdict[int(sublist[0]) * 100])
            fin.append(numdict[int(sublist[-2:])])
        else:
            for i in range(len(sublist)):
                fin.append(numdict[int(sublist[i]) * (10**(len(sublist) - 1 - i))])

        if len(sublist) >= 2:
            if sublist[-2] == '1':
                fin.append(orderDict[len(numList) - 1 - indx][2])
            else:
                if sublist == '000':
                    continue
                if sublist == '001':
                    fin.append(orderDict[len(numList) - 1 - indx][0])
                elif int(sublist[-1]) >= 5 or sublist[-1] == '1' or sublist[-1] == '0':
                    fin.append(orderDict[len(numList) - 1 - indx][2])
                else:
                    fin.append(orderDict[len(numList) - 1 - indx][1])
        else:
            if sublist[0] == '1':
                fin.append(orderDict[len(numList) - 1 - indx][0])
            elif int(sublist[0]) < 5:
                fin.append(orderDict[len(numList) - 1 - indx][1])
            else:
                fin.append(orderDict[len(numList) - 1 - indx][2])
    fin = [x for x in fin if x != '']
    return ''.join(fin).replace('jeden miliard', 'miliard').replace('jeden milion', 'milion').replace('jeden tysiąc', 'tysiąc')
