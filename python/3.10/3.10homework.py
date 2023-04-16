ticket=5000
discount1=0.9
discount2=0.6
discount3=0.5
discount4=0.4
dticket1=ticket*discount1
dticket2=ticket*discount2
dticket3=ticket*discount3
dticket4=ticket*discount4


month=int(input('请输入您的出行月份：1-12:\n'))
choice =int( input('请问您选择头等舱还是经济舱？头等舱输入1，经济舱输入2\n'))

if 2<month<11 and choice == 1:
    print(f'您的机票价格为:{dticket1}')
elif 2<month<11 and choice == 2:
    print(f'您的机票价格为:{dticket2}')
elif month>10 or month<3 and choice == 1:
    print(f'您的机票价格为:{dticket3}')
else:
    print(f'您的机票价格为:{dticket4}')

#print("您的机票价格为:"+str(dticket4))
