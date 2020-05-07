'''
convertation from binary to decimal and from decimal to binary
'''
def dec_to_bin(n, res_list):
    '''
    Convertation from decimal to binary system
    res_list - list  with binary number
    '''
    if n < 2:
        res_list.append(int(n))
        res_list.reverse()
        return res_list
    res_list.append(int(n%2))
    dec_to_bin(n//2, res_list)
    return ''.join(map(str, res_list))

def bin_to_dec(n):
    '''
    convert from binary to decimal
    '''
    return sum((int(x)*2**(len(n)-i-1) for i, x in enumerate(n)))

def convert(n, system):
    '''
    Common enter to choose system for convert
    and verify input number
    '''
    if not isinstance(n, (int, str)):
        print('Error type of number. Accepet str and int')
    if system == 'dec':
        if not set(str(n)).issubset({'0', '1'}):
            print(f'Input {n} is not binary number')
        try:
            print(bin_to_dec(str(n)))
        except:
            print(f'Programm can`t convert {n} in the {system}')
    elif system == 'bin':
        try:
            print(dec_to_bin(n, []))
        except:
            print(f'Programm can`t convert {n} in the {system}')
    else:
        print('Error type of system. We convert to the dec or the bin')
