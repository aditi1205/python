#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Tue Sep  7 20:48:12 2021

@author: abhishekdubey

Input:
The first line of input consists of two space-separated integers N, 
M representing no.of students and no.of subjects
The next N lines consist of M space separated integers Ai,j representing i'th student marks in j'th subject.

Output:
Print space separated subject's highest mark in in a single line

Sample Output2
3 4
78 46 75 89
64 56 71 65
67 81 67 77

Sample Output2:
78 81 75 89

"""
import numpy as np

arr = []

firstLineInput = input()
numStudents, numSubjects =  list(map(int, firstLineInput.split(" ")))

for i in range(numStudents):
    iThLineInput = input()
    subjectMarks = np.array(list(map(int, iThLineInput.split(" "))))
    
    col = []
    for j in range(numSubjects):
        col.append(subjectMarks[j])
    arr.append(col)

ndarr = np.asarray(arr)
maxMarksInSubjects = np.amax(ndarr, axis=0)
print(*maxMarksInSubjects)