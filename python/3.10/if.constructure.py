

# cost=100
# income=110
# interest=(income-cost)/cost
#
# if interest >=0.3:
#     print('高利润');
# elif 0<interest <0.3:
#     print('低利润');
# else:
#     print('负利润')


# interest = float(input('请输入利润率,数值在-1到1之间，如0.3：'))
# if interest >=0.3:
#     print('高利润');
# elif 0<interest <0.3:
#     print('低利润');
# else:
#     print('负利润')

cost= float(input('请输入一个数值，如3000：'))
income= float(input('请输入另一个数值，如3000：'))
interest=float((income-cost)/cost)


if interest >=0.3:
    print('高利润');
elif 0<interest <0.3:
    print('低利润');
else:
    print('负利润')



