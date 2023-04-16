# # # 字典和集合
# # # cc={'名字':'老二','名字':'老大'}
# # # # print(cc)
# # # ff=set(cc)
# # # # print(ff)
# #
# #
# # #建立字典，元组，
# # # # a={'c':6,'b':7}
# # # # t=1,2,3,4,5
# # # # t1=[1,2],[4,5],{'c':6,'b':7}
# # # # print(type(t1))
# # 字典取值方法-寻找
# # # # dict={'a':1,'b':2,'c':3}
# # # # print(dict.items())
# # # # for key,value in dict.items():
# # # #     print(key,value)
# #
# # # # info1={'name':'jjj','age':88,'gender':'男'}
# # # # key='name1'
# # # # aaaa=info1.get(key)
# # # # if aaaa is not None:
# # # #     print(aaaa)
# # # # else:
# # # #     print('无')
# # #
# # # #
# #
# #
# # 集合加减
# # # # gather={'否定；的否定给',87687689,('对方地方地方大师傅似的非人',)}
# # # # gather.add('bucuo')
# # # # print(gather)
# #
#
# song = '''
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky. Twinkle,
# twinkle, little star,
# How I wonder what you are!
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# '''
# #易错点，去空值用strip函数去不掉，用replace
# song=str(song.replace('\n','').replace(',','').replace('.','').replace('!','').lower())
# song=song.split() #把字符串分隔成单词，注意不能取空格，否则句子分不出来。
# print(song)
# #
# # # 第一种做法：
# cou={} # 这是空盒子，建一个盒子，就是把数过的字符放进去。
# #错误 ： for i in range(0,len(song1)):
# # #如果是i在range里，那么就是位置值：1235,打印出的结果如：12345,正确做法如：
# for i in song: #开始遍历,后面加的是字符串，所以在字符中遍历，不是在偏移量里遍历。
#     if i not in cou:
#         cou[i]=1
#         #开始建立字典，如果song1出现的字符没有放在盒子里，就给他放进去，并且计数为1，[i]代表键，1代表值
#     else:
#         cou[i]+=1 #如果已经在盒子里，就在原来计数的基础上加1.用加赋值x=x+i, x+=i
# for key in cou: #第一种：这里是在提取键值对，有两种处理方式，
#     print(f'{key}',':一共出现了',cou[key],'次') #f格式化语法：’{变量}‘，‘内容’，字典的键，
# for key,value in cou.items():#第二种：用items函数：for key,value in  字典.items()
#     print(f'{key}', ':一共出现了', cou[key], '次')
# # #第二种做法：
# cou=''  #赋一个空的字符串，当作盒子
# for i in song:
#     if i not in cou:
#         cou_i=1
#     else:
#         cou_i+=1
#     print(f'{i}', ':一共出现了', {cou_i}, '次')
# # #
# # #两种方法对比
# # # # why='否定；的否定给；对方地方地方大师傅似的非人；非二哥认同感肉；体和儿童；以后，儿童。和儿童人。有微软特，吕让他人，特瑞特微软二'
# # # # dic={}
# # # #
# # # # for k in why:
# # # #     if k not in  dic:
# # # #         dic[k]=1
# # # #     else:
# # # #         dic[k]+=1
# # # # for key in  dic:
# # # #     print(key,dic[key])
# # # # why='否定；的否定给；对方地方地方大师傅似的非人；非二哥认同感肉；体和儿童；以后，儿童。和儿童人。有微软特，吕让他人，特瑞特微软二'
# # # # cou_why=''
# # # # for i in why:
# # # #     if i not in cou_why:
# # # #         print(f'{i}:',why.count(i),'次')
# # # #         cou_why+=i
# # # #
# # # # t1 = [(1, 2),(4,2,8),4,6,(7,9,0,9), 5]
# # # # count1=t1.count((4,2,8))
# # # # print(count1)
# #
# #冒泡排序
# # list=[22,55,78,90,3,4,67,29]
# # print(list)
# # for i in range(0,len(list)-1):  #外面的大循环，每一次，以list[i]为基础，两个临近值比较，一共要循环n次，
# #     for i in range(0,len(list)-1):#第一次，以list[0]为基础，俩个临近值互相比较，从前到后两两比较0，一共要n次，
# #         if list[i] > list[i+1]:  #前后元素交换位置
# #             list[i],list[i+1]=list[i+1],list[i]
# # print(list)
# #
#
