__author__ = 'katya'
hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def convert_hex_to_int(longnum):
    x = len(longnum) % 8
    if x == 0:
        longnum = longnum
    else:
        longnum = str((8-x) * '0' + longnum)

    result = []

    while longnum:
        slice = longnum[-8:]
        longnum = longnum.replace(slice, '')
        degree = 28
        preres = 0
        for i in slice:
            for z in hex:
                if i == z:
                    preres = preres + (hex.index(z) << degree)
                    degree = degree - 4

        result.append(preres)

        """
        love_kate = ""
        for elem in result:
            love_kate += str(elem)
            #print result
        print int(love_kate)"""
    print result
    return result


def convert_int_to_hex(result):
    res_for_inttohex = ''
    for i in range(0, len(result)):
        x1 = ((result[i] >> 28) & 15)
        x2 = ((result[i] >> 24) & 15)
        x3 = ((result[i] >> 20) & 15)
        x4 = ((result[i] >> 16) & 15)
        x5 = ((result[i] >> 12) & 15)
        x6 = ((result[i] >> 8) & 15)
        x7 = ((result[i] >> 4) & 15)
        x8 = ((result[i]) & 15)

        for1 = hex[x1] + hex[x2] + hex[x3] + hex[x4]+ hex[x5] + hex[x6] + hex[x7] + hex[x8]
        res_for_inttohex = for1 + res_for_inttohex

    #if res_for_inttohex[0] == '0' and res_for_inttohex[1] != '':
        #res_for_inttohex = res_for_inttohex.replace('0', '')


    print res_for_inttohex


def long_add(num1, num2):
    carry = 0
    c = []
    res = 0
    for i in range(0, len(num2)):
        temp = num1[i] + num2[i] + carry
        c.append(temp & (0xFFFFFFFF))
        carry = temp >> 32
    convert_int_to_hex(c)


def long_sub(num1, num2):
    borrow = 0
    c = []
    if num1 < num2:
        print 'Try again! num2 must be bigger than num1 '
    else:
        for i in range(0, len(num2)):
            temp = num1[i] - num2[i] - borrow
            if temp >= 0:
                c.append(temp)
                borrow = 0
            else:
                cp = 0x100000000 + temp
                c.append(cp)
                borrow = 1
        convert_int_to_hex(c)



def long_cmp(num1, num2):
    i = len(num1) - 1
    j = len(num1) - 1

    while num1[j] == num2[j] and j >= 0:
        j -= 1
        i -= 1
    if i == -1:
        return 0

    elif num1[i] > num2[i]:
        return 1
    else:
        return -1

def long_shift_digits_to_high(val1, val2):
    for i in range(0, val2):
        val1.append(0)
    return val1






def long_mul_const(num, const):
    carry = 0
    c = []
    for i in range(0, len(num)):
        temp = num[i] * const + carry
        c.append(temp & 0xFFFFFFFF)
        carry = temp >> 32
        c.append(carry)
    #print c
    return c

def long_mul(num1, num2):
    c = []
    for i in range(0, 2*len(num1)):
        c.append(0)
    c = c[:len(c)-1]
    for i in range(0, len(num1)):
        temp = long_mul_const(num1, num2[i])
        long_shift_digits_to_high(temp, i)
        c = long_add(temp, c)
    print c
    convert_int_to_hex(c)



def long_square(num):
    #print long_mul(convert_hex_to_int(num), convert_hex_to_int(num))
    return long_mul(convert_hex_to_int(num), convert_hex_to_int(num))

def long_shift_bits_to_high(n1, n2):
    n = (n1 << n2) & 15
    return n

def long_div_mod(num1, num2):
    k = num2.bit_length()
    R = num1
    Q = 0
    x = long_cmp(R, B)
    while (x == 0) or (x == 1):
        t = R.bit_length()
        print t
        C = long_shift_bits_to_high(B, t - k)
        y = long_cmp(R, C)
        if y == -1 :
            t = t - 1
            C = LongShiftBitsToHigh(B, t - k)
            R = R - C
            Q = Q + 2**(t - k)
    return Q, R


def convert_to_binary_from_hex(hex_number):
    result = []
    bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    for ch in hex_number:
        result.append(bin[ch])
    #print result
    return result

def int_to_str(num):
    num = str(num)
    res_for_inttohex = ''
    while num:
        slice = num[-8:]
        num = num.replace(slice, '')
        x1 = ((int(slice) >> 28) & 15)
        x2 = ((int(slice) >> 24) & 15)
        x3 = ((int(slice) >> 20) & 15)
        x4 = ((int(slice) >> 16) & 15)
        x5 = ((int(slice) >> 12) & 15)
        x6 = ((int(slice) >> 8) & 15)
        x7 = ((int(slice) >> 4) & 15)
        x8 = (int(slice) & 15)

        for1 = hex[x1] + hex[x2] + hex[x3] + hex[x4]+ hex[x5] + hex[x6] + hex[x7] + hex[x8]
        res_for_inttohex = for1 + res_for_inttohex
        while res_for_inttohex[0] == '0':
            res_for_inttohex = res_for_inttohex.replace('0', '')
    print res_for_inttohex






def long_power(a, b):
    ##print b
    num = ''
    for x in b:
        num += str(x)
    #num = int(num)
    c = 1
    for i in range(0, len(str(num))):
        if num[i] == '1':
            c = long_mul(c, b)
            a = long_mul(a, a)
    return c




#convert_hex_to_int('FFFFFFFE00000001')
#convert_int_to_hex([2271560481, 19088743])
#long_add(convert_hex_to_int('FFAAEEE1243647'), convert_hex_to_int('AAAEE'))
#long_sub(convert_hex_to_int('111'), convert_hex_to_int('111'))
#long_cmp(convert_hex_to_int('FFAAEEE1243647'), convert_hex_to_int('AAAEEF25367652'))
#long_shift_digits_to_high([12121212], 7)
#long_mul_const(convert_hex_to_int('11111111'), 286331153 )
long_mul(convert_hex_to_int('FFAAEEE1243647'), convert_hex_to_int('AAAEEF25367652'))
#long_square('FFFF')
#long_div_mod(convert_hex_to_int('2468'), convert_hex_to_int('1234'))
#long_power(convert_hex_to_int('23152315'), convert_to_binary_from_hex('FFFF'))
#convert_to_binary_from_hex('FFFF')
#int_to_str(18446744065119617025)