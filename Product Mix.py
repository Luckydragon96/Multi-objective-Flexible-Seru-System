# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:54:41 2021

@author: 81514
"""
import numpy as np
import random


orders=20
numberOfProduct=4

#分别按照产品产生相应订单
#按照每种产品的分布和订单到达间隔生成每种产品的订单列表，然后根据达到时间选取前30个订单
def produceProductsOrders(orders,numberOfProduct):#生成随机场景
    #按照产品需求分布产生每种产品的需求量
    Order_List = []
    record_times = [0 for i in range(numberOfProduct)]#记录产品到达的次数
    LastTime = [0 for i in range(numberOfProduct)]#记录最后订单的到达时间
    #print('record_times',record_times)
    index = [i for i in range(numberOfProduct)]
    #print('index',index)
    while (len(Order_List) < (orders)):
        #print('###############下一次循环################')
        #随机产生一个数，来确定下个订单是哪种产品类型
        random_item = random.choice(index)
        #print('random_item',random_item)
        #根据需求分布，随机产生需求量
        if random_item == 0:
            batch = int(np.random.normal(30,30))
        elif random_item == 1:
            batch = int(np.random.normal(50,30))
        elif random_item == 2:
            batch = int(np.random.normal(80,30))
        else:
            batch = int(np.random.normal(100,30))
        #print('batch',batch)
        #批量不能小于0，生成每种产品的订单需求
        if batch > 0:
            #给每个订单按照订单间隔分布，随机生成一个到达时间
            if record_times[random_item] == 0:#该产品的首个订单到达时间为0
                arriveTime = 0
            else:
                if random_item == 0: 
                    intervalTime = int(np.random.normal(100,10))
                elif random_item == 1:
                    intervalTime = int(np.random.normal(150,15))
                elif random_item == 2:
                    intervalTime = int(np.random.normal(200,20))
                else:
                    intervalTime = int(np.random.normal(250,25))    
                #print('intervalTime',intervalTime)
                arriveTime = LastTime[random_item] + intervalTime
                #print('arriveTime',arriveTime)    
            record_times[random_item] += 1
            #print('record_times',record_times)
            LastTime[random_item] += arriveTime
            #print('LastTime',LastTime)
            Order_List.append([random_item+1,batch,arriveTime]) 
            #print('Order_List',Order_List)
            Order_List.sort(key= lambda x: x[2])
            #print('Order_List',Order_List)
        else:
            continue
    return Order_List
produceProductsOrders(orders,numberOfProduct)

scenarios=500
OrderList=[]
for i in range(scenarios):
    order=produceProductsOrders(orders,numberOfProduct)
    OrderList.append(order)
print('OrderList',OrderList)
    
    
      
    

#print('cpzh_list',cpzh_list)
#print('矩阵',cpzh_list)

#np.savetxt('10cp_zuhe.txt',cpzh_list)
 
#np.savetxt('5cp_zuhe(sumis500).txt',cpzh_list, delimiter=" ", fmt='%s')

