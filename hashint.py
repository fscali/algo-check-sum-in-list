#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

elements = {}
target_sums = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]
def read_file(filename):
    f = open(filename,'rU')
    for line in f:
        elements[int(line)] = int(line)




def main():
    read_file('HashInt.txt')
    result = ''
    for target_sum in target_sums:
        flag = False
        for el in elements.keys():
            complement = target_sum - el
            if complement in elements:
                flag = True
                result += '1'
                break
        if not flag:
            result += '0'
    print(result)

if __name__=='__main__':
    main()

