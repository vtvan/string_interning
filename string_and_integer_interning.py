from sys import intern

# # 字串中有空白者不intern
# name1 = '  Alex   Van is a Pythonista.   '
# name2 = '  Alex   Van is a Pythonista.   '

# print(f'{name1 = }\t\t\t{name2 = }')
# print(f'{id(name1) = :<28}{id(name2) = }')
# print(f'{(id(name1) == id(name2)) = }')

# -------------------
# 改用intern()函數。
# name1 = intern('  Alex   Van is a Pythonista.   ')
# name2 = intern('  Alex   Van is a Pythonista.   ')

# print(f'{name1 = }\t\t\t{name2 = }')
# print(f'{id(name1) = :<28}{id(name2) = }')
# print(f'{(id(name1) == id(name2)) = }')

# ======================================================
# 內含ASCII 128以上字元者不intern
# os1 = 'Linux©'     # ©是ASCII 128以上的字元。
# os2 = 'Linux©'

# print(f'{os1 = }\t\t\t{os2 = }')
# print(f'{id(os1) = :<22}{id(os2) = }')
# print(f'{(id(os1) == id(os2)) = }')

# -------------------
# 改用intern()函數。
# os1 = intern('Linux©')
# os2 = intern('Linux©')

# print(f'{os1 = }\t\t\t{os2 = }')
# print(f'{id(os1) = :<22}{id(os2) = }')
# print(f'{(id(os1) == id(os2)) = }')

# ++++++++
# name1 = '張曼玉'
# name2 = '張曼玉'

# print(f'{name1 = }\t\t{name2 = }')
# print(f'{id(name1) = :<20}{id(name2) = }')
# print(f'{(id(name1) == id(name2)) = }')

# -------------------
# 改用intern()函數。
# name1 = intern('張曼玉')
# name2 = intern('張曼玉')

# print(f'{name1 = }\t\t{name2 = }')
# print(f'{id(name1) = :<20}{id(name2) = }')
# print(f'{(id(name1) == id(name2)) = }')

# ======================================================

# 長度超過4,096個字元的字串不intern
# leng = 4097
# str1 = 'A' * 4097    # 連用5個4_096，何以不用變數？
# str2 = 'A' * 4097    # Alex是否功力大退？
# str3 = 'A' * 4097    # 當然不是。
# str4 = 'A' * 4097    # 請耐心看下去，自然明白。
# str5 = 'A' * 4097
# print(f'{id(str1)=:<20}{id(str2)=:<20}{id(str3)=:<20}{id(str4)=:<20}{id(str5)=}')
# print(f'{(id(str1) == id(str2) == id(str3) == id(str4) == id(str5)) = }')

# -------------------
# 改用intern()函數。
# str1 = intern('A' * 4_097)
# str2 = intern('A' * 4_097)

# print(f'{id(str1)=:<20}{id(str2)=:<20}')
# print(f'{(id(str1) == id(str2)) = }')

# ======================================================

# 字串由variable組合而成者不intern
# first = 'first'
# last = 'last'
# name1 = 'first' + 'last'
# name2 = 'first' + last

# print(f'{name1 = }\t\t{name2 = }')
# print(f'{id(name1) = :<20}{id(name2) = }')
# print(f'{(id(name1) == id(name2)) = }')

# -------------------
# 改用intern()函數。
# str1 = intern('A' * 4_097)
# str2 = intern('A' * 4_097)

# print(f'{id(str1)=:<20}{id(str2)=:<20}')
# print(f'{(id(str1) == id(str2)) = }')

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^  整數  ^^
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# num1 = -5    # implicit的整數interning範圍為-5 ~ 256。
# num2 = -5
# print(f'{num1 = }\t\t{num2 = }')
# print(f'{id(num1) = :<20}{id(num2) = }')
# print(f'{(id(num1) == id(num2)) = }')

# print()
num1 = -6**19
num2 = -6**19
print(f'{num1 = }\t\t{num2 = }')
print(f'{id(num1) = :<20}{id(num2) = }')
print(f'{(id(num1) == id(num2)) = }')
print(f'{num1 is num2 = }')
# print()
# num1 = 256
# num2 = 256
# print(f'{num1 = }\t\t{num2 = }')
# print(f'{id(num1) = :<20}{id(num2) = }')
# print(f'{(id(num1) == id(num2)) = }')

# print()
# num = 999999999999999999999999*9999999999999999999999999999999999*999999999999999999999999
# num1 = num
# num2 = num
# print(f'{num1 = }\t\t{num2 = }')
# print(f'{id(num1) = :<20}{id(num2) = }')
# print(f'{(id(num1) == id(num2)) = }')