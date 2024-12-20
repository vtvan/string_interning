from sys import intern
import random as rd
import time
from string import ascii_letters

str_lens = (100, 10_000, 5_000_000)
loops = (100, 10_000, 1_000_000)

for str_len in str_lens:
    rand_str = ''.join(rd.choices(ascii_letters + ' ', k=str_len))
    str1 = rand_str + ' The End. '
    str2 = rand_str + ' The End. '
    str3 = intern(rand_str + ' The End. ')
    str4 = intern(rand_str + ' The End. ')
    # print(f'{(id(str3) == id(str4)) = }')
    # print(f'{(id(str1) == id(str2)) = }')

    for loop in loops:
        time1 = time.time()
        for _ in range(loop):
            is_equal_sans_interning = (str1 == str2)
        time2 = time.time()
        duration_sans_interning = time2 - time1
        print(f'{str_len = :<12}{loop = :<12}')
        print(f'{duration_sans_interning = }')

        # ================================
        time3 = time.time()
        for _ in range(loop):
            is_equal_with_interning = (str3 == str4)
        time4 = time.time()
        duration_with_interning = time4 - time3
        print(f'{duration_with_interning = }')
        # print()
        print(f'{(duration_with_interning < duration_sans_interning) = }')
        print(f'{(duration_with_interning / duration_sans_interning) = :.10f}')
        print('------')
    print('===========================')