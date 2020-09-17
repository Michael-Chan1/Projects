import pandas as pd
from typing import List
from random import randint

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def export_excel(first_name: int, last_name: int, sin: int, ssn: int,
                 # snid: int, apac_c: int, apac_h: int, apac_i: int,
                 # apac_k: int, apac_t: int
                 ) -> None:
    ids = {'First_Name': get_first_names(first_name),
           'Last_Name': get_last_names(last_name), 'SIN': get_sin(sin),
           'SSN': get_ssn(ssn)}

    max_ids = max(len(ids['First_Name']), len(ids['Last_Name']),
                  len(ids['SIN']), len(ids['SSN']))
    while len(ids['First_Name']) < max_ids:
        ids['First_Name'].append(' ')
    while len(ids['Last_Name']) < max_ids:
        ids['Last_Name'].append(' ')
    while len(ids['SIN']) < max_ids:
        ids['SIN'].append(' ')
    while len(ids['SSN']) < max_ids:
        ids['SSN'].append(' ')

    df = pd.DataFrame(ids, columns=['First_Name', 'Last_Name', 'SIN', 'SSN'])
    # print(df)
    df.to_excel('export_dataframe.xls')


def get_first_names(num: int) -> List[str]:
    f = open('first_names.txt')
    new_list = []
    lst = []
    for line in f:
        current_line = line.split(',')
        new_list.append(current_line[0][:len(current_line) - 2])
    for _ in range(num):
        index = randint(0, len(new_list) - 1)
        lst.append(new_list.pop(index))
    return lst


def get_last_names(num: int) -> List[str]:
    f = open('last_names.txt')
    new_list = []
    lst = []
    for line in f:
        current_line = line.split(',')
        new_list.append(current_line[0][:len(current_line) - 2])
    for _ in range(num):
        index = randint(0, len(new_list) - 1)
        lst.append(new_list.pop(index))
    return lst


def get_sin(num: int) -> List[str]:
    lst = []
    for _ in range(num):
        valid = False
        temp_num = randint(100000000, 999999999)
        while not valid and temp_num in lst:
            if _check_sin(temp_num):
                valid = True
            else:
                temp_num += 1
        ran_num = randint(1,3)
        if ran_num == 1:
            lst.append(str(temp_num))
        elif ran_num == 2:
            str_num = str(temp_num)
            sin = str_num[0:3] + ' ' + str_num[3:6] + ' ' + str_num[6:9]
            lst.append(sin)
        else:
            str_num = str(temp_num)
            sin = str_num[0:3] + '-' + str_num[3:6] + '-' + str_num[6:9]
            lst.append(sin)
    return lst


def _check_sin(num: int) -> bool:
    check = str(num)
    new_num = 0
    odd = True
    for digit in check:
        if odd:
            new_num += int(digit)
            odd = False
        else:
            if 2 * int(digit) >= 10:
                new_num += 2 * int(digit) - 9
            else:
                new_num += 2 * int(digit)
            odd = True
    return new_num % 10 == 0


def get_ssn(num: int) -> List[str]:
    lst = []
    for _ in range(num):
        area_number = randint(1,899)
        while area_number == 666 and area_number in lst:
            area_number = randint(1, 899)
        group_number = randint(1, 99)
        serial_number = randint(1, 9999)
        ran_num = randint(1,3)
        temp_num = area_number * 1000000 + group_number * 10000 + serial_number
        if ran_num == 1:
            lst.append(str(temp_num))
        elif ran_num == 2:
            str_num = str(temp_num)
            sin = str_num[0:3] + ' ' + str_num[3:5] + ' ' + str_num[5:9]
            lst.append(sin)
        else:
            str_num = str(temp_num)
            sin = str_num[0:3] + '-' + str_num[3:5] + '-' + str_num[5:9]
            lst.append(sin)
    return lst


def get_snid(num: int):
    lst = []
    for _ in range(num):
        area_number = randint(1, 899)
        while area_number == 666 and area_number in lst:
            area_number = randint(1, 899)
        group_number = randint(1, 99)
        serial_number = randint(1, 9999)
        ran_num = randint(1, 3)
        temp_num = area_number * 1000000 + group_number * 10000 + serial_number
        if ran_num == 1:
            lst.append(str(temp_num))
        elif ran_num == 2:
            str_num = str(temp_num)
            sin = str_num[0:3] + ' ' + str_num[3:5] + ' ' + str_num[5:9]
            lst.append(sin)
        else:
            str_num = str(temp_num)
            sin = str_num[0:3] + '-' + str_num[3:5] + '-' + str_num[5:9]
            lst.append(sin)
    return lst
