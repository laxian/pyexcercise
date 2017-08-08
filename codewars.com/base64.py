tb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='


def int_to_bin_str(num):
    ret = ''
    while num // 2 != 0:
        ret += str(num % 2)
        num = num // 2
    ret += str(num % 2)
    return ret[::-1]


def int_to_bin_8(num):
    ret = ''
    while num // 2 != 0:
        ret += str(num % 2)
        num = num // 2
    ret += str(num % 2)

    ret += '0' * (8 - len(ret))
    return ret[::-1]


def bin_str(str):
    lst = []
    for c in str:
        lst.append(int_to_bin_8(ord(c)))
    return ''.join(lst)


def encode(str):
    bin = bin_str(str)
    print(bin)
    ret = []
    while len(bin) >= 6:
        ret.append(tb[bin_str_to_int(bin[:6])])
        bin = bin[6:]
    if len(bin) == 2:
        bin += '0000'
        ret.append(tb[bin_str_to_int(bin)])
        ret.append('==')
    elif len(bin) == 4:
        bin += '00'
        ret.append(tb[bin_str_to_int(bin)])
        ret.append('=')
    return ''.join(ret)


def bin_str_to_int(str):
    '''10010=18'''
    sum = 0
    for c in str:
        sum *= 2
        sum += 1 if c == '1' else 0
    return sum


def restore_bin_str(str):
    ret = ''
    for c in str:
        ret += int_to_bin_8(tb.index(c))[2:]
    if str.endswith('=='):
        ret = ret[:-4]
    elif str.endswith('='):
        ret = ret[:-2]

    return ret


def decode(str):
    str = restore_bin_str(str)
    ret = []
    while len(str) >= 8:
        ret.append(chr(bin_str_to_int(str[:8])))
        str = str[8:]
    return ''.join(ret)

print(encode('GO'))
print(decode('dGhpcyBpcyBhIHN0cmluZyE'))
# print(restore_bin_str('bGF4aWFueg='))
# print(bin_str(1))
# print(bin2int('10001000'))
