#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 23:56:33 2021

@author: abhishekdubey
"""

n = int(input())

myDict = {}
medicineTypeIdCountList = []

highestOccuringIdList = []

for i in range(n):
    medicineTypeId = int(input())
    
    if (medicineTypeId not in myDict):
        myDict.update({medicineTypeId:1})
    else:
        myDict.update({medicineTypeId:myDict.get(medicineTypeId)+1})
    

for x, y in myDict.items():
    medicineTypeIdCountList.append(y)


maxValue = sorted(medicineTypeIdCountList, reverse=True)[0]

for x, y in myDict.items():
    if y == maxValue:
        highestOccuringIdList.append(x)

minMedicineId = sorted(highestOccuringIdList, reverse=False)[0]

print("minMedicineId", minMedicineId)