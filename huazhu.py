import csv
import time
# 暗网地址：http://lei6ezsexd4iq2tm.onion
# crm.txt为华住官网注册资料，包括姓名，手机号，游行，身份证号，登陆密码等信息。 全部资料共53G，大约1.23亿条记录
# cusinfo为酒店入住时登记的身份信息，主要为身份证信息，包括姓名，身份证号，家庭住址，生日，内部id号。全部资料共22.3G，大约1.3亿人身份证信息
# history 为酒店开房记录，包括内部id号，同房间关联号，姓名，卡号，手机号，邮箱，入住时间，离开时间，酒店id号，房间号，消费金额等信息。共66.2G，大约2.4亿条记录。
# 以上数据脱裤时间为2018年8月14号。

print('初始化数据……')
t0 = time.clock()
data = []
with open('crm.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    data += rows
with open('cusinfo.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    data += rows
with open('history.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    data += rows
print('完成，用时' + str(time.clock() - t0) + 's，' + str(len(data)) + '条信息')

value = ''
while value != 'quit':
    flag = 0
    value = input('想要查找谁？\n')
    if value != 'quit':
        for person in data:
            person = str(person)
            if value.lower() in person.lower():    
                print(person)
                flag = 1
    else:
        pass
    if flag == 1:
        print('找到了以上相关信息，请确认\n')
    elif flag == 0 and value != 'quit':
        print('黑客泄露的三万条测试数据中没有' + str(value) + '的信息。\n')
