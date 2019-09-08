# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:50:43 2019

@author: Kunal Jani
"""

import numpy as np
import math as mt

#Declare the possible amount that can be won if the bank offer is not accepted.
amounts=[1,5,10,50,75,100,200,300,400,500,750,1000,5000,10000,20000,50000,75000,100000,200000,300000,
         400000,500000,750000,1000000]
cases=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
#print(cases)
#Randomly assign the values that can be won to the different cases
values=[]
remaining_amounts=[]
for i in range(len(amounts)):
    remaining_amounts.append(amounts[i])
eliminated_amounts=[]
for i in range(len(cases)):
    amt=np.random.uniform(0,len(amounts))
    amt_int=int(amt)
    values.append(amounts[amt_int])
    amounts.pop(amt_int)

#print(values)

#Check is a valid case is chosen.

case_no=-1
while(case_no<0 or case_no>23):
    print('Choose your case number from 0 to 23')
    case_number=input()
    case_no=int(case_number)
    if(case_no<0 or case_no>23):
        print('Case number does not exist')
    else:
        break

your_case=cases[case_no]
your_value=values[case_no]
values.pop(case_no)
cases.pop(case_no)
#print(cases)
#print(values)
#print('Your case number is '+str(your_case))
#print('Your value is '+str(your_value))

#The game of choosing the cases starts here.
no_of_cases_left_to_open=6
deal=False
total_iterations=0
bank_offer=0
amount_accepted=0
while(deal!=True or len(cases)!=0):
    trials=no_of_cases_left_to_open
    while(trials>0):
        print(cases)
        print('Enter case number')
        case_selected=input()
        case_sel=int(case_selected)
        pop_value=0
        for i in range(len(cases)):
            if(cases[i]==case_sel):
                pop_value=i
                break
        #If a case with a higher value is selected, the bank offer drops, else the 
        #bank offer rises.
        if(values[pop_value]>=0 and values[pop_value]<100):
            bank_offer=bank_offer+np.random.uniform(25000,30000)
        if(values[pop_value]>100 and values[pop_value]<=1000):
            bank_offer=bank_offer+np.random.uniform(15000,25000)
        if(values[pop_value]>1000 and values[pop_value]<=75000):
            bank_offer=bank_offer+np.random.uniform(5000,15000)
        if(values[pop_value]>100000 and values[pop_value]<=300000):
            nmval=np.random.uniform(15000,25000)
            if(bank_offer-nmval>0):
                bank_offer=bank_offer-nmval
        if(values[pop_value]>300000 and values[pop_value]<=500000):
            nmval=np.random.uniform(25000,50000)
            if(bank_offer-nmval>0):
                bank_offer=bank_offer-nmval
        if(values[pop_value]>500000 and values[pop_value]<=1000000):
            nmval=np.random.uniform(50000,75000)
            if(bank_offer-nmval>0):
                bank_offer=bank_offer-nmval
        total_iterations=total_iterations+1
        #print(remaining_amounts)
        print('Value in case:'+str(values[pop_value]))
        remaining_amounts.remove(values[pop_value])
        eliminated_amounts.append(values[pop_value])
        print('Remaining amounts:')
        print(remaining_amounts)
        print('eliminated amounts:')
        print(eliminated_amounts)
        cases.pop(pop_value)
        values.pop(pop_value)
        trials=trials-1
    #If the bank offer is accepted, the game is over, else the game continues
    #till the number of cases which are remaining are zero.
    print('New offer is:'+str(bank_offer))
    print('Do you want to accept the offer?(1/0)')
    decision=input()
    decs=int(decision)
    if(decs==1):
        deal=True
        amount_accepted=bank_offer
        break
    else:
        deal=False
    if(cases==[]):
        break
    if(no_of_cases_left_to_open!=1):
        no_of_cases_left_to_open=no_of_cases_left_to_open-1
        
if(deal):
    print('You earned:'+str(amount_accepted))
    print('Amount in your case:'+str(your_value))
else:
    print('You earned:'+str(your_value))    
