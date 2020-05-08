'''
convertation from binary to decimal and from decimal to binary
'''
def dec_to_bin(dec_number, res_list):
    '''
    Convertation from decimal to binary system
    res_list - list  with binary number
    '''
    if dec_number < 2:
        res_list.append(int(dec_number))
        res_list.reverse()
        return res_list
    res_list.append(int(dec_number%2))
    dec_to_bin(dec_number//2, res_list)
    return ''.join(map(str, res_list))

def bin_to_dec(bin_number):
    '''
    convert from binary to decimal
    '''
    return sum((int(x)*2**(len(bin_number)-i-1) for i, x in enumerate(bin_number)))

def convert(number, system):
    '''
    Common enter to choose system for convert
    and verify input number
    '''
    if not isinstance(number, (int, str)):
        print('Error type of number. Accepet str and int')
    if system == 'dec':
        if not set(str(number)).issubset({'0', '1'}):
            print(f'Input {number} is not binary number')
        try:
            print(bin_to_dec(str(number)))
        except:
            print(f'Programm can`t convert {number} in the {system}')
    elif system == 'bin':
        try:
            print(dec_to_bin(number, []))
        except:
            print(f'Programm can`t convert {number} in the {system}')
    else:
        print('Error type of system. We convert to the dec or the bin')
