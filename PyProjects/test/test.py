filename = 'test.py'

try:
    10/3
    with open(filename) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    print('找不到文件')
except ZeroDivisionError:
    print('不能被0除')
else:
    for line in lines:
        print(line.rstrip())
