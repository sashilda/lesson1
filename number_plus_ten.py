v = input('Введите число от 1 до 10: ')

try:
    v_int=int(v)
except Exception as ex:
    print("oops!")
    exit()

if v_int>=1 and v_int<=10:
    print(v_int+10)
else:
    print("bye")
    exit()