# 001 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

num_list = [1, 2, 3, 4, ]
for x1 in num_list:
    for x2 in num_list:
        for x3 in num_list:
            if x1 != x2 and x2 != x3 and x1 != x3:
                print(x1, x2, x3)


# 002 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

# 思路：从高处开始筛选

income = [0, 100000, 200000, 400000, 600000, 1000000][::-1]
print(income)
rating = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01][::-1]

actual_profit = int(input('actual profit:'))
actual_income = 0
for level in income:
    # 获得索引 123
    idx = income.index(level)
    if actual_profit > level:
        actual_income += (actual_profit - level) * rating[idx]
        actual_profit = level

print(actual_income)

# 003 一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？

for x in range(1000):
    if (x + 100)**0.5 % 1 == 0 and (x + 268)**0.5 % 1 == 0:
        print(x)

# 004 输入某年某月某日，判断这一天是这一年的第几天？
# 判断是不是闰年 4 的倍数 不是100的倍数

def leap_year(num):
    if num % 4 == 0 and num % 100 != 0:
        return 1
    else:
        return 0


common_year_mouths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_mouths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years = [common_year_mouths, leap_year_mouths]
days = 0

year, mouth, day = input('year.mouth.day').split('.')
year, mouth, day = int(year), int(mouth), int(day)
actual_year_mouths = years[leap_year(year)]
for i in range(mouth - 1):
    days += actual_year_mouths[i]

days += day
print(days)

# 005 输入三个整数x,y,z，请把这三个数由小到大输出。
x, y, z = input('x,y,z').split(',')
x, y, z = int(x), int(y), int(z)
while not x < y < z:
    if x > y:
        x, y = y, x
    if y > z:
        y, z = z, y
    if x > z:
        x, z = z, x

print(x, y, z)

x, y, z = input('x,y,z').split(',')
x, y, z = int(x), int(y), int(z)
list_xyz = []
list_xyz.append(x)
list_xyz.append(y)
list_xyz.append(z)
list_xyz.sort()
print(list_xyz)


# 006 0、1、1、2、3、5、8、13、21、34、……
def fb(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fb(n - 1) + fb(n - 2)
print(fb(7))


num_list = list()
while x < 100:
    num_list.append(x)
    num_list.append(y)
    x, y = x + y, x + 2 * y

print(num_list)

# 007 将一个列表的数据复制到另一个列表中
list1 = [1, 2, 3]
list2 = list1[:]
# list2.append('4')
print(list2)

# 008 输出 9*9 乘法口诀表
for j in range(1,10):
    for i in range(1,j+1):
        print(i,'*',j,'=',i*j,end='\t')
    print('')

# 009 暂停一秒输出。
import time

for i in range(100):
    print(i)
    time.sleep(1.0)

# 010 暂停一秒输出，并格式化当前时间

import time
import datetime

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))

# 011 古典问题：
# 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

f1 = 1
f2 = 1
list_num = []
for i in range(15):
    list_num.append(f1)
    list_num.append(f2)
    f1 += f2
    f2 += f1
print(list_num)

# 012 判断101-200之间有多少个素数，并输出所有素数。

def prime_number(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime


total = 0
for num in range(101, 201):
    prime = prime_number(num)
    if prime == True:
        print(num)
        total += 1

print(total)

# 013 打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if 100 * i + 10 * j + k == i ** 3 + j ** 3 + k ** 3:
                print(100 * i + 10 * j + k)


