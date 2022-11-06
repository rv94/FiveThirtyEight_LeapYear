# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:45:56 2022

@author: vigne
"""
#Import libraries
import pandas as pd

# #Commenting out as LP formulation doesn't work - cannot divide by a DV
# from pulp import *

# # Create the 'prob' variable to contain the problem data
# prob = LpProblem("LeapYearProblem", LpMinimize)

# #Decision Variables
# L = LpVariable(name = "NoOfLeapYears",
#                 lowBound = 1,
#                 cat = 'Integer')

# N = LpVariable(name = "NoOfTotalYears",
#                 lowBound = 4,
#                 upBound = 400,
#                 cat = 'Integer')

# #Add Objective
# prob += abs((((365*N)+L)/L)-365.24217)

##Brute Force it like a caveman

#Get variables
NoOfTotalYears = int(4)
NoOfLeapYears = int(1)

#Initialize data frame
AnswerDF = pd.DataFrame(columns = ['LeapYears', 'TotalYears', 'DaysPerYear', 'DaysDifference'])

#Write Loop & append to data frame through iteration
for NoOfTotalYears in range(4, 401):
    for NoOfLeapYears in range(1, int((NoOfTotalYears/4)+1)):
        DPY = float(((365 * NoOfTotalYears) + NoOfLeapYears)/NoOfTotalYears)
        DayDiff = abs(float(DPY - 365.24217))
        AnswerDF = AnswerDF.append({'LeapYears':NoOfLeapYears,
                                    'TotalYears':NoOfTotalYears,
                                    'DaysPerYear':DPY, 
                                    'DaysDifference':DayDiff},
                                   ignore_index=True)
        
#Re-sort data frame
AnswerDF = AnswerDF.sort_values(by = 'DaysDifference')

NoOfLeapYears_Answer = int(AnswerDF.head(1).LeapYears)
NoOfTotalYears_Answer = int(AnswerDF.head(1).TotalYears)
DPY_Answer = float(AnswerDF.head(1).DaysPerYear)


#Print answer
print('''The answer is {0:d} leap days out of every {1:d} years, averaging to {2:f} days per year.
         '''.format(NoOfLeapYears_Answer, NoOfTotalYears_Answer, DPY_Answer))

