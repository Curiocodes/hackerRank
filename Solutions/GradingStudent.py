#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)) :
        grade = grades[i]
        multiples = int(grade/5)
        nextValue = (multiples * 5) + 5 
        if nextValue - grade < 3 :
            if(nextValue >= 40):
                grades[i] = nextValue
                    
        
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
